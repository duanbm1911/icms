# Generated by Django 4.2.6 on 2024-02-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0022_devicebasicinfo_device_firmware_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="deviceconfiguration",
            name="user_created",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="deviceinterface",
            name="user_created",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="devicemanagement",
            name="user_created",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="devicetopology",
            name="user_created",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="devicebasicinfo",
            name="user_created",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]