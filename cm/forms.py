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
        
class F5DeviceForm(forms.ModelForm):
    
    class Meta:
        model = F5Device
        fields = [
            'f5_device_ip',
            'f5_device_name',
        ]
        

class F5CreateVirtualServerForm(forms.ModelForm):

    class Meta:
        model = F5CreateVirtualServer
        fields = [
            'f5_device_ip',
            'service_name',
            'vs_name',
            'vs_ip',
            'vs_port',
            'pool_member',
            'client_ssl_profile',
            'server_ssl_profile'
        ]