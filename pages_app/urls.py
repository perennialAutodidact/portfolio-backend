from django.urls import path

from . import views

app_name='pages_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('home-videos/', views.home_videos, name='home_videos'),
]