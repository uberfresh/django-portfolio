from django.contrib import admin
from .models import AboutUser
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
	list_display = ('id','username',)



admin.site.register(AboutUser,AccountAdmin)