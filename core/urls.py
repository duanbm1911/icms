from django.urls import path
from core import views
from django.conf.urls import handler400
from core.views import *


handler400 = views.redirect_home_url

urlpatterns = [
    path('', views.redirect_home_url),
]
