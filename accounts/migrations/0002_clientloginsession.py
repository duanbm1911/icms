# Generated by Django 5.0.1 on 2024-05-30 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientLoginSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_ip', models.GenericIPAddressField()),
                ('failed_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]