from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('dev/kakao/', DevKakaoLoginView.as_view()), # 개발자 로그인
    path('kakao/login/callback/', DevKaKaoCallbackView.as_view()), # 개발자 로그인 콜백
    path('kakao/login/<str:code>/', KaKaoCallbackView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()), # 토큰 리프레시
    path('token/logout/', LogoutView.as_view()), # 로그아웃
    path('profileImage/upload/', UploadProfileView.as_view()), # MoC 프로필 이미지 업로드
    path('profileImage/select/<str:type>/', SelectProfileView.as_view()), # 프로필 이미지 선택
    path('mypage/', MyPageView.as_view()),
]