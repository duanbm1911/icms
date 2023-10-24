from django.db import models

# Create your models here.


class IpLocation(models.Model):
    """Model definition for IpLocation."""

    location = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        """Unicode representation of IpLocation."""
        return self.location

class IpProject(models.Model):
    """Model definition for IpProject."""

    project = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        """Unicode representation of IpProject."""
        return self.project

class IpSubnet(models.Model):
    """Model definition for IpSubnet."""

    subnet = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey('IpLocation', on_delete=models.CASCADE)
    project = models.ForeignKey('IpProject', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __str__(self):
        """Unicode representation of IpSubnet."""
        return subnet

class IpStatus(models.Model):
    """Model definition for IpStatus."""
    status = models.CharField(max_length=100)

    def __str__(self):
        """Unicode representation of IpStatus."""
        return self.status


class IpModel(models.Model):
    """Model definition for IpModel."""

    ip_address = models.GenericIPAddressField()
    subnet = models.ForeignKey('IpSubnet', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    status = models.ForeignKey('IpStatus', on_delete = models.CASCADE)
    user_request = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)


    def __str__(self):
        """Unicode representation of IpModel."""
        return self.ip_address



