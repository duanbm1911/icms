# Generated by Django 4.2.6 on 2024-07-03 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='f5template',
            name='client_http_profile',
        ),
        migrations.RemoveField(
            model_name='f5template',
            name='client_protocol_profile',
        ),
        migrations.RemoveField(
            model_name='f5template',
            name='http_analytics_profile',
        ),
        migrations.RemoveField(
            model_name='f5template',
            name='http_compression_profile',
        ),
        migrations.RemoveField(
            model_name='f5template',
            name='partition',
        ),
        migrations.RemoveField(
            model_name='f5template',
            name='protocol',
        ),
        migrations.RemoveField(
            model_name='f5template',
            name='server_http_profile',
        ),
        migrations.RemoveField(
            model_name='f5template',
            name='server_protocol_profile',
        ),
        migrations.RemoveField(
            model_name='f5template',
            name='snat_name',
        ),
        migrations.RemoveField(
            model_name='f5template',
            name='tcp_analytics_profile',
        ),
        migrations.RemoveField(
            model_name='f5template',
            name='web_acceleration_profile',
        ),
    ]