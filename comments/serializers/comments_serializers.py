from rest_framework import serializers
from ..models import Comment

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'body', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many = True)
    class Meta:
        model = Comment
        fields = '__all__' 
        depth = 1


class CommentMyPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'body', 'created_at']