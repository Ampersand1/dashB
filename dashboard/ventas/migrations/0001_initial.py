# Generated by Django 5.0.4 on 2024-04-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=120)),
                ('ventas', models.CharField(max_length=120)),
                ('barrio', models.CharField(max_length=120)),
            ],
        ),
    ]
