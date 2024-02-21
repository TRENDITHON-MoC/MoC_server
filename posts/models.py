from django.db import models
from daily.models import Daily

def post_image_path(instance):
    filename = f"{instance.post.pk}/{instance.pk}.jpeg"
    return f'post_images/{filename}'

def thumbnail_image_path(instance):
    filename = f"{instance.post.pk}/thumbnail_{instance.pk}.jpeg"
    return f'post_images/{filename}'

class Hashtag(models.Model):
    tags = models.CharField(max_length = 60, default = "")

    def __str__(self):
        return self.tags

    class Meta:
        db_table = 'hashtag'


class Category(models.Model):
    category_name = models.CharField(max_length = 60, default = "")

    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = 'category'


class Post(models.Model):
    user = models.ForeignKey('accounts.User', null=True, on_delete=models.CASCADE, related_name = 'posts')
    like = models.ManyToManyField('accounts.User', related_name = 'like_post')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name = 'posts')
    daily = models.ForeignKey(Daily, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, null = True)
    like_cnt = models.IntegerField(default=0)
    located = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'post'
    

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "image")
    image = models.ImageField(upload_to = post_image_path)

    class Meta:
        db_table = 'post_image'


class ThumbnailImage(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "thumbnail_image")
    thumbnail_image = models.ImageField(upload_to = thumbnail_image_path)

    class Meta:
        db_table = 'thumbnail_image'