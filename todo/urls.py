from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", views.TodosviewSetApiView)
router_user = DefaultRouter()
router_user.register("", views.UsersViewSetApiView)


urlpatterns = [
    path('', views.get_users, name='get_users'),
    path('<int:todoId>/', views.get_user, name='get_user'),

    path('cbv/', views.TodosListApiView.as_view(), name='get_users'),
    path('cbv/<int:todoId>/',
         views.TodosDetailApiView.as_view(), name='get_user'),
    path('mixin/', views.TodosMixinListApi.as_view(), name='get_users'),
    path('mixin/<int:pk>/',
         views.TodosMixinDetailApi.as_view(), name='get_users'),
    path('generics/',
         views.TodosGenericsListApiView.as_view(), name='get_users'),
    path('generics/<int:pk>/',
         views.TodosGenericsDetailApiView.as_view(), name='get_users'),

    path('viewset/', include(router.urls)),
    path('user/', include(router_user.urls)),


]
