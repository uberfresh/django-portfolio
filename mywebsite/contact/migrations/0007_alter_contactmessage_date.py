# Generated by Django 3.2.4 on 2021-06-06 22:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_contactmessage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 22, 54, 27, 441269, tzinfo=utc)),
        ),
    ]
