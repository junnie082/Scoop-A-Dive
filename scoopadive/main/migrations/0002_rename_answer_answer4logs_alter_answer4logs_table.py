# Generated by Django 5.0 on 2024-01-19 06:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Answer4Logs',
        ),
        migrations.AlterModelTable(
            name='answer4logs',
            table='Answer4Logs',
        ),
    ]