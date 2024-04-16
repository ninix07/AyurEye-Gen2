# Generated by Django 5.0.4 on 2024-04-16 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inference_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='XRayImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img_file', models.ImageField(upload_to='images/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='XRayPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infection_type', models.CharField(max_length=255)),
                ('bounding_box_coordinates', models.JSONField(max_length=1000)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inference_api.xrayimage')),
            ],
        ),
        migrations.DeleteModel(
            name='XRayModel',
        ),
    ]