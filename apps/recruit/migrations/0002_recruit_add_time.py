# Generated by Django 2.0.5 on 2018-12-27 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]
