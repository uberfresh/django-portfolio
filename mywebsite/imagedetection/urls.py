from django.urls import path
from . import views

app_name = 'imagedetection'
urlpatterns = [
path('',views.Image.as_view(),name="upload"),
path('imageshow/<int:pk>',views.ImageShow.as_view(),name="imageshow")
]

