from django.urls import path,include
from . import views
app_name = 'account'
urlpatterns = [
path('register/',views.RegisterView.as_view(),name="register"),
path('login/',views.LoginPageView.as_view(),name="login"),
path('about/<str:username>/',views.AboutView.as_view(),name="about"),
path('about/edit/<pk>/',views.AboutUpdateView.as_view(),name="about_update"),

]