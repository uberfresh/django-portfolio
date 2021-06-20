from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import AboutUser
from django.contrib import messages

from .forms import RegisterForm,AboutForm
from django.views import generic
from django.contrib.auth.views import LoginView
# Create your views here.

class RegisterView(generic.CreateView):
	form_class = RegisterForm
	template_name = "account/register.html"

	def form_valid(self,form):
		form.save()
		messages.success(self.request,'Account was created for:<strong> '+ form.cleaned_data.get('username') + "</strong>") 
		return redirect('/account/login')


class LoginPageView(LoginView):
	template_name = 'account/login.html'
     
	def form_valid(self,form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(self.request,username = username,password= password)

		if user is not None:
			login(self.request,user)
			return redirect('/blog/')
		else:
			return redirect('/account/login')
		
	def form_invalid(self,form):
			response = super().form_invalid(form)
			messages.info(self.request, 'Your username or password is incorrect!.')
			return response

	

class AboutView(generic.CreateView):
	model= AboutUser
	template_name = 'account/about.html'
	form_class = AboutForm

	def form_valid(self,form):		
		form.save()
		obj = form.save()
		obj.username = self.request.user
		obj.save()
		return super().form_valid(form)



class AboutUpdateView(generic.UpdateView):
	model = AboutUser
	form_class = AboutForm
	template_name = 'account/about.html'


	

	
