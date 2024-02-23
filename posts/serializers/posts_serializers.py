from rest_framework import serializers
from ..models import *
from comments.serializers import CommentSerializer

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'


class PostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body']


class ImageRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']


class ImageResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']

    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url)
        return None


class PostResponseSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    hashtags = serializers.SerializerMethodField()
    image = ImageResponseSerializer(many = True)
    class Meta:
        model = Post
        fields = '__all__'

    def get_comments(self, obj):
        comments = obj.comments.all()
        serializer = CommentSerializer(comments, many = True)
        return serializer.data

    def get_hashtags(self, obj):
        tags = obj.hashtags.all()
        serializer = HashtagSerializer(tags, many = True)
        return serializer.data
    

class PostListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'thumbnail', 'created_at']

    def get_thumbnail(self, obj):
        request = self.context.get('request')
        first_image = obj.image.all().order_by('id').first()
        if not first_image:
            return None
        serializer = ImageResponseSerializer(first_image, context={'request': request})
        return serializer.data