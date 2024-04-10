from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_user, name='register'),
]