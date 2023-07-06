from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies
from .forms import MovieForm


# Create your views here.
def index(request):
    movie = Movies.objects.all()
    return render(request, 'index.html', {'mov': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')


def details(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    return render(request, 'details.html', {'mov': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        movie = Movies(name=name, year=year, desc=desc, image=image)
        movie.save()
    return render(request, 'add.html')


def update(request, id):
    movie = Movies.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'movie': movie})
