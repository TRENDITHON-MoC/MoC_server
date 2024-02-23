from django.db import models
from .daily_models import Daily

class PopularPost(models.Model):
    daily = models.ForeignKey(Daily, on_delete = models.CASCADE, related_name = 'pupular_post')
    post = models.ForeignKey('posts.Post', on_delete = models.CASCADE, related_name = 'pupular_post')