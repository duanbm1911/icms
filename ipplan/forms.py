from django import forms
from ipplan.models import *
from src.ipplan.func import *
from django.core.exceptions import ValidationError
from ipaddress import ip_network, IPv4Address
import re, json




def validate_xss(value):
    regex = '<([A-Za-z_{}()/]+(\s|=)*)+>(.*<[A-Za-z/>]+)*'
    result = re.search(regex, value)
    if result:
        raise ValidationError('The input string contains unusual characters')
    
class RegionForm(forms.ModelForm):
    """Form definition for IpProject."""
    region = forms.CharField(validators=[validate_xss])
    description = forms.CharField(validators=[validate_xss])
    class Meta:
        """Meta definition for IpProjectform."""

        model = Region
        fields = ('region', 'description')

class LocationForm(forms.ModelForm):
    """Form definition for Location."""
    location = forms.CharField(validators=[validate_xss])
    description = forms.CharField(validators=[validate_xss])
    
    class Meta:
        """Meta definition for Locationform."""

        model = Location
        fields = ('location', 'region', 'description',)

class SubnetForm(forms.ModelForm):
    """Form definition for Subnet."""
    name = forms.CharField(validators=[validate_xss])
    description = forms.CharField(validators=[validate_xss])
    
    class Meta:
        """Meta definition for Subnetform."""

        model = Subnet
        fields = ('subnet', 'name', 'location', 'description')

    def clean_subnet(self):
        subnet = self.cleaned_data.get('subnet')
        if is_subnet(subnet) is False:
            raise ValidationError("Subnet is not validated")
        return subnet


class SubnetUpdateForm(forms.ModelForm):
    """Form definition for Subnet."""
    name = forms.CharField(validators=[validate_xss])
    description = forms.CharField(validators=[validate_xss])
    
    class Meta:
        """Meta definition for Subnetform."""

        model = Subnet
        fields = ('name', 'location', 'description')
        

class RequestIpAddressForm(forms.Form):
    """RequestIpAddressForm definition."""

    subnet = forms.ModelChoiceField(queryset=Subnet.objects.all())
    ip_address = forms.CharField(validators=[validate_xss], widget=forms.SelectMultiple)
    status = forms.ModelChoiceField(queryset=IpStatus.objects.all())
    description = forms.CharField(max_length=200, validators=[validate_xss])

    def clean_subnet(self):
        subnet = self.cleaned_data.get('subnet')
        is_subnet_exists = Subnet.objects.filter(subnet=subnet).exists()
        if not is_subnet(subnet):
            raise ValidationError("Subnet is not validated")
        elif not is_subnet_exists:
            raise ValidationError("This subnet is not in database")
        return subnet

    def clean_ip_address(self):
        subnet = self.cleaned_data.get('subnet')
        list_ips = self.cleaned_data.get('ip_address')
        print(list_ips)
        used_ips = IpAddressModel.objects.filter(subnet__subnet=subnet).values_list('ip_address', flat=True)
        list_ips_overlap = [i for i in list_ips if i in used_ips]
        list_ips_invalid = [i for i in list_ips if is_ip(i) is False or IPv4Address(i) not in ip_network(subnet)]
        if list_ips_overlap:
            list_ips_overlap = ",".join(list_ips_overlap)
            raise ValidationError(f'IP address: {list_ips_overlap} already used')
        elif list_ips_invalid:
            list_ips_invalid = ",".join(list_ips_invalid)
            raise ValidationError(f'IP address: {list_ips_invalid} is invalid or not belong to subnet: {subnet}')
        return ",".join(list_ips)

class IpAddressModelForm(forms.ModelForm):
    """Form definition for IpAddressModel."""

    class Meta:
        """Meta definition for IpAddressModelform."""

        model = IpAddressModel
        fields = ('ip_address', 'subnet', 'status', 'description', )

class IpAddressModelUpdatelForm(forms.ModelForm):
    """Form definition for IpAddressModelUpdatelForm."""
    description = forms.CharField(validators=[validate_xss])
    
    class Meta:
        """Meta definition for IpAddressModelUpdatelForm."""

        model = IpAddressModel
        fields = ('ip_address', 'status', 'description', )
