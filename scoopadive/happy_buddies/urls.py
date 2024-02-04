from django.urls import path

from happy_buddies import views

app_name = 'happy_buddies'

urlpatterns = [
    path('', views.index, name='happy_buddies'),
]