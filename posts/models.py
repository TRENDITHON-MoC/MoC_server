from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    hashtags = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    like_cnt = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)