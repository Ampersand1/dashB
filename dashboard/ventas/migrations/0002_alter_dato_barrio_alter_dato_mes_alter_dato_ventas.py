# Generated by Django 5.0.4 on 2024-04-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dato',
            name='barrio',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dato',
            name='mes',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dato',
            name='ventas',
            field=models.IntegerField(),
        ),
    ]