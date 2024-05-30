from django import forms
from ipplan.models import *
from src.ipplan.func import *
from django.core.exceptions import ValidationError
import re



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
    count = forms.IntegerField()
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
