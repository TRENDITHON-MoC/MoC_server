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


class MyPageView(APIView):
    """
    마이페이지에 필요한 정보를 출력하는 뷰
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user_serializer = UserResponseSerializer(request.user)
        post_serializer = PostListSerializer(request.user.posts.order_by('-created_at'), many = True, context = {'request' : request})
        comment_serializer = CommentMyPageSerializer(request.user.comments.order_by('-created_at'), many = True)

        res = {
            "msg" : "마이페이지 정보 반환 성공",
            "data" : {
                "user_info" : user_serializer.data,
                "post_list" : post_serializer.data,
                "comment_list" : comment_serializer.data
            }
        }
        return Response(res, status = status.HTTP_200_OK)
    

class MyLikedPostView(APIView):
    """
    내가 좋아요 한 글을 출력하는 뷰
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        posts = user.like_post.all()
        serializer = PostListSerializer(posts.order_by('-created_at'), many = True, context = {'request':request})
        
        return Response(serializer.data, status = status.HTTP_200_OK)
