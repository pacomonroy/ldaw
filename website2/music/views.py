from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Album, Song
from .forms import AlbumForm, SongForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        raise
        # return render(request, 'music/detail.html', {
        #     'album': album,
        #     'error_message': "No song selected"
        # })

    else:
        selected_song.is_fav = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
from django.shortcuts import render


def AlbumCreate(request):
    context = { }
    
    if request.method == "POST":
        
        # Get the form through POST
        new_album_form = AlbumForm(request.POST)
        
        # Validate form data
        if new_album_form.is_valid():
            # Get form variables
            # Create donor object
            context['album'] = Album.objects.create(**new_album_form.cleaned_data)
            return index(request)
        
        context['form'] = new_album_form
        return render(request, 'music/album_form_create.html', context)
    
    else:
        new_album_form = AlbumForm()
    
    context['form'] = new_album_form
    
    return render(request, 'music/album_form_create.html', context)
