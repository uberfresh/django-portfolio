from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
path('',views.BlogView.as_view(),name="blog"),
path('<slug:slug>',views.ArticleView.as_view(),name="article"),
path('publish_post/',views.PublishPostView.as_view(),name="publish_post"),
path('<str:username>/profile',views.ProfileView.as_view(),name="profile"),
path('<slug:slug>/edit',views.UpdatePostView.as_view(),name="update"),
path('<pk>/delete',views.DeletePostView.as_view(),name="delete"),

]

