# Generated by Django 2.2 on 2019-04-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boilerplate', '0007_merge_20190412_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='due_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
