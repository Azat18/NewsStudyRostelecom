from django.shortcuts import render
from django.http import HttpResponse
from .forms import DemoForm, Demo
def index(request):
    #return render(request, 'general.html')
    return render(request, 'magazine/index.html')
def account(request):

    return render(request, 'account/index.html')

def news(request):
    return render(request, 'news/index.html')

def news_1(request):
    return render(request, 'news_1/index.html')


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