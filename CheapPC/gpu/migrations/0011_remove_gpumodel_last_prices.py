# Generated by Django 3.1.7 on 2021-04-14 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpu', '0010_gpumodel_last_prices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpumodel',
            name='last_prices',
        ),
    ]