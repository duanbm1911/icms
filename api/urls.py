from django.urls import path
from api import views
from api.views import *


urlpatterns = [
    path('inventory/dashboard-01', views.inventory_dashboard_01),
    path('inventory/dashboard-02', views.inventory_dashboard_02)
]
