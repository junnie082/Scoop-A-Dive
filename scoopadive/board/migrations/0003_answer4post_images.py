# Generated by Django 5.0 on 2024-01-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_answer4post_table_alter_post_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer4post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
