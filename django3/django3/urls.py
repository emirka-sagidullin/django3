"""django3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from djangopon import views

top_info = [
    path('', views.top),
    path('likes/<int:id>/', views.topLikes),
    path('comments/<int:id>/', views.topComments),
]

new_info = [
    path('', views.new),
    path('likes/<int:id>/', views.newLikes),
    path('comments/<int:id>/', views.newComments),
]

posts_patterns = [
    path('', views.posts),
    path('new/', include(new_info)),
    path('top/', include(top_info)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include(posts_patterns)),
    path('', views.main),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('access/', views.access),
    path('json/', views.json),
    path('get/', views.get),
    path('set/', views.set)
]

