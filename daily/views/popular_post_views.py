from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *
from posts.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import *
from django.utils import timezone
from datetime import timedelta

class PopularPostView(APIView):
    def get(self, request):
        yesterday = timezone.localtime(timezone.now()).date() - timedelta(days=1)
        date = Daily.objects.prefetch_related('popular_post').get(day = yesterday)
        popular_posts = date.popular_post.all()
        posts = [pp.post for pp in popular_posts]
        serializer = PostListSerializer(posts, many = True, context = {'request' : request})
        res = {
            "msg" : "인기글 리스트",
            "data" : serializer.data
        }
        return Response(res, status = status.HTTP_200_OK)