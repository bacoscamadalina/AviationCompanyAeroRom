# Generated by Django 4.2.13 on 2024-05-25 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_cartitem_passenger_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='passenger_names',
        ),
    ]
