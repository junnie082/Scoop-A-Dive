# Generated by Django 5.0.1 on 2024-01-17 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='create_date',
            field=models.DateTimeField(null=True),
        ),
    ]
