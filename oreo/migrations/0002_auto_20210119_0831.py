# Generated by Django 3.1.5 on 2021-01-19 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oreo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='message',
            name='upadted',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
