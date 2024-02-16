from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('dev/kakao/', DevKakaoLoginView.as_view()), # 개발자 로그인
    path('kakao/login/callback/', DevKaKaoCallbackView.as_view()), # 개발자 로그인 콜백
    path('token/refresh/', TokenRefreshView.as_view()), # 토큰 리프레시
    path('token/logout/', LogoutView.as_view()), # 로그아웃
    path('profileImage/upload/', UploadProfileView.as_view()),
    path('profileImage/select/<str:type>/', SelectProfileView.as_view()),
]