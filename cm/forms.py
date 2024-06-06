from django import forms
from cm.models import *


class CheckpointPolicyForm(forms.ModelForm):

    class Meta:

        model = CheckpointPolicy
        fields = [
            'policy',
            'layer',
            'section',
            'site'
        ]

class CheckpointSiteForm(forms.ModelForm):

    class Meta:

        model = CheckpointSite
        fields = [
            'site',
            'smc'
        ]

class CheckpointRuleForm(forms.ModelForm):
    
    STATUS = (
        ('Created', 'Created'),
        ('Processing', 'Processing'),
        ('Failed', 'Failed'),
        ('Success', 'Success'),
        ('Install-Only', 'Install-Only')
    )
    
    status = forms.ChoiceField(choices=STATUS)
    
    class Meta:
        model = CheckpointRule
        fields = [
            'policy',
            'description',
            'source',
            'destination',
            'protocol',
            'schedule',
            'status'
        ]
        

class LBDeviceCategoryForm(forms.ModelForm):
    
    class Meta:
        model = LBDeviceCategory
        fields = [
            'device_category'
        ]
        
class LBDeviceForm(forms.ModelForm):
    
    class Meta:
        model = LBDevice
        fields = [
            'device_ip',
            'device_name',
            'device_category'
        ]
        

class LBCreateVirtualServerForm(forms.ModelForm):

    class Meta:
        model = LBCreateVirtualServer
        fields = [
            'service_name',
            'vs_name',
            'vs_ip',
            'vs_port',
            'pool_name',
            'client_ssl_profile',
            'server_ssl_profile'
        ]