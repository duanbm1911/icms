# Generated by Django 4.2.6 on 2024-07-19 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckpointPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy', models.CharField(max_length=200, unique=True)),
                ('layer', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckpointSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=100, unique=True)),
                ('smc', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckpointRuleSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(blank=True, max_length=100)),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cm.checkpointpolicy')),
            ],
        ),
        migrations.CreateModel(
            name='CheckpointRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('source', models.CharField(max_length=1000)),
                ('destination', models.CharField(max_length=1000)),
                ('protocol', models.CharField(max_length=1000)),
                ('schedule', models.CharField(blank=True, max_length=1000)),
                ('section', models.CharField(blank=True, max_length=100)),
                ('user_created', models.CharField(max_length=200)),
                ('time_created', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=200)),
                ('message', models.CharField(blank=True, max_length=3000, null=True)),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cm.checkpointpolicy')),
            ],
        ),
        migrations.AddField(
            model_name='checkpointpolicy',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cm.checkpointsite'),
        ),
    ]