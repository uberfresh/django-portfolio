from django.urls import path
from . import views


app_name = 'base'
urlpatterns = [
path('',views.Index.as_view(),name="index"),
path('projects/',views.ProjectsView.as_view(),name="projects"),
]