# Generated by Django 4.2.13 on 2024-05-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_cartitem_depart_date_cartitem_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='passenger_names',
            field=models.CharField(default='', max_length=100),
        ),
    ]
