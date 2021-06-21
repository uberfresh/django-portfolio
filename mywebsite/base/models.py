from django.db import models

# Create your models here.


class Projects(models.Model):
	title = models.CharField(max_length=50)
	body = models.TextField()
	image = models.ImageField(null=True,blank=True)
	link = models.CharField(max_length=200)
	pub_date = models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return self.title