# Generated by Django 3.0.8 on 2021-05-30 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeatrip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='makeatrip',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='makeatrip',
            name='nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]