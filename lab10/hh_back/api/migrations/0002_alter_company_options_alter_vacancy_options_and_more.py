# Generated by Django 5.0.3 on 2024-04-12 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={},
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
