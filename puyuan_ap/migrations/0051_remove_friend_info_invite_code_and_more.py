# Generated by Django 4.2.4 on 2023-09-25 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0050_register_info_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend_info',
            name='invite_code',
        ),
        migrations.AddField(
            model_name='register_info',
            name='invite_code',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]