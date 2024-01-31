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
from django.urls import path, include

import user_profile
from main import views
from main.views import index, home, posting, new_log, remove_post

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('common/', include('common.urls')),
    path('profile/', include('user_profile.urls')),
    path('', views.index, name='index'),
    path('divepedia/', include('divepedia.urls')),
    path('board/', include('board.urls')),
]

# Serve media files during development

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
