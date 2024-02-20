from django.db import models

class Monthly(models.Model):
    start_on = models.DateField()
    finish_on = models.DateField()


class Weekly(models.Model):
    monthly = models.ForeignKey(Monthly, on_delete = models.CASCADE, related_name = 'weekly')
    start_on = models.DateField()
    finish_on = models.DateField()


class Daily(models.Model):
    weekly = models.ForeignKey(Weekly, on_delete = models.CASCADE, related_name = 'daily')
    day = models.DateField()