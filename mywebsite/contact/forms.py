from django import forms
from django.forms import ModelForm
from contact.models import ContactMessage

class ContactForm(ModelForm):
	class Meta:
		model = ContactMessage
		fields = ['name','mail','subject','message']
		widgets ={'message':forms.Textarea(attrs={'rows':4, 'cols':15}),}

	  


