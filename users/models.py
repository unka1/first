from django.db import models
from books.models import books
from albums.models import albums
# Create your models here.
class user_s(models.Model):
    username=models.CharField(unique=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    albums=models.ManyToManyField(albums)
    books=models.ManyToManyField(books)