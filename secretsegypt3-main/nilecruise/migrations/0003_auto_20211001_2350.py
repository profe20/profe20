# Generated by Django 3.0.8 on 2021-10-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nilecruise', '0002_nilecruise_itinerary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnilecruisebook',
            name='guest',
            field=models.IntegerField(),
        ),
    ]
