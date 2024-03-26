from django import forms
from cm.models import *


class CheckpointPolicyForm(forms.ModelForm):

    class Meta:

        model = CheckpointPolicy
        fields = [
            'policy',
            'site_name'
        ]

class CheckpointSiteForm(forms.ModelForm):

    class Meta:

        model = CheckpointSite
        fields = [
            'site_name'
        ]