# Generated by Django 3.0.3 on 2020-04-19 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20200419_1255'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.EnrolledStudent'),
        ),
    ]
