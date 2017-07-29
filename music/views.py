from django.views import generic
from models import Album


class IndexView(generic.ListView):
	template_name="music/index.html"
	context_object_name = "all_albums" #Default is object_list

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	"Detail view takes primary key as input so change it in url.py"
	template_name="music/detail.html"
	model=Album
		


		