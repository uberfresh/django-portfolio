from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import AboutUser
from .forms import RegisterForm
# Create your views here.
def register(request):
    form = RegisterForm
    context = {'form':form}
    if request.method == "POST":
    	form = RegisterForm(request.POST)
    	if form.is_valid():
    		form.save()	
    		user = User.objects.get(username = form.cleaned_data['username'])
    		m = AboutUser(username=user)
    	    
    		m.save()
#3Bth19995.
    		messages.success(request, 'Account was created for ' + form.cleaned_data.get('username'))
    		
    		return redirect('/account/login')

    	else:
    		return render(request,'account/register.html',context)

    return render(request,'account/register.html',context)

def loginpage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password =  request.POST.get('password')
		user = authenticate(request,username =username ,password = password)
		
		if user is not None:
			login(request,user)
			return redirect('/blog/')
		else:
			messages.info(request,'Username OR password is incorrect!')
		



	context = {}
	return render(request,'account/login.html',context)