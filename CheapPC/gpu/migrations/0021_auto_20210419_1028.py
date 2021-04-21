# Generated by Django 3.1.7 on 2021-04-19 15:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gpu', '0020_auto_20210419_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpumodel',
            name='notify_users',
        ),
        migrations.AlterField(
            model_name='historicalprice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 10, 28, 26, 824278)),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpu.gpumodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
