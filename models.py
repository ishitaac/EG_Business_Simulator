from django.db import models

# Create your models here.

# LOCATION
from django.db import models

class Location(models.Model):
    country = models.CharField(max_length= 50)
    postalCode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.state}"


# DEPARTMENT
class Department(models.Model):
    # DATA_TEAM = 'Data Team'
    # MARKETING = 'Marketing'
    # FINANCE = 'Finance'
    # ENGINEERING = 'Engineering'
    # PRODUCT_MANAGEMENT = "Product Management"
    # COMPLAINCE = "Complaince"
    # HUMAN_RESOURCES = "Human Resources"
    # SALES ="Sales"
    # CUSTOMER_SERVICE = "Customer Service"
    
    # DEPARTMENT_CHOICES = [
    #     (DATA_TEAM, 'Data Team'),
    #     (MARKETING, 'Marketing'),
    #     (FINANCE,"Finance"),
    #     (ENGINEERING, 'Engineering'),
    #     (PRODUCT_MANAGEMENT, 'Product Management'),
    #     (COMPLAINCE, 'Complaince'),
    #     (HUMAN_RESOURCES, 'Human Resources'),
    #     (SALES, "Sales"),
    #     (CUSTOMER_SERVICE, "Customer_Service")
    # ]
    
    # name = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, unique=True)
    
    name = models.CharField(max_length=100, unique=True)
    department_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    

# JOB TABLE
class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

# EMPLOYEE TABLE
class Employee(models.Model):
    employee_id = models.CharField(max_length =50, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    job = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
# MANAGER MODEL
class Manager(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # employee_id = models.IntegerField(null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.OneToOneField('Department', on_delete=models.CASCADE)

    def __str__(self):
        return f"Manager - {self.first_name} {self.last_name}"
    
# PERFORMANCE TABLE: foreign key to employee
class Employee_Ratings(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    performance_rating = models.DecimalField(max_digits=3, decimal_places=2)
    numberCompaniesWorkedIn = models.DecimalField(max_digits=3, decimal_places=2)
    relationWithManager = models.DecimalField(max_digits=3, decimal_places=2)
    yearsAtCompany = models.DecimalField(max_digits=3, decimal_places=2)
    yearsSinceLastPromoted = models.DecimalField(max_digits=3, decimal_places=2)
    comments = models.TextField()

    def __str__(self):
        return f"Performance - {self.year} ({self.employee})"
    
