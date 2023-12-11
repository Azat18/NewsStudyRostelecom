from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.db import connection, reset_queries
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse_lazy
import json
#URL:    path('search_auto/', views.search_auto, name='search_auto'),
def search_auto(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':# Альтернатива if request.is_ajax()
        q = request.GET.get('term','')
        articles = Article.objects.filter(title__icontains=q)
        results =[]
        for a in articles:
            results.append(a.title)
            data = json.dumps(results)
    else:
        data = 'fail'
        mimetype = 'application/json'
    return HttpResponse(data,mimetype)

def news(request):
   return render(request,'news/news.html')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/news_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_object = self.object
        images = Image.objects.filter(article=current_object)
        context['images'] = images
        return context

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'news/create_article.html'
    fields = ['title','anouncement','text','tags']

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('news_index') #именованная ссылка или абсолютную
    template_name = 'news/delete_article.html'

# class ArticleDeleteView(DeleteView):
#     model = Article
#     success_url = reverse_lazy('news_index') #именованная ссылка или абсолютную
#     template_name = 'news/delete_article.html'

#человек не аутентифицирован - отправляем на страницу другую
# @login_required(login_url="/") Альтернатива ниже
from django.conf import settings
@login_required(login_url=settings.LOGIN_URL)
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None: #проверили что не аноним
                new_article = form.save(commit=False)
                new_article.author = current_user
                new_article.save() #сохраняем в БД
                form.save_m2m() #сохраняем теги
                # form = ArticleForm()
                for img in request.FILES.getlist('image_field'):
                    Image.objects.create(article=new_article, image=img, title=img.name)

                return redirect('news_index')
    else:
        form = ArticleForm()
    return render(request,'news/create_article.html', {'form':form})
def index(request):
    # пример применения пользовательского менеджера
    # articles = Article.published.all()
    # it = Tag.objects.filter(title='IT').first()
    # print('IT использовалось: ',it.tag_count())

    categories = Article.categories  # создали перечень категорий
    author_list = User.objects.all()  # создали перечень авторов

    if request.method == "POST":
        selected_author = int(request.POST.get('author_filter'))
        selected_category = int(request.POST.get('category_filter'))

        if selected_author == 0:  # выбраны все авторы
            articles = Article.objects.all()
        else:
            articles = Article.objects.filter(author=selected_author)
        if selected_category != 0:  # фильтруем найденные по авторам результаты по категориям
            articles = articles.filter(category__icontains=categories[selected_category - 1][0])


    else:  # если страница открывется впервые
        selected_author = 0
        selected_category = 0
        articles = Article.objects.all()

    context = {'articles': articles, 'author_list': author_list, 'selected_author': selected_author,
               'categories': categories, 'selected_category': selected_category}

    return render(request, 'news/news_list.html', context)


    # Работающий вариант
    # articles = Article.objects.all()
    # a = articles.first()
    # categories = Article.categories
    # titles = Article.title
    # dates = Article.date
    # t1 = Article.objects.filter(title__icontains="Новость")
    # # print('Статья: ',a.title, 'Категории: ',a.categories)
    # context = {'articles': articles}
    # print(t1)
    #
    # author_list = User.objects.all()
    # selected = 0
    # if request.method == "POST":
    #     print(request.POST)
    #     selected = int(request.POST.get('author_filter'))
    #     if selected == 0:
    #         articles = Article.objects.all()
    #     else:
    #         articles = Article.objects.filter(author=selected)
    #     print(connection.queries)
    # else:
    #     articles = Article.objects.all()
    # context = {'articles': articles, 'author_list': author_list, 'selected': selected, 'categories': categories,}
    # return render(request, 'news/news_list.html', context)


   # articles = Article.objects.filter(author=request.user.id)
   # print(articles)
   # article = Article.objects.get(author=2)
   # print(article.tags.all())
   # tag = Tag.objects.filter(title='IT').first()
   # tagged_news = Article.objects.filter(tags=tag)
   # print(tagged_news)
   # article = Article.objects.filter(title__contains='дня')
   # article = Article.objects.filter(author=request.user)
   # user_list = User.objects.all()
   # for user in user_list:
   #     print(Article.objects.filter(author=user))
   # # print(user_list)
   # context = {'article':article}
   # return render(request, 'news/contact_page.html', context)


# def detail(request, id):
   # article = Article.objects.filter(id=id).first()
   # print(article, type(article))
 # пример создания новости
# author = User.objects.get(id=request.user.id)
# article = Article(author=author,title='Заголовок1',
#                   anouncement='Анонс', text='текст')
# article.save()
#пример итерирования по объектам QuerySet
    # articles = Article.objects.all()
    # s=''
    # for article in articles:
    #     s+=f'<h1>{article.title}</h1><br>'
    # return HttpResponse(s)
