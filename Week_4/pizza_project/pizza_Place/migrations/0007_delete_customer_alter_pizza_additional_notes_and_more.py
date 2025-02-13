# Generated by Django 5.1.5 on 2025-02-13 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_Place', '0006_remove_pizza_toppings_pizza_toppings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AlterField(
            model_name='pizza',
            name='additional_notes',
            field=models.TextField(default='no other instructions'),
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza_Place.topping'),
            preserve_default=False,
        ),
    ]
