from django.urls import path

from board import views

app_name='board'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('view_new_post/', views.view_new_post, name='view_new_post'),
    path('new_post/', views.new_post, name='new_post'),
    path('<int:post_id>/remove', views.remove_post, name='remove_post'),
    path('<int:post_id>/answer_create/', views.answer_create, name='answer_create'),
    path('<int:post_id>/view_modify_post/', views.view_modify_post, name='view_modify_post'),
    path('<int:post_id>/modify_post/', views.modify_post, name='modify_post'),
    path('post/vote/<int:post_id>/', views.post_vote, name='post_vote'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify')
]