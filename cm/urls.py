from django.urls import path
from cm import views
from cm.views import *


urlpatterns = [
    path('checkpoint/create-task', CheckpointTaskView.as_view()),
    path('checkpoint/list-task', CheckpointTaskListView.as_view()),
    path('checkpoint/delete-task/<int:pk>', CheckpointTaskDeleteView.as_view()),
    path('checkpoint/detail-task/<int:pk>', CheckpointTaskDetailView.as_view()),
    path('checkpoint/objects/create-policy', CheckpointPolicyCreateView.as_view()),
    path('checkpoint/objects/list-policy', CheckpointPolicyListView.as_view()),
    path('checkpoint/objects/update-policy/<int:pk>', CheckpointPolicyUpdateView.as_view()),
    path('checkpoint/objects/delete-policy/<int:pk>', CheckpointPolicyDeleteView.as_view()),
    path('checkpoint/objects/create-site', CheckpointSiteCreateView.as_view()),
    path('checkpoint/objects/list-site', CheckpointSiteListView.as_view()),
    path('checkpoint/objects/update-site/<int:pk>', CheckpointSiteUpdateView.as_view()),
    path('checkpoint/objects/delete-site/<int:pk>', CheckpointSiteDeleteView.as_view()),
]