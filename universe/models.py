from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    rate = models.FloatField()
    created_date = models.DateTimeField(auto_created=True)
    modified_date = models.DateTimeField(auto_now=True)
