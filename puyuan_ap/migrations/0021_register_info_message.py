# Generated by Django 4.2.4 on 2023-09-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0020_remove_register_info_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_info',
            name='message',
            field=models.CharField(max_length=30, null=True),
        ),
    ]