from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    content_type = models.CharField(max_length=100)
    write_date = models.DateTimeField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
