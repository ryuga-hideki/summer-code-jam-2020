"""rss_it URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from .views import create_post_form
from syndication_app.views import post_view, comment_add

urlpatterns = [
    path('', include('syndication_app.urls')),
    path('rss/', include('syndication_app.urls')),
    path('admin/', admin.site.urls),
    path('post/<str:community>', create_post_form),
    path('posts/<int:post_id>', post_view),
    path('posts/<int:post_id>/comment', comment_add),
    path('chat/', include('irc_chat.urls'))
]
