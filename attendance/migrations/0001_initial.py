# Generated by Django 3.0.2 on 2020-01-28 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('academic', '0002_auto_20200128_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic.ClassRegistration')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.EnrolledStudent')),
            ],
            options={
                'unique_together': {('student', 'date')},
            },
        ),
    ]
