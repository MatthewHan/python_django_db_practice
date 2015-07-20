from django.db import models
from django.utils import timezone
# Create your models here.
class Interest(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(default=timezone.now, blank = True)
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    age = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(default=timezone.now, blank = True)
    occupation = models.CharField(max_length = 255)
    interests = models.ManyToManyField(Interest)