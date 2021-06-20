from django.shortcuts import render
from .forms import ContactForm
from django.views import generic,View
from django.contrib import messages
# Create your views here.


class Contact(generic.CreateView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
   
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["mapbox_access_token"] = "pk.eyJ1IjoidWJlcmZyZXNoIiwiYSI6ImNrZXN2eXM4czA5a2YycnJ1bG52emVudWsifQ.Qf3bryBpqqbw63bntFbVsw"
        return context

    
    def form_valid(self,form):
        form.save()
        messages.success(self.request, 'Your message has been sent successfully.')
        return super().form_valid(form=form)
        
    def form_invalid(self,form):
        response = super().form_invalid(form)
        messages.success(self.request, 'Your message has not been sent!.')
        return response
    


        

    