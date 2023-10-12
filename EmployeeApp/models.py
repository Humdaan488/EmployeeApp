from django.db import models

# Create your models here.
# each model maps to a single database table
# Each attribute of model represents a datbase field

# model to store department details
class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length= 500)

# model to store employee details
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

# We will use PostgreSQL as database to create tables from these models -> Connected Django App to postgreSQL using pip install psycopg2

