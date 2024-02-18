from django.db import models

class Post(models.Model):
    user = models.ForeignKey('accounts.User', null=True, on_delete=models.CASCADE, related_name = 'posts')
    # 모델 만든 후에 작성
    # like = models.ForeignKey('Like', on_delete=models.SET_NULL, null=True, blank=True)
    # category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    # daily = models.ForeignKey('Daily', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    hashtags = models.CharField(max_length=255)
    like_cnt = models.IntegerField(default=0)
    located = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title