# Generated by Django 4.1.3 on 2023-01-12 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userevent_doctor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userevent',
            name='event_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Event Name'),
        ),
    ]
