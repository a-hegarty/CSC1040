# Generated by Django 5.1.5 on 2025-02-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_Place', '0005_alter_pizza_toppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='pizza_Place.topping'),
        ),
    ]
