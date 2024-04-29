from django.urls import path, include
from . import views

urlpatterns = [
    path('users/', views.get_users, name='get_users'),
    path('users/<int:todoId>/', views.get_user, name='get_user'),

    path('cbv/users/', views.get_users, name='get_users'),
    path('cbv/users/<int:todoId>/', views.get_user, name='get_user'),

]
