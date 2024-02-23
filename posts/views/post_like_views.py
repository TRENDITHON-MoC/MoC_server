from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *
from posts.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import *

class PostLikeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, post_id):
        user = request.user
        post = Post.objects.get(pk = post_id)
        if post.like.filter(pk = user.pk).exists():
            post.like.remove(user)
            post.like_cnt -= 1
            res = {
                "msg" : "좋아요 해제",
                "data" : post.like_cnt
            }
        else:
            post.like.add(user)
            post.like_cnt += 1
            res = {
                "msg" : "좋아요 추가",
                "data" : post.like_cnt
            }
        return Response(res, status = status.HTTP_200_OK)