# Generated by Django 5.1.2 on 2024-11-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance_app', '0002_tbl_registration_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=30, null=True)),
                ('Address', models.TextField(null=True)),
                ('Email_Id', models.EmailField(max_length=254, null=True)),
                ('Contact_No', models.IntegerField(null=True)),
                ('Emg_ContactNo', models.IntegerField(null=True)),
                ('Date_Of_Birth', models.DateField(null=True)),
                ('PassOut_Year', models.CharField(max_length=30, null=True)),
                ('Qualification', models.CharField(max_length=50, null=True)),
                ('Exp_Company', models.CharField(max_length=100, null=True)),
                ('Exp_Field', models.CharField(max_length=100, null=True)),
                ('photo', models.ImageField(null=True, upload_to='media')),
                ('Aadhaar', models.FileField(null=True, upload_to='')),
                ('Join_Date', models.DateField(null=True)),
                ('Training_Start', models.DateField(null=True)),
                ('Training_End', models.DateField(null=True)),
                ('Work_Start', models.DateField(null=True)),
                ('Work_End', models.DateField(null=True)),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
                ('Updated_At', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TBL_FlutterStudents',
        ),
        migrations.DeleteModel(
            name='TBL_Registration',
        ),
    ]
