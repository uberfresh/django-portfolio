from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class ContactMessage(models.Model):
    mail = models.EmailField(max_length=254)
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
	
    def __str__(self):
        return self.mail
