from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.
def register(request):
    form = RegisterForm()
    context = {'form':form}
    if request.method == "POST":
    	form = RegisterForm(request.POST)
    	if form.is_valid():
    		form.save()
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