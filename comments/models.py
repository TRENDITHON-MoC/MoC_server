from django.db import models
from daily.models import Daily

class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('accounts.User', on_delete = models.CASCADE, related_name = 'comments')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='replies')
    # 모델 만든 후에 작성
    like = models.ManyToManyField('accounts.User', related_name = 'like_comment')
    daily = models.ForeignKey(Daily, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    
    class Meta:
        db_table = 'comment'