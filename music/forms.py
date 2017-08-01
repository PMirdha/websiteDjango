#Default file looked for when creating users

from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		"Specifies information about the above class"
		model = User
		fields = ['username','email','password']

