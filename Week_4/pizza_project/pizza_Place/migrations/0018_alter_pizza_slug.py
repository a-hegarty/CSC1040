# Generated by Django 5.1.5 on 2025-02-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_Place', '0017_remove_pizza_customer_id_pizza_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='slug',
            field=models.SlugField(default='{User.id}/{Pizza.id}'),
        ),
    ]
