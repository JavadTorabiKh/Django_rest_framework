from django.urls import path 
from .views import blog_page, blog_home, pade_detail

app_name = 'blog'

urlpatterns = [
    path('', blog_home),
    path('page/', blog_page),
    path('page/version/<int:page_id>/',pade_detail, name="pade_detail"),
] 