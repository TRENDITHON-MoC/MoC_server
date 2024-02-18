from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length = 60, default = "")

    def __str__(self):
        return self.category_name