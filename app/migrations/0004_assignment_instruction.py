# Generated by Django 3.2.23 on 2024-02-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_employee_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='instruction',
            field=models.TextField(null=True),
        ),
    ]