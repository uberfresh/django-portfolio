# Generated by Django 3.2.4 on 2021-06-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_alter_contactmessage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
