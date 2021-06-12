from django import forms
from django.forms import ModelForm
from .models import PostModal

class PublishForm(ModelForm):
	class Meta:
		model = PostModal
		fields = ['title','content','tag','image']
		


