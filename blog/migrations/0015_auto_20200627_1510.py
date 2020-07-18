# Generated by Django 2.1.1 on 2020-06-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200627_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rent_day',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='rent_hour',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='rent_month',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='rent_week',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sell_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
