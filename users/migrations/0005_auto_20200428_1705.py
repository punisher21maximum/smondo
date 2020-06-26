# Generated by Django 3.0.5 on 2020-04-28 17:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_student',
            name='roll_no',
            field=models.CharField(blank='True', max_length=3, validators=[django.core.validators.RegexValidator(message='example 70', regex='^[1-85]$')]),
        ),
    ]
