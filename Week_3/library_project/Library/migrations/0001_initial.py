# Generated by Django 5.1.5 on 2025-02-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.DateField()),
                ('author', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('title', models.CharField(max_length=30)),
                ('synopsis', models.TextField()),
            ],
        ),
    ]
