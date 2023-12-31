# Generated by Django 4.2.6 on 2023-10-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_devicevendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicecategory',
            name='creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='devicecategory',
            name='description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devicelocation',
            name='creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='devicelocation',
            name='description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devicemodel',
            name='device_creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='devicemodel',
            name='device_description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devicetype',
            name='creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devicevendor',
            name='creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='devicevendor',
            name='description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
