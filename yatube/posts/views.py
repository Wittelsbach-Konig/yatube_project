# from django.shortcuts import HttpResponse
from django.shortcuts import render


# Главная страница
def index(request):
    template = 'posts/index.html'
    context = {
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


# Фильтрация по группам
def group_posts(request):
    template = 'posts/group_list.html'
    context = {
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)

# Create your views here.
