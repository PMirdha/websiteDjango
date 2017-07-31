from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Album


class IndexView(generic.ListView):
	template_name="music/index.html"
	context_object_name = "all_albums" #Default is object_list

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	"Detail view takes primary key as input so change it in url.py"
	template_name="music/detail.html"
	model=Album
		
class AlbumCreate(CreateView):
	#Template not specified as default sees for modelname_form.html
	model = Album
	fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
	#Template not specified as default sees for modelname_form.html
	model = Album
	fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
	model = Album
	#success_url = reverse_lazy("music:index")# Redirect user to 
	#success_url = reverse("music:index")
	#success_url = reverse("music:index")
	#success_url = 'music/index/'
	def get_success_url(self):
		return reverse('music:index')