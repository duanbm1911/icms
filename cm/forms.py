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
        ('Success', 'Success')
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