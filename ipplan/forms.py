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
        if is_subnet(subnet) is False:
            raise ValidationError("Subnet is not validated")
        return subnet

class RequestIpAddressForm(forms.Form):
    """RequestIpAddressForm definition."""

    subnet = forms.ModelChoiceField(queryset=IpSubnet.objects.all())
    count = forms.IntegerField()
    status = forms.ModelChoiceField(queryset=IpStatus.objects.all())
    description = forms.CharField(max_length=200)

    def clean_subnet(self):
        subnet = self.cleaned_data.get('subnet')
        is_subnet_exists = IpSubnet.objects.filter(subnet=subnet).exists()
        if not is_subnet(subnet):
            raise ValidationError("Subnet is not validated")
        elif not is_subnet_exists:
            raise ValidationError("This subnet is not in database")
        return subnet


