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


class PopularTestView(APIView):
    serializer_class = DateSerializer
    def post(self, request):
        serializer = DateSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        yesterday = timezone.now().date() - timedelta(days=1)
        date = Daily.objects.prefetch_related('posts').get(day = yesterday)
        posts = date.posts
        
        popular_posts = posts.order_by('-like_cnt')[:1]
        for pp in popular_posts:
            PopularPost(daily = date, post = pp).save()

        res = {
            "data" : PostListSerializer(popular_posts, many = True, context = {'request' : request}).data
        }

        return Response(res)