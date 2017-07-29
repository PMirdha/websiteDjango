from django.http import Http404
from django.http import HttpResponse
#from django.template import loader 
from django.shortcuts import render,get_object_or_404
from .models import Album,Song

def index(request):
	all_albums=Album.objects.all();
	#all_albums=Album.objects.filter(id=10);
	#template=loader.get_template('music/index.html');        #Shortcut used see return render()
	#return HttpResponse(template.render(context,request))
	context={'all_albums': all_albums,}
	#http=""
	#for album in all_albums:
	#	url = str(album.id)+'/'
	#	http+='<a href="'+url+'">'+album.album_title+"&nbsp;"+album.artist+'</a><br>'
	return render(request,'music/index.html',context)

def detail(request,album_id):
	# Shortcut is mentioned below
	#try:
	#	album=Album.objects.get(pk=album_id)
		#songs=album.song_set.all();
	#except Album.DoesNotExist:
	#	raise Http404("Album Does not exist")
	album=get_object_or_404(Album,pk=album_id)
	return render(request,'music/detail.html',{'album': album})

def favorite(request,album_id):
	album=get_object_or_404(Album,pk=album_id)
	try:
		selected_song=album.song_set.get(pk=request.POST['song'])
	except	(KeyError,Song.DoesNotExist):
		return render(request,'music/detail.html',{
			'album': album,
			'error_message':"You did not select a valid song"
			})
	else:
		selected_song.is_favorite='true'
		selected_song.save()
		return render(request,'music/detail.html',{'album': album})

