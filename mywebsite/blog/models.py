from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
import string
import random
from django.urls import reverse
from .unislug import generate_unique_slug

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Tag(models.Model):
	tag_name = models.CharField(max_length=50)

	def __str__(self):
		return self.tag_name

class Post(models.Model):
	title = models.CharField(max_length=200)
	tag = models.ForeignKey(Tag,on_delete=models.CASCADE,blank=True,null=True)
	author = models.ForeignKey('auth.user',on_delete = models.CASCADE, blank=True, null = True)
	banner_image = models.ImageField(null=True,blank=True)
	content = RichTextUploadingField(config_name = 'special') 
	slug = models.SlugField(max_length=255, null= True,blank=True)
	pub_date = models.DateTimeField(auto_now_add = True, null=True)
	updated_date = models.DateTimeField(blank =True,null = True)
    
	def save(self):
		self.updated_date = timezone.now()
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

    
