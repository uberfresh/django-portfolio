from django.db import models
from django.urls import reverse
# Create your models here.
class AboutUser(models.Model):
	username = models.OneToOneField('auth.user',on_delete = models.CASCADE, blank=True, null = True)
	birth_day = models.DateField(null=True)
	about_user = models.TextField(max_length=250,blank=True,null=True)
	profile_pic = models.ImageField(null=True,blank=True)
	


	def get_absolute_url(self):
	    return reverse('blog:blog')


	
