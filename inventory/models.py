from django.db import models


# Create your models here.

class DeviceProvince(models.Model):
    device_province = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_province
    
class DeviceType(models.Model):
    device_type = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_type

class DeviceCategory(models.Model):
    device_category = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_category
    
class DeviceVendor(models.Model):
    device_vendor = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_vendor

class DeviceOS(models.Model):
    device_os = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_os
    
class DeviceBranch(models.Model):
    device_branch = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_branch
    
class DeviceTag(models.Model):
    device_tag = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        return self.device_tag

    
class Device(models.Model):
    device_name = models.CharField(max_length=200, blank=True)
    device_ip = models.GenericIPAddressField(unique=True)
    device_province = models.ForeignKey('DeviceProvince', on_delete=models.PROTECT)
    device_branch = models.ForeignKey('DeviceBranch', on_delete=models.PROTECT, blank=True, null=True)
    device_type = models.ForeignKey('DeviceType', on_delete=models.PROTECT)
    device_category = models.ForeignKey('DeviceCategory', on_delete=models.PROTECT)
    device_vendor = models.ForeignKey('DeviceVendor', on_delete=models.PROTECT)
    device_os = models.ForeignKey('DeviceOS', on_delete=models.PROTECT)
    device_tag = models.ForeignKey('DeviceTag', on_delete=models.PROTECT, blank=True, null=True)
    device_firmware = models.CharField(max_length=200, blank=True, null=True)
    device_status = models.CharField(max_length=200, blank=True, null=True)
    device_stack = models.BooleanField(default=False, blank=True, null=True)
    device_description = models.CharField(max_length=200, blank=True, null=True)
    device_creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.device_ip

class DeviceManagement(models.Model):
    """Model definition for DeviceManagement."""

    device_ip = models.ForeignKey('Device', on_delete=models.CASCADE)
    device_serial_number = models.CharField(max_length=100, blank=True, unique=True)
    start_ma_date = models.DateField(blank=True, null=True)
    end_ma_date = models.DateField(blank=True, null=True)
    start_license_date = models.DateField(blank=True, null=True)
    end_license_date = models.DateField(blank=True, null=True)
    end_sw_support_date = models.DateField(blank=True, null=True)
    end_hw_support_date = models.DateField(blank=True, null=True)
    start_used_date = models.DateField(blank=True, null=True)
    user_created = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """Unicode representation of DeviceManagement."""
        return str(self.device_ip)

class DeviceInterface(models.Model):
    """Model definition for DeviceInterface."""

    device_ip = models.ForeignKey('Device', on_delete=models.CASCADE)
    list_interface_name = models.JSONField(max_length=4000, blank=True, null=True)
    list_interface_desc = models.JSONField(max_length=4000, blank=True, null=True)
    list_interface_speed = models.JSONField(max_length=4000, blank=True, null=True)
    list_interface_type = models.JSONField(max_length=4000, blank=True, null=True)
    list_interface_state = models.JSONField(max_length=4000, blank=True, null=True)
    user_created = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        """Unicode representation of DeviceInterface."""
        return str(self.device_ip)


class DeviceRackLayout(models.Model):
    """Model definition for DeviceRackLayout."""

    device_ip = models.ForeignKey('Device', on_delete=models.CASCADE)
    device_rack_name = models.CharField(max_length=200, blank=True, null=True)
    device_rack_unit = models.IntegerField(blank=True, null=True)
    user_created = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        """Unicode representation of DeviceRackLayout."""
        return str(self.device_ip)
    

class DeviceConfiguration(models.Model):
    """Model definition for DeviceConfiguration."""

    device_ip = models.ForeignKey('Device', on_delete=models.CASCADE)
    device_config_standardized = models.BooleanField(blank=True, null=True)
    device_monitored = models.BooleanField(blank=True, null=True)
    device_backup_config = models.BooleanField(blank=True, null=True)
    user_created = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """Unicode representation of DeviceConfiguration."""
        return str(self.device_ip)
    
class DeviceFirmware(models.Model):
    """Model definition for DeviceFirmware."""
    
    device_type = models.ForeignKey('DeviceType', on_delete=models.CASCADE)
    firmware = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        """Unicode representation of DeviceFirmware."""
        return str(self.firmware)