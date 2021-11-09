# Generated by Django 3.0.8 on 2021-04-01 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20210327_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='image',
            new_name='Our_Values',
        ),
        migrations.RemoveField(
            model_name='about',
            name='title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='title3',
        ),
        migrations.AddField(
            model_name='about',
            name='Our_Story',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='Our_image',
            field=models.ImageField(blank=True, null=True, upload_to='main_product'),
        ),
        migrations.AddField(
            model_name='about',
            name='Who_We_Are',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='Who_image',
            field=models.ImageField(blank=True, null=True, upload_to='main_product'),
        ),
    ]
