# Generated by Django 5.0.1 on 2024-04-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_rename_devicetopology_deviceracklayout'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
