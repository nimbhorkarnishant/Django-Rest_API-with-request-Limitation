# Generated by Django 2.2.6 on 2020-07-02 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmarksapi', '0005_auto_20200702_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_counter',
            name='counter_req',
            field=models.IntegerField(default=None),
        ),
    ]