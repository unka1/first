from django.db import models

# Create your models here.
class albums(models.Model):
    album=models.CharField(max_length=200)
    artist=models.CharField(max_length=100)
