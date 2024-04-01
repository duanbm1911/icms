from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('account/logout', views.logout, name='logout'),
    path('account/change_password', views.change_password, name='change_password'),
]