# Generated by Django 2.2 on 2019-04-12 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boilerplate', '0003_auto_20190412_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('Success', 'S'), ('Fail', 'F'), ('Pending', 'P')], max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='dealer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='boilerplate.Dealer'),
        ),
    ]
