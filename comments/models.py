from django.db import models

class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    # 모델 만든 후에 작성
    # like = models.ForeignKey('Like', on_delete=models.SET_NULL, null=True, blank=True)
    # daily = models.ForeignKey('Daily', on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)