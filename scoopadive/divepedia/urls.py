from django.urls import path
from divepedia import views

app_name = 'divepedia'

urlpatterns = [
    path('', views.index, name='index'),
    path('jeju_dive_shops/', views.view_jeju_shops, name='view_jeju_shops')
]