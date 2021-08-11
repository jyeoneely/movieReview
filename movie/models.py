from django.db import models
from django.utils import timezone
from account.models import User


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)  # 영화명
    description = models.TextField()  # 영화설명
    poster = models.ImageField(upload_to='media/', blank=True, null=True)  # 포스터
    pub_date = models.DateField()  # 개봉일
    director = models.CharField(max_length=100)  # 감독
    create_date = models.DateTimeField(default=timezone.now)
    like_user = models.ManyToManyField(User, related_name='like_movie')

    def __str__(self):
        return self.title
# --------------------------------------------------------------------------------------------------------
#    audience = models.IntegerField()                               #관중
#    genres = models.ManyToManyField(Genre, related_name='movie')   #장르
