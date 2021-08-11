from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.views import generic

"""
def index(request):
    page = request.GET.get('page', '1')
    movie_list = Movie.objects.order_by('-pub_date', 'title')
    paginator = Paginator(movie_list, 10)
    page_obj = paginator.get_page(page)

    context = {
        'movie_list': page_obj,
    }
    return render(request, 'movie/movie_list.html', context)
"""


class IndexView(generic.ListView):
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range
        return context

    def get_queryset(self):
        return Movie.objects.order_by("-pub_date", "-create_date", "title")


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST,
                         request.FILES)  # subject = request.POST['subject']  content=request.POST['content']
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie:index')
    else:
        form = MovieForm()
    context = {'form': form}
    return render(request, 'movie/form.html', context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {'movie': movie}
    return render(request, 'movie/detail.html', context)


def modify(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie:detail', movie_id=movie.id)
    else:
        form = MovieForm(instance=movie)
    context = {'form': form}
    return render(request, 'movie/form.html', context)


def delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return redirect('movie:index')
