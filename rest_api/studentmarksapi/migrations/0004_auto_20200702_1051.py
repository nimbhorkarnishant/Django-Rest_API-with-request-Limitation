# Generated by Django 2.2.6 on 2020-07-02 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentmarksapi', '0003_request_counter_counter_req'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_counter',
            name='counter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
