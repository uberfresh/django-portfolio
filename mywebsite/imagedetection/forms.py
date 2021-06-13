from django import forms
from django.forms import ModelForm
from .models import Upload

class ImageForm(ModelForm):
	class Meta:
		model = Upload
		fields = ['image','action']
		


