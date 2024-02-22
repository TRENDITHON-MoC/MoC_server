from rest_framework.views import APIView
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from ..serializers import *
from ..models import *
import requests
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from decouple import config


class DevKakaoLoginView(APIView):
    """
    개발자용 카카오 로그인 뷰
    """
    def get(self, request):
        kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        redirect_uri = config('KAKAO_REDIRECT_URI')
        client_id = config('KAKAO_REST_API_KEY')

        return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}")
    

class ServerDevLoginView(APIView):
    def get(self, request):
        kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        redirect_uri = "https://momentcraft.site/accounts/kakao/login/callback/"
        client_id = config('KAKAO_REST_API_KEY')

        return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}")    
    

class DevKaKaoCallbackView(APIView):
    """
    개발자용 액세스 토큰 발급 뷰
    """
    def get(self, request):
        data = {
            "grant_type" : "authorization_code",
            "client_id" : config('KAKAO_REST_API_KEY'),
            "redirect_uri" : config('KAKAO_REDIRECT_URI'),
            "code" : request.GET["code"]
        }

        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        response = requests.post(kakao_token_api, data=data).json()
        kakao_token = response.get("access_token")

        kakao_user_api = "https://kapi.kakao.com/v2/user/me"
        header = {"Authorization":f"Bearer ${kakao_token}"}
        user_information = requests.get(kakao_user_api, headers = header).json()

        kakao_id = user_information['id']
        kakao_profile_image = user_information["kakao_account"]["profile"]["thumbnail_image_url"]
        nickname = user_information["properties"]["nickname"]

        user = User.objects.filter(kakao_id = kakao_id).first()
        
        if user is not None:
            if user.kakao_profile_image != kakao_profile_image:
                user.kakao_profile_image = kakao_profile_image
            if user.nickname != nickname:
                user.nickname = nickname
            user.save()
            serializer = UserResponseSerializer(user, context = {'request' : request})
            token = TokenObtainPairSerializer.get_token(user)
            access_token = str(token.access_token)
            refresh_token = str(token)

            res = {
                "msg" : "기존 사용자 로그인",
                "data" : {
                    "user" : serializer.data,
                    "access_token" : access_token,
                    "refresh_token" : refresh_token,
                    "exist_user" : True
                }
            }
            return Response(res, status = status.HTTP_200_OK)
        
        new_user = User(kakao_id = kakao_id, kakao_profile_image = kakao_profile_image, nickname = nickname)
        new_user.save()
        serializer = UserResponseSerializer(new_user, context = {'request' : request})
        token = TokenObtainPairSerializer.get_token(new_user)
        access_token = str(token.access_token)
        refresh_token = str(token)

        res = {
            "msg" : "신규 사용자 로그인",
            "data" : {
                "user" : serializer.data,
                "access_token" : access_token,
                "refresh_token" : refresh_token,
                "exist_user" : False
            }
        }
        return Response(res, status = status.HTTP_200_OK)