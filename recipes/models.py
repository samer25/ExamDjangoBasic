from django.db import models


# Create your models here.
class Recipes(models.Model):
    title = models.CharField(max_length=30)
    images_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(max_length=250)
    time = models.IntegerField()
