# Generated by Django 5.1.5 on 2025-02-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_Place', '0010_orderedpizza_ordertime_payment_details_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedpizza',
            name='deliverytime',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
