# Generated by Django 4.2.1 on 2023-05-29 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_time_login',
            field=models.BooleanField(default=True),
        ),
    ]
