from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import authenticate,login
from django.shortcuts import render,get_object_or_404
from music.models import Album
from music.forms import UserForm


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
	success_url = reverse_lazy('music:index')# Redirect user to 
	#success_url = reverse("music:index")
	#success_url = reverse("music:index")
	#success_url = 'music/index/'
	#def get_success_url(self):
	#	return reverse('music:index')

class UserFormView(View):
	form_class = UserForm
	template_name = "music/registration_form.html"

	#display blank form
	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})

	#process form data
	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_vaild():
			print ("coming")
		user=form.save(commit=False)

		#cleaned (normalized) data
		username=form.cleaned_data['username']
		password=form.cleaned_data['password']
		user.set_password(password)
		user.save()

		user=authenticate(username=username,password=password)

		if user is not None:

			if user.is_active:

				login(request,user)

				return redirect('music:index')

		return render(request,self.template_name,{'form':form})