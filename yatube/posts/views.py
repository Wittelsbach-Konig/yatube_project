from django.shortcuts import HttpResponse

# Главная страница
def index(request):
    return HttpResponse('Главная страница')

#
def group_posts(request, slug):
    return HttpResponse(f'Посты отфильтрованы по группам {slug}')

# Create your views here.
