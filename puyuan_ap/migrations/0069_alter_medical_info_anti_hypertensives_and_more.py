# Generated by Django 4.2.5 on 2023-10-05 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0068_alter_medical_info_anti_hypertensives_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical_info',
            name='anti_hypertensives',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='insulin',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='medical_info',
            name='oad',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
