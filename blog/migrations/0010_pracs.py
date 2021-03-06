# Generated by Django 3.0.5 on 2020-05-06 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_quespaper_exam_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pracs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('starred', models.BooleanField(default=False)),
                ('academic_year', models.CharField(choices=[('FY', 'I'), ('SY', 'II'), ('TY', 'III'), ('BE', 'IV')], default='I', max_length=100)),
                ('branch', models.CharField(choices=[('CS', 'CS'), ('Mech', 'Mech'), ('ENTC', 'ENTC'), ('IT', 'IT'), ('CHEM', 'CHEM'), ('ETX', 'ETX'), ('Civil', 'Civil'), ('FY', 'FY')], default='CS', max_length=100)),
                ('sub', models.CharField(choices=[('NO SUBJECT', 'NO SUBJECT'), ('DSF', 'Data Structures And Files'), ('DSGT', 'Data Structures and Graph Theory'), ('AM2', 'Applied Mathematcs'), ('AM1', 'Applied Mechanics'), ('EI', 'Engineering Informatics'), ('DBMS', 'DBMS'), ('SYSTEM ENGG', 'SYSTEM ENGG'), ('MATHS', 'MATHS'), ('PSYCHO', 'PSYCHO'), ('MATERIAL ENGG', 'MATERIAL ENGG'), ('PYTHON', 'PYTHON'), ('CPP', 'CPP'), ('EEE', 'EEE'), ('None', 'none')], default='NO SUBJECT', max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=100)),
                ('pracs_author', models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student'), ('other', 'Other')], default='Anonymous', max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('fileMy', models.FileField(blank=True, upload_to='Pracs')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
