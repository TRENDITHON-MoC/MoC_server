from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import *
from rest_framework.permissions import *
from posts.models import *
from posts.serializers import *
from rest_framework import status
from .permissions import *

# @api_view(['GET', 'POST'])
# def comment_create_view(request, post_id):
#     user = request.user
#     post = get_object_or_404(Post, pk=post_id)

#     if request.method == 'GET':
#         comments = Comment.objects.filter(post=post)
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(post=post)
#             post_response_serializer = PostResponseSerializer(post, context = {'request':request})
#             return Response(post_response_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, post_id):
        post = Post.objects.get(pk = post_id)
        user = request.user

        serializer = CommentRequestSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(user = user, post = post)
        return Response(PostResponseSerializer(post, context = {'request':request}).data, status = status.HTTP_201_CREATED)
    

class CommentDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, comment_id):
        comment = Comment.objects.get(pk = comment_id)
        self.check_object_permissions(request, comment)

        comment.delete()
        return Response({
                "msg": "댓글 삭제 성공"
        }, status=status.HTTP_200_OK)




# @api_view(['DELETE'])
# def comment_delete_view(request, pk):
#     try:
#         comment = Comment.objects.get(pk=pk)
#     except Comment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'DELETE':
#         comment.delete()
#         return Response({
#                 "msg": "댓글 삭제 성공"
#         }, status=status.HTTP_200_OK)