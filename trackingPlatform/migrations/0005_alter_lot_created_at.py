# Generated by Django 3.2.10 on 2022-07-22 12:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trackingPlatform', '0004_auto_20220722_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 12, 50, 52, 896511, tzinfo=utc)),
        ),
    ]
