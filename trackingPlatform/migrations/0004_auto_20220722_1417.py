# Generated by Django 3.2.10 on 2022-07-22 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trackingPlatform', '0003_alter_lot_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lot',
            old_name='hash',
            new_name='txId',
        ),
        migrations.AlterField(
            model_name='lot',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 12, 17, 22, 26157, tzinfo=utc)),
        ),
    ]
