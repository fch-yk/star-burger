# Generated by Django 4.1.5 on 2023-02-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, unique=True, verbose_name='адрес')),
                ('latitude', models.FloatField(verbose_name='широта')),
                ('longitude', models.FloatField(verbose_name='долгота')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='изменена в')),
            ],
            options={
                'verbose_name': 'локация',
                'verbose_name_plural': 'локации',
            },
        ),
    ]
