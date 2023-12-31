# Generated by Django 4.2.5 on 2023-10-06 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0086_alter_setting_info_after_recording_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting_info',
            name='no_recording_for_a_day',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='setting_info',
            name='over_max_or_under_min',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 17, 15, 9, 585736)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='ended_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 17, 15, 9, 585736)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 17, 15, 9, 585736)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 17, 15, 9, 585736)),
        ),
    ]
