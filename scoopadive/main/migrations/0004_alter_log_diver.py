# Generated by Django 5.0 on 2024-02-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_log_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='diver',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
