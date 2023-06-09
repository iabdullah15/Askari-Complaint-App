# Generated by Django 4.1.7 on 2023-03-30 20:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('BuildingNo', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('sector', models.CharField(choices=[('A', 'SECTOR A'), ('B', 'SECTOR B'), ('C', 'SECTOR C')], max_length=1)),
                ('floors', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(7)])),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FlatNo', models.CharField(max_length=2)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('BuildingNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComplaintApp.building')),
            ],
        ),
    ]
