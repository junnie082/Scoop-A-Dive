"""
URL configuration for scoopadive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import index, home, posting, new_post, remove_post

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL 이름은 index이다.
    path('', index, name='index'),
    # URL:80/home에 접속하면 home 페이지 + URL 이름은 home 이다
    path('home/', home, name='home'),
    # URL:80/home/숫자로 접속하면 게시글-세부페이지(posting)
    path('home/<int:pk>/', posting, name="posting"),
    path('home/new_post/', new_post, name="new_post"),
    path('home/<int:pk>/remove/', remove_post),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)