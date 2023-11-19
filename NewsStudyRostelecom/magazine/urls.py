from django.contrib import admin
from django.urls import path


from . import views
urlpatterns = [
    path('demoform/', views.demoform),
    path('showlastimage/',views.showlastmodel),
    path('', views.index, name = 'demo'),
    path('account/', views.account, name = 'account'),
    path('news/', views.news, name = 'news'),
    path('news_1/', views.news_1, name = 'news_1'),
    ]


