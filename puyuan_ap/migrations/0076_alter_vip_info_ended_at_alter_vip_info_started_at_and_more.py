# Generated by Django 4.2.5 on 2023-10-06 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0075_remove_setting_info_name_default_info_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip_info',
            name='ended_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 15, 48, 16, 870438)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='started_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 15, 48, 16, 870438)),
        ),
        migrations.AlterField(
            model_name='vip_info',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 15, 48, 16, 870438)),
        ),
    ]