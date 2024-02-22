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
    def post(self, request, category_id):
        user = request.user
        category = Category.objects.get(pk = category_id)
        daily = Daily.objects.last()

        hastags_word_list = request.data.get('hashtags')
        print(hastags_word_list)
        hashtags_instance_list = []
        for h in hastags_word_list:
            hashtags_instance_list.append(create_hashtag(h))

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
        image_list = request.data.getlist('images')
        for image in image_list:
            post_image = PostImage(post = post, image = image)
            post_image.save()
        post_serializer = PostResponseSerializer(post, context={'request': request})
        return Response(post_serializer.data, status = status.HTTP_201_CREATED)
        

class PostUpdateView(APIView):
    """
    게시글 업데이트 뷰
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    def put(self, request, post_id):
        post = Post.objects.get(pk = post_id)
        self.check_object_permissions(request, post)

        added_hastags_list = request.data.get('added_hashtags')
        removed_hastags_list = request.data.get('removed_hashtags')
        removed_images_list = request.data.get('removed_images')

        serializer = PostRequestSerializer(post, data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        
        hashtags_instance_list = []
        for h in added_hastags_list:
            hashtags_instance_list.append(create_hashtag(h))

        for ah in hashtags_instance_list:
            post.hashtags.add(ah)
        
        for rh in removed_hastags_list:
            post.hashtags.remove(Hashtag.objects.get(pk = rh))
        
        for ri in removed_images_list:
            PostImage.objects.get(pk = ri).delete()

        post.save()

        res = {
            "msg" : "게시글 수정 성공",
            "data" : PostResponseSerializer(post, context = {'request':request}).data
        }

        return Response(res, status = status.HTTP_200_OK)
    

class PostDeleteView(APIView):
    """
    게시글 삭제 뷰
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    def delete(self, request, post_id):
        post = Post.objects.get(pk = post_id)
        self.check_object_permissions(request, post)
        post.delete()

        res = {
            "msg":"게시글 삭제 성공"
        }
        return Response(res, status=status.HTTP_204_NO_CONTENT)
    

class PostDetailView(APIView):
    """
    게시글 디테일 뷰
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, post_id):
        post = Post.objects.get(pk = post_id)

        data = PostResponseSerializer(post, context = {'request':request}).data
        res = {
            "msg" : "게시글 세부사항 반환 성공",
            "data" : data
        }
        return Response(res, status=status.HTTP_200_OK)