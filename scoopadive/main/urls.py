from django.urls import path

from . import views
from .views import *

app_name = 'main'

urlpatterns = [
    path('', index),
    path('home/', home),
    # 웹사이트의 첫화면은 index 페이지이다 + URL 이름은 index이다.
    path('', index, name='index'),
    # URL:80/home에 접속하면 home 페이지 + URL 이름은 home 이다
    path('home/', home, name='home'),
    # URL:80/home/숫자로 접속하면 게시글-세부페이지(posting)
    path('home/<int:pk>/', posting, name="posting"),
    path('home/new_log/', new_log, name="new_log"),
    path('home/<int:pk>/remove/', remove_post),
    path('answer/create/<int:logId>', views.answer_create, name="answer_create"),
    path('home/vote/<int:log_id>/', views.log_vote, name="log_vote"),
    path('home/log/modify/view_log_modify/<int:log_id>', views.view_modify_log, name="view_modify_log"),
    path('home/log/modify/<int:log_id>/', views.modify_log, name="modify_log"),
]