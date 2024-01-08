from django.urls import path
from .views import article_list, article_detail, article_create
from . import views

app_name = 'blog'
urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('articles/detail/<int:article_id>/', views.article_detail,  name='article_detail'),
    path('articles/create/', views.article_create, name='article_create'),
    path('articles/edit/<int:article_id>', views.article_edit, name='article_edit'),
    path('articles/delete/<int:article_id>', views.article_delete, name='article_delete'),
]