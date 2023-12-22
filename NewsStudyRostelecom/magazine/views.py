from django.shortcuts import render
from django.http import HttpResponse
from .forms import DemoForm, Demo
from news.models import Article
def index(request):

    return render(request, 'magazine/index.html')

def base(request):

    return render(request, 'magazine/base.html')
def account(request):

    return render(request, 'account/contact_page.html')

# def allnews(request):
#     return render(request, 'allnews/contact_page.html')
def news(request):
    return render(request,'magazine/news.html')

def news_1(request):
    return render(request, 'news_1/contact_page.html')

def demoform(request):
    form = DemoForm()
    if request.method == 'POST':
        new_model = DemoForm(request.POST,request.FILES)
        new_model.save()
    context = {'form':form}
    return render(request, 'magazine/image_Form.html', context)


def showlastmodel(request):
    model = Demo.objects.all().first()
    context = {'model': model}
    return render(request, 'magazine/image_Form.html', context)
# def page404(request):
#     return render(request, 'page404.html')