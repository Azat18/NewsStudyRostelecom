from django.contrib import admin
from django.urls import path


from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('content/', views.content, name = 'content'),
    path('sidebar/', views.sidebar),
    path('main/', views.main),
    path('menu/', views.menu),
]


