from django.urls import path
from cm import views
from cm.views import *


urlpatterns = [
    path('create-task', views.create_task),
    path('objects/create-policy', CheckpointPolicyCreateView.as_view()),
    path('objects/create-site', CheckpointSiteCreateView.as_view())
]
