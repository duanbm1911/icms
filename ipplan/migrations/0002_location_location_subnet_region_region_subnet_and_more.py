# Generated by Django 5.0.1 on 2024-07-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipplan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_subnet',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='region_subnet',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subnetgroup',
            name='group_subnet',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ipaddressmodel',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='region',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='subnet',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='subnetgroup',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='subnetgroup',
            name='group',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]