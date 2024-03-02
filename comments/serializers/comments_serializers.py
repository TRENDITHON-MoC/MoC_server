from rest_framework import serializers
from ..models import Comment

class CommentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['body']


class CommentResponseSerializer(serializers.ModelSerializer):
    like_cnt = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'body', 'created_at', 'like_cnt']

    def get_like_cnt(self, obj):
        likes = obj.like.all().count()
        return likes
