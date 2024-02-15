from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('dev/kakao/', DevKakaoLoginView.as_view()),
    path('kakao/login/callback/', DevKaKaoCallbackView.as_view()),
]