# Generated by Django 4.2 on 2024-10-11 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Conference', '0003_alter_conference_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 10, 11, 10, 31, 55, 408701, tzinfo=datetime.timezone.utc)),
        ),
    ]