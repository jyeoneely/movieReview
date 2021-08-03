from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Board(models.Model):
    TYPE_CHOICES = (
        ('한국영화','한국영화'),
        ('외국영화','외국영화'),
        ('자유글','자유글'),
    )
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=20, null=False)
    content_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='----')
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    board_hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.board_hit = self.board_hit + 1
        self.save()