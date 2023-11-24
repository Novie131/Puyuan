# Generated by Django 4.2.4 on 2023-09-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puyuan_ap', '0053_delete_friend_info_delete_friend_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='friend_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, null=True)),
                ('name', models.CharField(default='', max_length=255, null=True)),
                ('relation_type', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='register_info',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]