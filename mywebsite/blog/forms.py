from django import forms
from django.forms import ModelForm
from .models import Post

class PublishForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title','tag','image','content']
		


