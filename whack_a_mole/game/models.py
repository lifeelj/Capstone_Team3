from django.db import models

# Create your models here.


class Result(models.Model):
    age = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
