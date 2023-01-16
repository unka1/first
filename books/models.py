from django.db import models

class books(models.Model):
    bookname=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
