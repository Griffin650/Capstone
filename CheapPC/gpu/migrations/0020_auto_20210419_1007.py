# Generated by Django 3.1.7 on 2021-04-19 15:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gpu', '0019_auto_20210419_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpumodel',
            name='notify_users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='historicalprice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 10, 7, 40, 248228)),
        ),
    ]
