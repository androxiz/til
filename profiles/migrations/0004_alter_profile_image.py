# Generated by Django 5.1.5 on 2025-01-18 16:04

import sorl.thumbnail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='profiles/default_avatar/avatar.png', upload_to='profiles'),
        ),
    ]
