# Generated by Django 3.0.8 on 2021-05-29 14:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='packagessBook',
            new_name='packagesBook',
        ),
    ]