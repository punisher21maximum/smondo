# Generated by Django 2.1.1 on 2020-06-27 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200626_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwoWheeler',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Post')),
                ('km', models.PositiveIntegerField(blank=True, help_text='KM driven')),
                ('cc', models.PositiveIntegerField(blank=True, help_text='CC')),
                ('year', models.PositiveIntegerField(blank=True, help_text='bought year')),
            ],
            bases=('blog.post',),
        ),
        migrations.AlterField(
            model_name='post',
            name='rent_day',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='rent_hour',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='rent_month',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='rent_week',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sell_price',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='like pulsar, duke', max_length=100),
        ),
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('twowheeler_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.TwoWheeler')),
                ('brand', models.CharField(choices=[('Hercules', 'Hercules'), ('Hero', 'Hero'), ('Other', 'Other')], default='Other', max_length=100)),
            ],
            bases=('blog.twowheeler',),
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('twowheeler_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.TwoWheeler')),
                ('brand', models.CharField(choices=[('Bajaj', 'Bajaj'), ('Hero', 'Hero'), ('Honda', 'Honda'), ('Hero-honda', 'Hero-honda'), ('KTM', 'KTM'), ('Yamaha', 'Yamaha'), ('Suzuki', 'Suzuki'), ('TVS', 'TVS'), ('Royal-Enfield', 'Royal-Enfield'), ('Other', 'Other')], default='Other', max_length=100)),
            ],
            bases=('blog.twowheeler',),
        ),
        migrations.CreateModel(
            name='Scooty',
            fields=[
                ('twowheeler_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.TwoWheeler')),
                ('brand', models.CharField(choices=[('Bajaj', 'Bajaj'), ('Hero', 'Hero'), ('Honda', 'Honda'), ('Mahindra', 'Mahindra'), ('Suzuki', 'Suzuki'), ('TVS', 'TVS'), ('Other', 'Other')], default='Other', max_length=100)),
            ],
            bases=('blog.twowheeler',),
        ),
    ]
