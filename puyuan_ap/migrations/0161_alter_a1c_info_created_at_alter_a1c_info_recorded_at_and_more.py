# Generated by Django 4.2.5 on 2023-10-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0160_alter_a1c_info_created_at_alter_a1c_info_recorded_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='a1c_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-23 16:36:11'),
        ),
        migrations.AlterField(
            model_name='a1c_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-23 16:36:11'),
        ),
        migrations.AlterField(
            model_name='a1c_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-23 16:36:11'),
        ),
        migrations.AlterField(
            model_name='blood_sugar_info',
            name='recorded_at',
            field=models.DateTimeField(default='2023-10-23 16:36:11'),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-23 16:36:11'),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-23 16:36:11'),
        ),
        migrations.AlterField(
            model_name='setting_info',
            name='created_at',
            field=models.DateTimeField(default='2023-10-23 16:36:11'),
        ),
        migrations.AlterField(
            model_name='setting_info',
            name='updated_at',
            field=models.DateTimeField(default='2023-10-23 16:36:11'),
        ),
    ]
