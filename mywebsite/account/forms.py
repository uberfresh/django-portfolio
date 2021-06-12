from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']
		
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['password1'].help_text = None
    	
    	
    		
        
    

