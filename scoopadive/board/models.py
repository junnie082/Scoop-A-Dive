from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    postName = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    date = models.DateTimeField()
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    voter = models.ManyToManyField(User)  # 추천인 추가

    class Meta:
        db_table = 'Post'

    def __str__(self):
        return self.postName


class Answer4Post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    date = models.DateTimeField()
    voter = models.ManyToManyField(User) # 추천인 추가

    class Meta:
        db_table = 'Answer4Post'

    def __str__(self):
        return self.content