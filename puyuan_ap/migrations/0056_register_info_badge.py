# Generated by Django 4.2.4 on 2023-09-26 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0055_alter_register_info_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_info',
            name='badge',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
