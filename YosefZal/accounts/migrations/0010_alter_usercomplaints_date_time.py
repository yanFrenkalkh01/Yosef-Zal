# Generated by Django 4.1.3 on 2023-01-13 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_usercomplaints_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomplaints',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 1, 13, 7, 42, 9, 57194, tzinfo=datetime.timezone.utc), verbose_name='Date Time'),
            preserve_default=False,
        ),
    ]
