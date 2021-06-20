from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('contact/',include('contact.urls')),
    path('blog/',include('blog.urls')),
    path('account/',include('account.urls')),
    path('', include('django.contrib.auth.urls')),

    path('ckeditor',include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
