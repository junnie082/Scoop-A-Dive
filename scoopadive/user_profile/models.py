from django.contrib.auth.models import User
from django.db import models

from main.models import Log


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    birthday = models.DateField(null=True)
    age = models.IntegerField(null=True)
    diveLicense = models.CharField(null=True, max_length=50)
    is_ststMember = models.BooleanField(default=False)
    studentID = models.IntegerField(null=True)
    major = models.CharField(null=True, max_length=50)
    kisu = models.IntegerField(null=True)
    is_absence = models.BooleanField(null=True, default=False)
    introduction = models.TextField(null=True)
    image = models.ImageField(blank=True, null=True)
    loglist = models.ForeignKey(Log, null=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Profiles'

    def __str__(self):
        return self.name