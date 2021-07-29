from django.db import models
# from user import User

# Create your models here.

class Review(models.Model) :
    movie = models.CharField(max_length=50)              # ForeignKey(Movie, on_delete=models.CASCADE)
    star = models.PositiveIntegerField()                 # PositiveInteger vs Integer
    writer = models.CharField(max_length=10)               # ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)           여유되면 추가
    content = models.TextField()
    like_review = models.IntegerField(default=0)
    unlike_review = models.IntegerField(default=0)
    share_ulr = models.URLField()                             # URL 처리 서치

    def __str__(self):
        return self.movie + " Review"