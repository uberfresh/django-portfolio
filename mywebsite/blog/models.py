from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
import string
import random
from django.urls import reverse
from .unislug import generate_unique_slug
# Create your models here.


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.user',on_delete = models.CASCADE, blank=True, null = True)
	pub_date = models.DateTimeField(blank =True,null = True)
	tag = models.CharField(max_length = 300, blank =True,null= True)
	image = models.ImageField(null=True,blank=True)
	content = models.TextField() 
	slug = models.SlugField(max_length=255,unique = True, null= True)
    
	def save(self):
		self.pub_date = timezone.now()
		if self.slug:
			if slugify(self.title) != self.slug:
				self.slug = generate_unique_slug(Post,self.title)
		else:
			self.slug = generate_unique_slug(Post,self.title)
			
		super().save()
	
	def get_absolute_url(self):
		return reverse('blog:article',kwargs= {'slug':self.slug})
	
	def __str__(self):
		return self.title

    
