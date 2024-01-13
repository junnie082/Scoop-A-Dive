from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
   path('', index),
   path('home/', home),
   path('home/new_post/', new_post)
]