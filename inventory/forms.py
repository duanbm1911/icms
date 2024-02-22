from django import forms
from inventory.models import *


class DeviceBasicInfoForm(forms.ModelForm):

    class Meta:

        model = DeviceBasicInfo
        fields = [
            'device_name', 
            'device_ip', 
            'device_location', 
            'device_type', 
            'device_category', 
            'device_vendor', 
            'device_os',
            'device_stack',
            'device_description'
        ]

class DeviceLocationForm(forms.ModelForm):
    class Meta:

        model = DeviceLocation
        fields = [
            'device_location', 
            'description'
            ]

class DeviceOSForm(forms.ModelForm):
    class Meta:

        model = DeviceOS
        fields = [
            'device_os', 
            'description'
            ]

class DeviceTypeForm(forms.ModelForm):

    class Meta:

        model = DeviceType
        fields = [
            'device_type', 
            'description'
            ]

class DeviceCategoryForm(forms.ModelForm):

    class Meta:

        model = DeviceCategory
        fields = [
            'device_category', 
            'description'
            ]

class DeviceVendorForm(forms.ModelForm):

    class Meta:

        model = DeviceVendor
        fields = [
            'device_vendor', 
            'description'
            ]

class CreateDeviceBasicInfoForm(forms.Form):

    upload_file = forms.FileField()


class DeviceManagementForm(forms.ModelForm):
    start_ma_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    end_ma_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    start_license_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    end_license_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    end_sw_support_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    end_hw_support_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
    start_used_date = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}), required=False)
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


class DeviceTopologyForm(forms.ModelForm):
    
    class Meta:
        model = DeviceTopology
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
        ('0', '-----------------'),
        ('1', 'Device basic info'),
        ('2', 'Device management'),
        ('3', 'Device topology'),
        ('4', 'Device configuration'))
    database_table = forms.ChoiceField(label='Select database to export', choices=CHOICES, required=False)