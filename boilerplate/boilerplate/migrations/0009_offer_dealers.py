# Generated by Django 2.2 on 2019-04-13 08:28

import boilerplate.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boilerplate', '0008_auto_20190413_0734'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='dealers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=boilerplate.models.create_dealer_list, size=None),
        ),
    ]
