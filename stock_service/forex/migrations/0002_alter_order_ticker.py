# Generated by Django 3.2 on 2021-12-21 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='forex.ticker'),
        ),
    ]
