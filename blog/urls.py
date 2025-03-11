from django.shortcuts import render
from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts')]