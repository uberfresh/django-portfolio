from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterForm
# Create your views here.


class Register(generic.CreateView):
	form_class = RegisterForm
	succes_url = reverse_lazy('login') 
	template_name = 'register/register.html'