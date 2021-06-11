from django.contrib import admin
from .models import ContactMessage
# Register your models here.

class ContactMessageAdmin(admin.ModelAdmin):
  fieldsets = [
      ('Info', {'fields':['name','mail']}),
      ('Subject', {'fields':['subject']}),
      ('Message',{'fields':['message']}),
      ('Date',{'fields':['date']}),
  ]
  list_display = ('mail','subject','date')
  list_filter = ['date']
  search_fields = ['subject']
admin.site.register(ContactMessage,ContactMessageAdmin)