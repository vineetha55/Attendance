# Generated by Django 4.1.5 on 2024-10-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_registration',
            name='created_at',
            field=models.DateField(null=True),
        ),
    ]
