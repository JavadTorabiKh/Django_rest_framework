from django.urls import path 
from .views import blog_home

app_name = 'homePage'

urlpatterns = [
    path('', blog_home, name="blog_home"),

] 