# Generated by Django 3.0.5 on 2020-04-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_enotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enotes',
            name='starred',
            field=models.BooleanField(default=False),
        ),
    ]
