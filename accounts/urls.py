from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('logout/', views.logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
]