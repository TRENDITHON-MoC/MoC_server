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
            "msg" :f"사용자의 프로필 이미지를 {type}으로 변경",
            "data" : UserResponseSerializer(request.user).data
        }
        return Response(res, status = status.HTTP_200_OK)