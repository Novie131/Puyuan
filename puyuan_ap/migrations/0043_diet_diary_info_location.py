# Generated by Django 4.2.4 on 2023-09-25 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0042_alter_diet_diary_info_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='diet_diary_info',
            name='location',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
