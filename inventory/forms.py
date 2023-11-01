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
            'device_description'
        ]

class DeviceLocationForm(forms.ModelForm):

    class Meta:

        model = DeviceLocation
        fields = [
            'device_location', 
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
            'count_interface',
            'list_interface_name',
            'list_interface_desc',
            'list_interface_inuse',
            'list_interface_unuse',
            'list_interface_speed',
            'list_interface_type',
            'list_interface_state',
            'list_interface_neghbor'
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
