from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)                       #영화명
    description = models.TextField()                               #영화설명
    poster_url = models.CharField(max_length=300)                  #포스터
    pubDate = models.CharField(max_length=100)                     #개봉일
    director = models.CharField(max_length=100)                    #감독
    def __str__(self):
        return self.title
#--------------------------------------------------------------------------------------------------------
#    audience = models.IntegerField()                               #관중
#    genres = models.ManyToManyField(Genre, related_name='movie')   #장르


