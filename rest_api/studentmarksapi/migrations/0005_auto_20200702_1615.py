# Generated by Django 2.2.6 on 2020-07-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmarksapi', '0004_auto_20200702_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request_counter',
            name='counter',
        ),
        migrations.RemoveField(
            model_name='request_counter',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='request_counter',
            name='counter_req',
            field=models.IntegerField(default=0),
        ),
    ]