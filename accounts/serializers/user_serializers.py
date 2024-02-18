from rest_framework import serializers
from ..models import User
from django.conf import settings

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
    profile_image = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'nickname', 'profile_image']

    def get_profile_image(self, obj):
        request = self.context.get('request')
        if obj.profile_image_type == 'NATIVE':
            if obj.native_profile_image:
                return request.build_absolute_uri(settings.MEDIA_URL + str(obj.native_profile_image))
            else:
                return None
        elif obj.profile_image_type == 'KAKAO':
            if obj.kakao_profile_image:
                return obj.kakao_profile_image 
            else:
                return None
        else:
            return None