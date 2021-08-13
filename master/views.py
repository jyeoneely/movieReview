from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from movie.models import Movie


def index(request):
    return render(request, 'main.html')


def master(request):
    if request.user.is_superuser:
        return render(request, 'master/index.html')
    else:
        return render(request, 'master/master.html')


def movies(request):
    page = request.GET.get('page', '1')
    movie_list = Movie.objects.order_by('-pub_date', 'title')
    paginator = Paginator(movie_list, 10)
    page_obj = paginator.get_page(page)
    context = {
        'page_obj': page_obj
    }

    return render(request, 'master/movies.html', context)


def users(request):
    return render(request, 'master/users.html')