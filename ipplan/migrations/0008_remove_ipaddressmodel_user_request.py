# Generated by Django 4.2.6 on 2023-10-27 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipplan', '0007_ipstatus_ipaddressmodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipaddressmodel',
            name='user_request',
        ),
    ]
