# Generated by Django 5.1.3 on 2024-11-19 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date_posted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 11, 19, 17, 17, 29, 75910, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
