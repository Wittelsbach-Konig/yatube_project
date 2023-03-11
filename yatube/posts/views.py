from django.shortcuts import HttpResponse
from django.shortcuts import render


# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Фильтрация по группам
def group_posts(request, slug):
    return HttpResponse(f'Посты отфильтрованы по группам {slug}')

# Create your views here.
