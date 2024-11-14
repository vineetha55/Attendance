from django.db import models

# Create your models here.
class tbl_Employees(models.Model):
    FullName = models.CharField(max_length=30, null=True)
    Address = models.TextField(null=True)
    Email_Id = models.EmailField(null=True)
    Contact_No = models.IntegerField(null=True)
    Emg_ContactNo = models.IntegerField(null=True)
    Date_Of_Birth = models.DateField(null=True)
    PassOut_Year = models.CharField(max_length=30, null=True)
    Qualification = models.CharField(max_length=50, null=True)
    photo = models.ImageField(upload_to="media", null=True)
    Aadhaar = models.FileField(null=True)
    Join_Date = models.DateField(null=True)
    Training_Start = models.DateField(null=True)
    Training_End = models.DateField(null=True)
    Work_Start = models.DateField(null=True)
    Work_End = models.DateField(null=True)
    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.FullName


class tbl_Experience(models.Model):
    employee = models.ForeignKey(tbl_Employees, related_name='experiences', on_delete=models.CASCADE)
    Exp_Company = models.CharField(max_length=100, null=True)
    Exp_Field = models.CharField(max_length=100, null=True)
    Exp_Start_Date = models.DateField(null=True)
    Exp_End_Date = models.DateField(null=True)
    Certificate_File = models.FileField(upload_to="experience_certificates/", null=True, blank=True)

    def __str__(self):
        return f"{self.Exp_Company} - {self.Exp_Field}"
    