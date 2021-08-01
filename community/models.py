from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    author = models.CharField(max_length=20, null=False)
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title