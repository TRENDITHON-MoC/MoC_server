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
    """
    게시글 생성 뷰
    """
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
                "data" : PostResponseSerializer(post, context={'request': request}).data
            }
            return Response(res, status = status.HTTP_201_CREATED)
        res = {
            "msg" : "올바르지 않은 양식",
            "data" : serializer.errors
        }
        return Response(res, status = status.HTTP_400_BAD_REQUEST)
    

class PostImageUploadView(APIView):
    """
    이미지 업로드 뷰
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    def post(self, request, post_id):
        post = Post.objects.get(pk = post_id)
        self.check_object_permissions(request, post)

        image_serializer = ImageRequestSerializer(data = request.data)
        if not image_serializer.is_valid():
            return Response(image_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        image_list = image_serializer.validated_data
        try:
            for image in image_list:
                PostImage(image = image, post = post).save()
            post_serializer = PostResponseSerializer(post, context={'request': request})
            return Response(post_serializer.data, status = status.HTTP_201_CREATED)
        except:
            res = {
                "msg" : "이미지 형식은 올바르나 업로드 실패"
            }
            return Response(res, status = status.HTTP_400_BAD_REQUEST)
        