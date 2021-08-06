from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Review(models.Model) :
    movie = models.CharField(max_length=50)              # ForeignKey(Movie, on_delete=models.CASCADE)
    star = models.PositiveIntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)     # ForeignKey(User, on_delete=models.CASCADE, related_name='author_review')
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(null=True, blank=True)  # auto_now=True
    like_review = models.IntegerField(default=0)
    unlike_review = models.IntegerField(default=0)              # models.ManyToManyField(User, related_name='voter_question')
    # share_ulr = models.URLField("http://127.0.0.1:8000/review/pk")
    review_hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.movie + " Review"

    @property
    def update_counter(self):
        self.review_hit = self.review_hit +1
        self.save()