from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Log(models.Model):
    diver = models.CharField(null=True, max_length=20)
    logName = models.CharField(max_length=20)
    diveNo = models.IntegerField()
    date = models.DateField()
    location = models.CharField(max_length=50)
    buddy = models.CharField(null=True, max_length=20)
    timeIn = models.TimeField()
    timeOut = models.TimeField()
    weight = models.IntegerField()
    barStart = models.FloatField()
    barEnd = models.FloatField()
    maxDepth = models.FloatField()
    minDepth = models.FloatField()
    temperature = models.FloatField()
    comments = models.TextField()
    images = models.ImageField(blank=True, null=True)

    class Meta:
        db_table = 'Logs'
    def __str__(self):
        return self.logName


class Answer(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # create_date = models.DateTimeField()

    class Meta:
        db_table = 'Answers'