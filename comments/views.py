from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Comment
from posts.models import Post
from .serializers import CommentSerializer

@api_view(['GET', 'POST'])
def comment_create_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'GET':
        comments = Comment.objects.filter(parent=None, post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response({
                "msg": "댓글 작성 성공",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def comment_delete_view(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        comment.delete()
        return Response({
                "msg": "댓글 삭제 성공"
        }, status=status.HTTP_200_OK)