from django import forms
from inventory.models import *


class DeviceBasicInfoForm(forms.ModelForm):
    """Form definition for Device."""

    class Meta:
        """Meta definition for DeviceBasicInfoForm."""

        model = DeviceBasicInfo
        fields = ['device_name', 'device_ip', 'device_location', 'device_type', 'device_category', 'device_vendor', 'device_description']

class DeviceLocationForm(forms.ModelForm):
    """Form definition for DeviceLocation."""

    class Meta:
        """Meta definition for DeviceLocationform."""

        model = DeviceLocation
        fields = ['device_location', 'description']

class DeviceTypeForm(forms.ModelForm):
    """Form definition for DeviceType."""

    class Meta:
        """Meta definition for DeviceTypeform."""

        model = DeviceType
        fields = ['device_type', 'description']

class DeviceCategoryForm(forms.ModelForm):
    """Form definition for DeviceCategory."""

    class Meta:
        """Meta definition for DeviceCategoryform."""

        model = DeviceCategory
        fields = ['device_category', 'description']

class DeviceVendorForm(forms.ModelForm):
    """Form definition for DeviceVendor."""

    class Meta:
        """Meta definition for DeviceVendorform."""

        model = DeviceVendor
        fields = ['device_vendor', 'description']

class CreateDeviceBasicInfoForm(forms.Form):
    """CreateDeviceBasicInfoForm definition."""

    upload_file = forms.FileField()
