# Generated by Django 3.0.8 on 2021-09-25 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='itinerary',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]