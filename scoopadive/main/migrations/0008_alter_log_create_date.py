# Generated by Django 5.0.1 on 2024-01-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_log_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='create_date',
            field=models.DateTimeField(default='2024-01-01'),
        ),
    ]