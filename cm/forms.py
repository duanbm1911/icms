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
            'f5_template',
            'service_name',
            'vs_name',
            'vs_ip',
            'vs_port',
            'pool_member',
            'client_ssl_profile',
            'server_ssl_profile'
        ]
        

class F5TemplateForm(forms.ModelForm):
    
    irules = forms.ModelMultipleChoiceField(
        queryset=F5Irule.objects.all(),
        to_field_name='irule_name',
        required=False
    )
    waf_profile = forms.ModelChoiceField(
        queryset=F5WafProfile.objects.all(),
        to_field_name='waf_profile',
        required=False
    )

    class Meta:
        model = F5Template
        fields = [
            'template_name',
            'partition',
            'protocol',
            'client_protocol_profile',
            'server_protocol_profile',
            'client_http_profile',
            'server_http_profile',
            'snat_name',
            'http_analytics_profile',
            'tcp_analytics_profile',
            'http_compression_profile',
            'web_acceleration_profile',
            'irules',
            'waf_profile'
        ]
    
    def clean_waf_profile(self):
        waf_profile = self.cleaned_data["waf_profile"]
        if waf_profile == None:
            waf_profile = str()
        return waf_profile