from rest_framework import serializers
from ..models import User

class UserCreateSerailizer(serializers.ModelSerializer):
    """
    유저 생성 시리얼라이저
    """
    class Meta:
        model = User
        fields = ['kakao_id', 'nickname', 'kakao_profile_image']


class UserResponseSerializer(serializers.ModelSerializer):
    """
    유저 정보 응답 시리얼라이저
    """
    class Meta:
        model = User
        fields = ['id', 'nickname', 'profile_image']