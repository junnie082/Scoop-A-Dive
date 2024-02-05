# Generated by Django 5.0.1 on 2024-02-04 13:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('diveLicense', models.CharField(blank=True, max_length=50, null=True)),
                ('is_ststMember', models.BooleanField(blank=True, default=False, null=True)),
                ('studentID', models.IntegerField(blank=True, null=True)),
                ('major', models.CharField(blank=True, max_length=50, null=True)),
                ('kisu', models.IntegerField(blank=True, null=True)),
                ('is_absence', models.BooleanField(blank=True, default=False, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('loglist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.log')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Profiles',
            },
        ),
    ]
