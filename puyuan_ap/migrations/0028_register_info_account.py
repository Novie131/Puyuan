# Generated by Django 4.2.4 on 2023-09-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0027_vip_info_setting_info_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_info',
            name='account',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
