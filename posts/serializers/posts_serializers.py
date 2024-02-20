from rest_framework import serializers
from ..models import Post, Hashtag
from comments.serializers import CommentSerializer

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class PostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['category', 'title', 'body']


class PostResponseSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()
    # hashtag = serializers.
    class Meta:
        model = Post
        fields = '__all__'

    def get_comments(self, obj):
        comments = obj.comments.filter(parent = None)
        serializer = CommentSerializer(comments, many = True)
        return serializer.data
    
    def get_owner(self, obj):
        request = self.context.get('request')
        if request:
            if request.user == obj.user: return True
        return False
    

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'created_at']