# Generated by Django 3.0.8 on 2021-03-30 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20210330_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='place',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property_place', to='property.place'),
            preserve_default=False,
        ),
    ]
