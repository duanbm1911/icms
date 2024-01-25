from django.db import models

# Create your models here.

class Region(models.Model):
    """Model definition for Region."""

    region = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __unicode__(self):
        """Unicode representation of Region."""
        return self.region


class Location(models.Model):
    """Model definition for Location."""

    location = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __unicode__(self):
        """Unicode representation of Location."""
        return self.location


class Subnet(models.Model):
    """Model definition for Subnet."""

    subnet = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)

    def __unicode__(self):
        """Unicode representation of Subnet."""
        return self.subnet

class IpStatus(models.Model):
    """Model definition for IpAddressStatus."""

    status = models.CharField(max_length=100)

    def __unicode__(self):
        """Unicode representation of IpAddressStatus."""
        return self.status


class IpAddressModel(models.Model):
    """Model definition for IpModel."""

    ip_address = models.GenericIPAddressField(unique=True)
    subnet = models.ForeignKey('Subnet', on_delete=models.CASCADE)
    status = models.ForeignKey('IpStatus', on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    created_time = models.DateTimeField(auto_now=True)
    user_created = models.CharField(max_length=100)


    def __unicode__(self):
        """Unicode representation of IpModel."""
        return self.ip_address



