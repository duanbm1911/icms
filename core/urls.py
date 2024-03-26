from django.urls import path
from core import views
from core.views import *


urlpatterns = [
    path('', views.redirect_home_url),
]
