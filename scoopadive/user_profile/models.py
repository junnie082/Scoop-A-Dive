from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    # age = models.IntegerField()
    # diveLicense = models.CharField(max_length=50)
    is_ststMember = models.BooleanField(default=False)
    # studentID = models.IntegerField()
    # major = models.CharField(max_length=50)
    # kisu = models.IntegerField()
    # is_absence = models.BooleanField(default=False)

    class Meta:
        db_table = 'profiles'

    def __str__(self):
        return self.name