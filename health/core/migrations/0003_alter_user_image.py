# Generated by Django 4.2.1 on 2023-05-29 17:39

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_first_time_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.user_image_file_path),
        ),
    ]
