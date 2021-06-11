from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views import generic,View
# Create your views here.


class Contact(View):
    form_class = ContactForm()
    initial = {'key': 'value'}
    template_name = 'contact/contact.html'
    context = { 
        "mapbox_access_token" : "pk.eyJ1IjoidWJlcmZyZXNoIiwiYSI6ImNrZXN2eXM4czA5a2YycnJ1bG52emVudWsifQ.Qf3bryBpqqbw63bntFbVsw", 

        }
    def get(self,request):
        form = ContactForm(initial=self.initial)
        self.context["form"] = form
        return render(request,self.template_name,self.context)
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid(): 
            form.save()
            self.context["posted"] = "1"
        self.context["form"] = form        
        return render(request,self.template_name,self.context) 

    

    