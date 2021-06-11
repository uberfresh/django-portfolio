from django.db import models
from django.utils import timezone
from django.utils.text import slugify

import string
import random
# Create your models here.


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class PostModal(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	author = models.ForeignKey('auth.user',on_delete = models.CASCADE, blank=True, null = True)
	pub_date = models.DateTimeField(blank =True,null = True)
	tag = models.CharField(max_length = 300, blank =True,null= True)
	image = models.ImageField(null=True,blank=True)
	slug = models.SlugField(max_length=255,unique = True, null= True)

	def publish(self):
		self.pub_date = timezone.now()
		if not self.slug:
			self.slug = slugify(rand_slug() + "-" + self.title)

		self.save()
	   
	def __str__(self):
		return self.title

    
