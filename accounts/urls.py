from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('user-login/', views.login_page, name='user_login'),
    path('register/', views.register_page, name='user_register'),
    path('log-out/', views.log_out, name='user_log_out')
]