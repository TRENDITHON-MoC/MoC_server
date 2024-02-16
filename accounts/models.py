from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    """
    유저 생성 매니저
    """
    def create_user(self, google_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        # 사용자 생성 로직
        user = self.model(google_id=google_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, google_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # 슈퍼유저 생성 로직
        return self.create_user(google_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    유저 모델
    """
    PROFILE_IMAGE_CHOICES = (
        ('KAKAO', '카카오 프로필 사진'),
        ('NATIVE', 'MoC 프로필 사진')
    )
    kakao_id = models.CharField(max_length=30, unique=True, null = True)
    nickname = models.CharField(max_length=30, null = True) # 한글 10글자
    native_profile_image = models.ImageField(upload_to = 'profileImages/', blank=True, null=True)
    kakao_profile_image = models.TextField(blank=True, null=True)
    profile_image_type = models.CharField(max_length = 60, choices = PROFILE_IMAGE_CHOICES, default= 'KAKAO')
    USERNAME_FIELD = 'kakao_id'
    EMAIL_FIELD = None
    REQUIRED_FIELDS = []

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nickname
    
    @property
    def profile_image(self):
        if self.profile_image_type == 'KAKAO':
            return self.kakao_profile_image
        elif self.profile_image_type == 'NATIVE':
            if self.native_profile_image:
                return self.native_profile_image
            else:
                return None
        else:
            return None
    
    class Meta:
        db_table = 'user'