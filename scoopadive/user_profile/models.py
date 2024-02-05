from django.contrib.auth.models import User
from django.db import models

from main.models import Log


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(null=True, blank=True, max_length=20)
    birthday = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    diveLicense = models.CharField(null=True, blank=True, max_length=50)
    is_ststMember = models.BooleanField(null=True, blank=True, default=False)
    studentID = models.IntegerField(null=True, blank=True)
    major = models.CharField(null=True, blank=True,max_length=50)
    kisu = models.IntegerField(null=True, blank=True)
    is_absence = models.BooleanField(null=True, blank=True, default=False)
    introduction = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    loglist = models.ForeignKey(Log, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Profiles'

    def __str__(self):
        return self.name
