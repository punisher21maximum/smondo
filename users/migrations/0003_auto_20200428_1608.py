# Generated by Django 3.0.5 on 2020-04-28 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200428_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='lname',
            new_name='last_name',
        ),
    ]
