from django.db import models
from .utils import get_filtered_image
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
from django.urls import reverse
# Create your models here.
ACTION_CHOICES = (
('NO_FILTER','no_filter'),
('COLORIZED','colorized'),
('GRAY_SCALE','grayscale'),


	)

class Upload(models.Model):
	image = models.ImageField()
	action = models.CharField(max_length=50,choices=ACTION_CHOICES)
	updated = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return str(self.id)

	def save(self):
		pil_img = Image.open(self.image)

		cv_image = np.array(pil_img)
		img = get_filtered_image(cv_image,self.action)


		im_pil = Image.fromarray(img)

		buffer = BytesIO()
		im_pil.save(buffer,format='png')
		img_png = buffer.getvalue()

		self.image.save(str(self.image),ContentFile(img_png),save=False)
		super().save()
	def get_absolute_url(self):
		return reverse('imagedetection:imageshow',kwargs= {'pk':self.pk})

