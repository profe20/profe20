# Generated by Django 3.0.8 on 2021-06-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0014_slideimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slideimages',
            old_name='namee',
            new_name='Luxor',
        ),
        migrations.AddField(
            model_name='slideimages',
            name='aswan',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slideimages',
            name='makeatrip',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slideimages',
            name='tourpackages',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]