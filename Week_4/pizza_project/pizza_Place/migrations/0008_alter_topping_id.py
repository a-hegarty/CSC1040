# Generated by Django 5.1.5 on 2025-02-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_Place', '0007_rename_customer_id_pizza_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
