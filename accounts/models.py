

# Create your models here.
from django.db import models

# Create your models here.
class Studentdbs(models.Model):
    
    name=models.CharField(max_length=100);
    img=models.ImageField(upload_to="pics");
    registernumber=models.IntegerField();
    phonenumber=models.BigIntegerField();
    dob=models.DateField()
    department=models.CharField(max_length=25);
    Staffname=models.CharField(max_length=100);
    Mail=models.CharField(max_length=32);
    Password=models.CharField(max_length=8);
    def __str__(self):
        return self.name
    

class Staffdbs(models.Model):
    staffname=models.CharField(max_length=100);
    img=models.ImageField(upload_to="pics");
    staffid=models.IntegerField();
    Gender=models.CharField(max_length=10);
    Department=models.CharField(max_length=15);
    Mail=models.CharField(max_length=50);
    phonenumber=models.BigIntegerField();
    Password=models.CharField(max_length=8);
    def __str__(self):
        return self.staffname
    
    

class Admindbs(models.Model):
    institutename=models.CharField(max_length=50);
    instituteid=models.IntegerField(); 
    photo=models.ImageField(upload_to="pics");
    Mail=models.CharField(max_length=30);
    Password=models.CharField(max_length=8);
    def __str__(self):
        return self.institutename
    
class AttendanceDetails(models.Model):
    registernumber=models.IntegerField();
    Date=models.DateField(auto_now=True);
    Staffname=models.CharField(max_length=20);
    Status=models.CharField(max_length=10);
    def __str__(self):
        return str(self.registernumber)

'''class staff_name(models.Model):
    staffname=models.CharField(max_length=100)
    def __str__(self):
        return str(self.staffname)
    

class department(models.Model):
    department=models.ForeignKey(staff_name,models.CASCADE)
    staffname=models.CharField(max_length=40)

    def __str__(self):
        return self.department'''

    


    
    








