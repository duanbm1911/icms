# Generated by Django 4.2.6 on 2024-04-11 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_devicebranch_devicetag_device_device_branch_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeviceLocation',
            new_name='DeviceProvince',
        ),
        migrations.RenameField(
            model_name='deviceprovince',
            old_name='device_location',
            new_name='device_province',
        ),
    ]
