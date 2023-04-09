# Generated by Django 4.1.3 on 2023-04-07 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintApp', '0003_flat_resident'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComplaintType', models.CharField(max_length=255)),
                ('ComplaintDescription', models.TextField()),
                ('ComplaintTime', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to=settings.AUTH_USER_MODEL)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Resident', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]