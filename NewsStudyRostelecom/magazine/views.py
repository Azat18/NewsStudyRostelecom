from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #return render(request, 'general.html')
    return render(request, 'magazine/index.html')
def account(request):

    return render(request, 'account/index.html')

def news(request):
    return render(request, 'news/index.html')

def news_1(request):
    return render(request, 'news_1/index.html')