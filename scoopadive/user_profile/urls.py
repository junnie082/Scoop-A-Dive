from django.contrib import admin
from django.urls import path, include

from user_profile.views import view_profile, modify_profile

app_name = 'user_profile'

urlpatterns = [
    path('', view_profile, name="profile"),
    path('modify_profile/', modify_profile, name="modify_profile"),
]