# Generated by Django 3.2.7 on 2021-09-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AttendenceManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rollno', models.IntegerField()),
                ('course', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='faculty_registration',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
