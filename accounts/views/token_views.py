from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import *


class CustomTokenRefreshView(TokenRefreshView):
    """
    리프레시 토큰으로 새로운 토큰을 발급하는 뷰
    """
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """
    리프레시 토큰을 무효화하여 로그아웃 하는 뷰
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            res = {
                "msg" : "로그아웃 성공"
            }
            return Response(res, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            res = {
                "msg" : "로그아웃 실패"
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)