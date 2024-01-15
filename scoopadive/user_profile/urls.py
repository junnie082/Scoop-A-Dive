from django.contrib import admin
from django.urls import path, include

from user_profile.views import view_profile

app_name = 'user_profile'

urlpatterns = [
    path('', view_profile, name="profile"),
]