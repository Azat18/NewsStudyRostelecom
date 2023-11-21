from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.news, name='news_index'),
   path('show/', views.index, name='news_index_1'),
   path('show/<int:id>', views.detail, name='news_detail'),
 ]

