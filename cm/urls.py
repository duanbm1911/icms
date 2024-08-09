from django.urls import path
from cm import views
from cm.views import *


urlpatterns = [
    path('checkpoint/create-rule', CheckpointRuleView.as_view()),
    path('checkpoint/list-rule', CheckpointRuleListView.as_view()),
    path('checkpoint/delete-rule/<int:pk>', CheckpointRuleDeleteView.as_view()),
    path('checkpoint/detail-rule/<int:pk>', CheckpointRuleDetailView.as_view()),
    path('checkpoint/update-rule/<int:pk>', CheckpointRuleUpdateView.as_view()),
    path('checkpoint/objects/create-policy', CheckpointPolicyCreateView.as_view()),
    path('checkpoint/objects/list-policy', CheckpointPolicyListView.as_view()),
    path('checkpoint/objects/update-policy/<int:pk>', CheckpointPolicyUpdateView.as_view()),
    path('checkpoint/objects/delete-policy/<int:pk>', CheckpointPolicyDeleteView.as_view()),
    path('checkpoint/objects/create-site', CheckpointSiteCreateView.as_view()),
    path('checkpoint/objects/list-site', CheckpointSiteListView.as_view()),
    path('checkpoint/objects/update-site/<int:pk>', CheckpointSiteUpdateView.as_view()),
    path('checkpoint/objects/delete-site/<int:pk>', CheckpointSiteDeleteView.as_view()),
    path('f5/list-device', F5DeviceListView.as_view()),
    path('f5/objects/create-device', F5DeviceCreateView.as_view()),
    path('f5/objects/update-device/<int:pk>', F5DeviceUpdateView.as_view()),
    path('f5/objects/delete-device/<int:pk>', F5DeviceDeleteView.as_view()),
    path('f5/list-virtual-server', F5CreateVirtualServerListView.as_view()),
    path('f5/objects/create-virtual-server', F5CreateVirtualServerCreateView.as_view()),
    path('f5/objects/update-virtual-server/<int:pk>', F5CreateVirtualServerUpdateView.as_view()),
    path('f5/objects/delete-virtual-server/<int:pk>', F5CreateVirtualServerDeleteView.as_view()),
    path('f5/list-template', F5TemplateListView.as_view()),
    path('f5/objects/create-template', F5TemplateCreateView.as_view()),
    path('f5/objects/detail-template/<int:pk>', F5TemplateDetailView.as_view()),
    path('f5/objects/update-template/<int:pk>', F5TemplateUpdateView.as_view()),
    path('f5/objects/delete-template/<int:pk>', F5TemplateDeleteView.as_view()),
    path('proxy/objects/update-section/<int:pk>', ProxyRuleSectionUpdateView.as_view(), name='proxy_update_section'),
    path('proxy/objects/delete-section/<int:pk>', ProxyRuleSectionDeleteView.as_view(), name='proxy_delete_section'),
    path('proxy/list-section', ProxyRuleSectionListView.as_view(), name='proxy_list_section'),
    path('proxy/create-section', ProxyRuleSectionCreateView.as_view(), name='proxy_create_section'),
    path('proxy/objects/update-bypass-url/<int:pk>', ProxyBypassUrlUpdateView.as_view(), name='proxy_update_bypass_url'),
    path('proxy/objects/delete-bypass-url/<int:pk>', ProxyBypassUrlDeleteView.as_view(), name='proxy_delete_bypass_url'),
    path('proxy/list-bypass-url', ProxyBypassUrlListView.as_view(), name='proxy_list_bypass_url'),
    path('proxy/create-bypass-url', ProxyBypassUrlCreateView.as_view(), name='proxy_create_bypass_url'),
    path('proxy/localDatabaseUrl.txt', views.proxy_local_database_url, name='proxy_local_database_url')
]
