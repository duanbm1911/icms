from django.urls import path
from ipplan import views
from ipplan.views import *


urlpatterns = [
    path('create-location', LocationCreateView.as_view()),
    path('create-region', RegionCreateView.as_view()),
    path('create-subnet', SubnetCreateView.as_view()),
    path('create-multiple-subnet', views.create_multiple_subnet),
    path('request-multiple-ip', views.request_multiple_ip),
    path('delete-subnet/<int:pk>', SubnetDeleteView.as_view()),
    path('list-subnet', SubnetListView.as_view()),
    path('request-ip', views.request_ip_form),
    path('dashboard', views.dashboard),
    path('list-ip/<int:pk>', views.list_ip, name='list-ip'),
    path('update-subnet/<int:pk>', SubnetUpdateView.as_view()),
    path('list-ip/<int:pk>/delete-ip/<int:id>', IpAddressModelDeleteView.as_view()),
    path('list-ip/<int:pk>/update-ip/<int:id>', IpAddressModelUpdateView.as_view()),
    path('list-ip/<int:pk>/detail-ip/<int:id>', IpAddressModelDetailView.as_view())
]
