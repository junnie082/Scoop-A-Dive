# Generated by Django 5.0.1 on 2024-01-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_log_diver'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='diver',
            field=models.CharField(max_length=20, null=True),
        ),
    ]