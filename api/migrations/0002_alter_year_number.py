# Generated by Django 3.2 on 2021-05-07 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='number',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]
