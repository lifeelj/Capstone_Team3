from django.db import models

# Create your models here.

# class Users(models.Model):
#     name = models.CharField(max_length = 200)
#     age = models.IntegerField(default = 0)

#     def __str__(self):
#         return self.name

class Tasks(models.Model):
    age = models.IntegerField(default = 0)
    email = models.CharField(max_length = 200)
    transform = models.CharField(max_length = 200)
    distance = models.FloatField()
    time = models.FloatField()
