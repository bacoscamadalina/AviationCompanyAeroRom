# Generated by Django 4.2.13 on 2024-05-21 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_alter_cart_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='arrival',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='arrival_discount', to='tickets.destinations'),
        ),
    ]
