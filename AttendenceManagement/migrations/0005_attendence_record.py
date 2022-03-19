# Generated by Django 3.2.7 on 2021-10-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AttendenceManagement', '0004_student_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('date', models.DateField()),
                ('faculty', models.CharField(max_length=50)),
                ('status', models.CharField(default='Absent', max_length=50)),
            ],
        ),
    ]
