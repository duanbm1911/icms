from django import forms
from inventory.models import *
from django.core.exceptions import ValidationError
import re


def is_xss_validate(value):
    regex = '<([A-Za-z0-9_{}()/]+(\s|=)*)+>(.*<[A-Za-z/>]+)*'
    result = re.search(regex, value)
    if result:
        raise ValidationError('The input string contains unusual characters')
    
class DeviceForm(forms.ModelForm):
    device_name = forms.CharField(validators=[is_xss_validate])
    device_description = forms.CharField(validators=[is_xss_validate])
    class Meta:
        
        model = Device
        fields = [
            'device_name', 
            'device_ip', 
            'device_province', 
            'device_branch',
            'device_type',
            'device_category', 
            'device_vendor',
            'device_os',
            'device_tag',
            'device_stack',
            'device_description'
        ]
    

class DeviceProvinceForm(forms.ModelForm):
    device_province = forms.CharField(validators=[is_xss_validate])
    description = forms.CharField(validators=[is_xss_validate])
    class Meta:

        model = DeviceProvince
        fields = [
            'device_province', 
            'description'
            ]

class DeviceOSForm(forms.ModelForm):
    device_os = forms.CharField(validators=[is_xss_validate])
    description = forms.CharField(validators=[is_xss_validate])
    class Meta:

        model = DeviceOS
        fields = [
            'device_os', 
            'description'
            ]

class DeviceTypeForm(forms.ModelForm):
    device_type = forms.CharField(validators=[is_xss_validate])
    description = forms.CharField(validators=[is_xss_validate])
    class Meta:

        model = DeviceType
        fields = [
            'device_type', 
            'description'
            ]

class DeviceCategoryForm(forms.ModelForm):
    device_category = forms.CharField(validators=[is_xss_validate])
    description = forms.CharField(validators=[is_xss_validate])
    class Meta:

        model = DeviceCategory
        fields = [
            'device_category', 
            'description'
            ]

class DeviceVendorForm(forms.ModelForm):
    device_vendor = forms.CharField(validators=[is_xss_validate])
    description = forms.CharField(validators=[is_xss_validate])
    class Meta:

        model = DeviceVendor
        fields = [
            'device_vendor', 
            'description'
            ]
        
class DeviceBranchForm(forms.ModelForm):
    device_branch = forms.CharField(validators=[is_xss_validate])
    description = forms.CharField(validators=[is_xss_validate])
    class Meta:

        model = DeviceBranch
        fields = [
            'device_branch', 
            'description'
            ]
        
class DeviceTagForm(forms.ModelForm):
    device_tag = forms.CharField(validators=[is_xss_validate])
    description = forms.CharField(validators=[is_xss_validate])
    class Meta:

        model = DeviceTag
        fields = [
            'device_tag', 
            'description'
            ]

class CreateDeviceForm(forms.Form):
    upload_file = forms.FileField()


class DeviceManagementForm(forms.ModelForm):
    start_ma_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    end_ma_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    start_license_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    end_license_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    end_sw_support_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    end_hw_support_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    start_used_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    device_serial_number = forms.CharField(validators=[is_xss_validate])
    class Meta:
        model = DeviceManagement
        fields = [
            'device_ip', 
            'device_serial_number', 
            'start_ma_date', 
            'end_ma_date', 
            'start_license_date', 
            'end_license_date', 
            'end_sw_support_date', 
            'end_hw_support_date', 
            'start_used_date'
            ]


class DeviceInterfaceForm(forms.ModelForm):

    class Meta:
        model = DeviceInterface
        fields = [
            'device_ip',
            'list_interface_name',
            'list_interface_desc',
            'list_interface_speed',
            'list_interface_type',
            'list_interface_state',
        ]


class DeviceRackLayoutForm(forms.ModelForm):
    
    class Meta:
        model = DeviceRackLayout
        fields = [
            'device_ip',
            'device_rack_name',
            'device_rack_unit'
        ]


class DeviceConfigurationForm(forms.ModelForm):
    
    class Meta:
        model = DeviceConfiguration
        fields = [
            'device_ip',
            'device_config_standardized',
            'device_monitored',
            'device_backup_config'
        ]


class DeviceExportForm(forms.Form):
    CHOICES = (
        ('1', 'Device'),
        ('2', 'Device management'),
        ('3', 'Device rack layout'),
        ('4', 'Device configuration'),
        ('5', 'Device incorrect firmware'),
        ('6', 'Device expired license (6 months)'))
    database_table = forms.ChoiceField(label='Select database to export', choices=CHOICES, required=False)
    
class DeviceFirmwareForm(forms.ModelForm):

    class Meta:
        model = DeviceFirmware
        fields = [
            'device_type',
            'firmware',
            'description'
        ]