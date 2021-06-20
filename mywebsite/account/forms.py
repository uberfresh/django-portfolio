from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import AboutUser

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['password1'].help_text = None
  
class DateInput(forms.DateInput):
	input_type = 'date'
    	
class AboutForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.fields['profile_pic'].label = "Profile Picture"
		

	class Meta:
		model = AboutUser
		fields = ['birth_day','about_user','profile_pic']

		widgets = {
		'birth_day' : DateInput(attrs={'type':'date'})
		}


    

