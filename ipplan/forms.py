from django import forms
from ipplan.models import *
from src.ipplan.func import *
from django.core.exceptions import ValidationError


class IpLocationForm(forms.ModelForm):
    """Form definition for IpLocation."""

    class Meta:
        """Meta definition for IpLocationform."""

        model = IpLocation
        fields = ('location','description',)

class IpProjectForm(forms.ModelForm):
    """Form definition for IpProject."""

    class Meta:
        """Meta definition for IpProjectform."""

        model = IpProject
        fields = ('project', 'description')

class IpSubnetForm(forms.ModelForm):
    """Form definition for IpSubnet."""

    class Meta:
        """Meta definition for IpSubnetform."""

        model = IpSubnet
        fields = ('subnet', 'location', 'project', 'description')

    def clean_subnet(self):
        subnet = self.cleaned_data.get('subnet')
        if ip_address_verify(subnet) is False:
            raise ValidationError("Subnet is not validated")
        return subnet

