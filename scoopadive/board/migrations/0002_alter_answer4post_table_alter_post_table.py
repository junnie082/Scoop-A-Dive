# Generated by Django 5.0 on 2024-01-19 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='answer4post',
            table='Answer4Post',
        ),
        migrations.AlterModelTable(
            name='post',
            table='Post',
        ),
    ]