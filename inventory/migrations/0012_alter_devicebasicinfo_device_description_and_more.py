# Generated by Django 4.2.6 on 2024-01-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_rename_list_interface_neghbor_deviceinterface_list_interface_neighbor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicebasicinfo',
            name='device_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='devicebasicinfo',
            name='device_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='devicecategory',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='devicecategory',
            name='device_category',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='deviceinterface',
            name='list_interface_desc',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='deviceinterface',
            name='list_interface_inuse',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='deviceinterface',
            name='list_interface_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='deviceinterface',
            name='list_interface_neighbor',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='deviceinterface',
            name='list_interface_speed',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='deviceinterface',
            name='list_interface_state',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='deviceinterface',
            name='list_interface_type',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='deviceinterface',
            name='list_interface_unuse',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='devicelocation',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='devicelocation',
            name='device_location',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='devicemanagement',
            name='device_serial_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='devicemanagement',
            name='end_hw_support_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='devicemanagement',
            name='end_license_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='devicemanagement',
            name='end_ma_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='devicemanagement',
            name='end_sw_support_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='devicemanagement',
            name='start_license_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='devicemanagement',
            name='start_ma_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='devicemanagement',
            name='start_used_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='devicetopology',
            name='device_rack_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='devicetopology',
            name='device_rack_unit',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='device_type',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='devicevendor',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='devicevendor',
            name='device_vendor',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]