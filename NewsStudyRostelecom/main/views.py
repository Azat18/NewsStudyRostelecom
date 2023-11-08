from django.shortcuts import render
from django.http import HttpResponse

from .models import News

def index(request):
    value = 100
    n1 = News('Новость 1', 'Текст 1', '05.05.2025')
    n2 = News('Новость 2', 'Текст 2', '10.05.2025')
    l = [n1, n2]
    context = {'title': 'Страница главная',
               'Header1': 'Заголовок страницы',
               'value': value,
               'numbers': l}
    return render(request, 'main/index.html',context)

def about(request):
    return render(request, 'main/about.html')

def content(request):
    return render(request, 'main/content.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def sidebar(request):
    return render(request, 'main/sidebar.html')

