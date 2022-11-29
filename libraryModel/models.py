from email.policy import default
from secrets import choice
from django.db import models

# Create your models here.
choices = (('Fantasy','Fantasy'),('Literary','Literary'),('Mystery','Mystery'),('Science Fiction','Science Fiction'),('Thriller','Thriller'))

class Ebooks(models.Model):
    title = models.TextField()
    author = models.TextField()
    genre = models.CharField(max_length = 15,choices= choices )
    review = models.IntegerField()
    favorite = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return self.Title