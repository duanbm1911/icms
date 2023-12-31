# Generated by Django 4.2.6 on 2023-10-30 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_devicemodel_device_vendor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeviceModel',
            new_name='DeviceBaseInfo',
        ),
        migrations.CreateModel(
            name='DeviceManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_ma_date', models.DateField()),
                ('end_ma_date', models.DateField()),
                ('start_license_date', models.DateField()),
                ('end_license_date', models.DateField()),
                ('end_sw_support_date', models.DateField()),
                ('end_hw_support_date', models.DateField()),
                ('start_used_date', models.DateField()),
                ('device_ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.devicebaseinfo')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceInterface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_interface', models.CharField(max_length=500)),
                ('count_interface', models.IntegerField()),
                ('list_interface_inuse', models.CharField(max_length=500)),
                ('list_interface_unuse', models.CharField(max_length=500)),
                ('list_interface_neighbor', models.CharField(max_length=500)),
                ('list_interface_speed', models.CharField(max_length=500)),
                ('device_ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.devicebaseinfo')),
            ],
        ),
    ]
