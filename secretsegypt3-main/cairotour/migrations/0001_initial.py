# Generated by Django 3.0.8 on 2021-09-03 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cairotour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='property/')),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('itinerary', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_product')),
            ],
        ),
        migrations.CreateModel(
            name='cairotourReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pricee', models.IntegerField(default=0)),
                ('feedback', models.TextField(max_length=2000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('cairotour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cairotour_pcairo', to='cairotour.cairotour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cairotourImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_product')),
                ('cairotour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cairotour_Images', to='cairotour.cairotour')),
            ],
        ),
        migrations.CreateModel(
            name='cairotourBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('guest', models.CharField(choices=[(' 1 ', '1 '), ('2 ', '2'), ('3', '3'), ('4', '4')], max_length=100)),
                ('datesfrom', models.DateTimeField(default=django.utils.timezone.now)),
                ('cairotour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Book_cairotour', to='cairotour.cairotour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cairotour',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cairotour_category', to='cairotour.category'),
        ),
        migrations.AddField(
            model_name='cairotour',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cairotour_place', to='cairotour.place'),
        ),
        migrations.AddField(
            model_name='cairotour',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
