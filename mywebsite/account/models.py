from django.db import models

# Create your models here.
class AboutUser(models.Model):
	username = models.ForeignKey('auth.user',on_delete = models.CASCADE, blank=True, null = True)
	about_user = models.TextField(max_length=250,blank=True,null=True)
