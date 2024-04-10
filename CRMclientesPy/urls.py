from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>/', views.customer_page, name='record'),
    path('add_record/', views.add_record, name='add'),
    path('edit_record/<int:pk>/', views.edit_record, name='edit'),
    path('delete_record/<int:pk>/', views.delete_customer_page, name='delete'),
]