# Generated by Django 4.2.4 on 2023-09-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0015_remove_friend_info_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a1c_info',
            name='a1c',
            field=models.IntegerField(null=True),
        ),
    ]
