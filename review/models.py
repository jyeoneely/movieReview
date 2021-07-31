from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse


class Review(models.Model) :
    movie = models.CharField(max_length=50)              # ForeignKey(Movie, on_delete=models.CASCADE)
    star = models.PositiveIntegerField()                 # PositiveInteger vs Integer (0~5 제한 필요)
    author = models.CharField(max_length=10)             # ForeignKey(User, on_delete=models.CASCADE, related_name='author_review')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    like_review = models.IntegerField(default=0)
    unlike_review = models.IntegerField(default=0)              # models.ManyToManyField(User, related_name='voter_question')
    # share_ulr = models.URLField("http://127.0.0.1:8000/review/pk")    # 템플릿 구현 방향으로 논의예정
    review_hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.movie + " Review"

    @property
    def update_counter(self):
        self.review_hit = self.review_hit +1
        self.save()