# Generated by Django 3.0.8 on 2021-04-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20210403_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='guest',
            field=models.IntegerField(choices=[(' 1 ', '1 '), ('2 ', '2'), ('3', '3'), ('4', '4')], max_length=100),
        ),
    ]