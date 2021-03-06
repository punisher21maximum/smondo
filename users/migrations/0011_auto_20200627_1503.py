# Generated by Django 2.1.1 on 2020-06-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200627_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='floor',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14')], default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='society',
            field=models.CharField(choices=[('Smondo 3.0', 'Smondo 3.0'), ('Other', 'Other')], default='Smondo 3.0', max_length=50),
        ),
    ]
