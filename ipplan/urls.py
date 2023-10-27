from django.urls import path
from ipplan import views
from ipplan.views import *


urlpatterns = [
    path('create-ip-location', IpLocationCreateView.as_view()),
    path('create-ip-regoin', IpRegoinCreateView.as_view()),
    path('create-ip-subnet', IpSubnetCreateView.as_view()),
    path('list-ip-subnet', IpSubnetListView.as_view()),
    path('request-ip', views.request_ip_form),
    path('dashboard', views.dashboard)
]
