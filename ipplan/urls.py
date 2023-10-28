from django.urls import path
from ipplan import views
from ipplan.views import *


urlpatterns = [
    path('create-ip-location', IpLocationCreateView.as_view()),
    path('create-ip-regoin', IpRegoinCreateView.as_view()),
    path('create-ip-subnet', IpSubnetCreateView.as_view()),
    path('list-ip-subnet', IpSubnetListView.as_view()),
    path('request-ip', views.request_ip_form),
    path('dashboard', views.dashboard),
    path('list-ip/<int:pk>', views.list_ip, name='list-ip'),
    path('update-ip-subnet/<int:pk>', IpSubnetUpdateView.as_view()),
    path('list-ip/<int:pk>/delete-ip/<int:id>', IpAddressModelDeleteView.as_view()),
    path('list-ip/<int:pk>/update-ip/<int:id>', IpAddressModelUpdateView.as_view()),
    path('list-ip/<int:pk>/detail-ip/<int:id>', IpAddressModelDetailView.as_view())

]
