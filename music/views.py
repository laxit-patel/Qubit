from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def error_404(request):
    data = {}
    return render(request, 'music/error404.html', data)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Albumm Does Not Exist")
    return render(request, 'music/details.html', {'album': album})
