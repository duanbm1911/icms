from django import forms
from ipplan.models import *
from src.ipplan.func import *
from django.core.exceptions import ValidationError


class IpRegoinForm(forms.ModelForm):
    """Form definition for IpProject."""

    class Meta:
        """Meta definition for IpProjectform."""

        model = IpRegoin
        fields = ('regoin', 'description')

class IpLocationForm(forms.ModelForm):
    """Form definition for IpLocation."""

    class Meta:
        """Meta definition for IpLocationform."""

        model = IpLocation
        fields = ('location', 'regoin', 'description',)

class IpSubnetForm(forms.ModelForm):
    """Form definition for IpSubnet."""

    class Meta:
        """Meta definition for IpSubnetform."""

        model = IpSubnet
        fields = ('subnet', 'name', 'location', 'description')

    def clean_subnet(self):
        subnet = self.cleaned_data.get('subnet')
        if ip_address_verify(subnet) is False:
            raise ValidationError("Subnet is not validated")
        return subnet

