# Generated by Django 5.0.6 on 2024-05-16 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_price_end_date_price_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='arrival',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='arrival_prices', to='tickets.destinations'),
        ),
        migrations.AlterField(
            model_name='price',
            name='end_date',
            field=models.DateField(default='2023-12-31'),
        ),
        migrations.AlterField(
            model_name='price',
            name='start_date',
            field=models.DateField(default='2023-12-31'),
        ),
    ]
