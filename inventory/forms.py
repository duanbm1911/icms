from django import forms
from inventory.models import *


class DeviceForm(forms.ModelForm):
    """Form definition for Device."""

    class Meta:
        """Meta definition for Deviceform."""

        model = DeviceModel
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

class CreateDeviceForm(forms.Form):
    """CreateDeviceForm definition."""

    upload_file = forms.FileField()
