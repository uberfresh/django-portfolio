from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
path('',views.PostList.as_view(),name="post_list"),
path('<slug:slug>',views.Post.as_view(),name="post"),
path('publish/',views.PublishForm.as_view(),name="publish"),
]

