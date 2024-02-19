from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers import *
from ..models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import *
from ..permissions import IsOwnerOrReadOnly
from PIL import Image
from io import BytesIO
from django.utils.timezone import now
from posts.serializers.posts_serializers import *
from comments.serializers.comments_serializers import *


class SelectProfileView(APIView):
    """
    카카오/MoC 중 프로필 사진을 선택하는 뷰
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, type):
        if type == "KAKAO":
            request.user.profile_image_type = "KAKAO"
            request.user.save()
        elif type == "NATIVE":
            request.user.profile_image_type = "NATIVE"
            request.user.save()
        else:
            res = {
                "msg" : "등록되지 않은 프로필 이미지 타입"
            }
            return Response(res, status = status.HTTP_400_BAD_REQUEST)
        res = {
            "msg" :f"사용자의 프로필 이미지를 {type}로 변경",
            "data" : UserResponseSerializer(request.user, context = {'request' : request}).data
        }
        return Response(res, status = status.HTTP_200_OK)
    

class UploadProfileView(APIView):
    """
    MoC 프로필 이미지 업로드
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.profile_image_type != "NATIVE":
            res = {
                "msg" : "현재 MoC 프로필 이미지가 선택되어 있지 않습니다."
            }
            return Response(res, status = status.HTTP_400_BAD_REQUEST)
        
        image = Image.open(request.FILES['image'])
        image = image.convert('RGB')

        image.thumbnail((500, 500))
        buffer = BytesIO()
        image.save(buffer, format = 'JPEG', quality = 80)
        buffer.seek(0)
    
        file_name = f"{request.user.nickname}/{request.user.nickname}_{now().strftime('%Y%m%d%H%M%S')}.jpeg"
        request.user.native_profile_image.save(f'{file_name}', buffer, save=True)
        res = {
            "msg" : "프로필 이미지 업로드 성공",
            "data" : UserResponseSerializer(request.user, context = {'request' : request}).data
        }
        return Response(res, status = status.HTTP_201_CREATED)