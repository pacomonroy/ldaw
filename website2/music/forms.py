from django.forms import ModelForm
from .models import Album, Song


class AlbumForm(ModelForm):
	class Meta:
		model = Album
		fields = ['artist', 'album_title', 'genre', 'album_art']
		
class SongForm(ModelForm):
	class Meta:
		model = Song
		fields = ['album', 'file_type', 'song_title', 'is_fav']