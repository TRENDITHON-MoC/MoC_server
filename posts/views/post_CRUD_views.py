from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers.posts_serializers import *
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import *
from ..permissions import IsOwnerOrReadOnly


def create_hashtag(word):
    instance = Hashtag.objects.filter(tags = word).first()
    if not instance:
        hashtag = Hashtag.objects.create(tags = word)
        return hashtag
    return instance


class PostCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, category_name):
        user = request.user
        category = Category.objects.get(category_name = category_name)
        daily = Daily.objects.last()

        hastags_word_list = request.data.getlist('hashtags')
        print(hastags_word_list)
        hashtags_instance_list = []
        for h in hastags_word_list:
            hashtags_instance_list.append(create_hashtag(h))
        print(hashtags_instance_list)

        serializer = PostRequestSerializer(data = request.data)
        if serializer.is_valid():
            post = serializer.save(user = user, category = category, daily = daily)
            for hashtag in hashtags_instance_list:
                post.hashtags.add(hashtag)
            post.save()
            res = {
                "msg" : "게시글 작성 성공",
                "data" : PostResponseSerializer(post).data
            }
            return Response(res, status = status.HTTP_201_CREATED)
        res = {
            "msg" : "올바르지 않은 양식",
            "data" : serializer.errors
        }
        return Response(res, status = status.HTTP_400_BAD_REQUEST)