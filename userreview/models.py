from django.db import models

# Create your models here.


class Review(models.Model):
    username = models.CharField(max_length=40)
    user_review = models.TextField()
    ratings = models.IntegerField()
