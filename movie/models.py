from django.db import models


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)  # 영화명
    description = models.TextField()  # 영화설명
    poster = models.ImageField(upload_to='media/', blank=True, null=True)  # 포스터
    pub_date = models.DateField()  # 개봉일
    director = models.CharField(max_length=100)  # 감독

    # models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)                    #감독
    def __str__(self):
        return self.title
# --------------------------------------------------------------------------------------------------------
#    audience = models.IntegerField()                               #관중
#    genres = models.ManyToManyField(Genre, related_name='movie')   #장르
