import factory
from factory.faker import faker
import faker.providers
from .models import *
import factory.random
from factory.fuzzy import FuzzyDecimal
from faker.providers import BaseProvider
import random
import string
from factory import SubFactory
from datetime import datetime, timedelta
from factory.fuzzy import FuzzyDecimal


FAKE = faker.Faker()


import factory
from factory import Faker, Factory, SubFactory, LazyAttribute
from .models import Department, Location, Job, Employee_Ratings, Employee, Manager
from factory.faker import Faker as FactoryFaker
from faker import Faker
from factory.faker import Faker

# DATABASES

DEPARTMENTS = [
    "Product",
    "Business Operations",
    "Marketing",
    "Human Resources",
    "Finance & Accounting",
    "Sales",
    "Tech & Engineering",
    "Customer Service",
    "Data Science",
    "Legal & Complaince",
]


    
# PROVIDER FOR LOCATION
import factory
from factory.faker import Faker as FactoryFaker
from .models import Location


# PROVIDER FOR EMAIL
class CustomFakerProvider:
    def custom_email(self, first_name, last_name):
        first_name = first_name.lower()
        last_name = last_name.lower()
        domain = "walmart.com"  # You can change this to your desired domain
        return f"{first_name}.{last_name}@{domain}"
    
# Custom Provider FOR CITIES
class CustomFakerProvider:
    def postalCode(self, country):
        if country.lower() == 'canada':
            return random.choice(['A1A 1A1', 'B2B 2B2', 'C3C 3C3', 'D4D 4D4', 'E5E 5E5'])
        elif country.lower() == 'usa':
            return random.choice(['12345', '54321', '67890', '98765', '45678'])

    def city(self, country):
        if country.lower() == 'canada':
            return random.choice(['Toronto', 'Montreal', 'Vancouver', 'Calgary', 'Ottawa'])
        elif country.lower() == 'usa':
            return random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'])

    def state(self, city):
        if city.lower() in ['toronto', 'ottawa']:
            return 'Ontario'
        elif city.lower() =="montreal":
            return 'Quebec'
        elif city.lower() == 'calgary':
            return 'Alberta'
        elif city.lower() == 'vancouver':
            return 'British Columbia'
        elif city.lower() == 'miami':
            return 'Florida'
        elif city.lower() == 'new york':
            return 'New York state'
        elif city.lower() == 'chicago':
            return 'Illnois'
        elif city.lower() == 'los angeles':
            return 'California'
        elif city.lower() == 'houston':
            return 'Texas'



# Location Factory
# class LocationFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Location

#     country = factory.Faker('random_element', elements=['Canada', 'USA'])
#     postalCode = factory.LazyAttribute(lambda obj: CustomFakerProvider().postalCode(obj.country))
#     city = factory.LazyAttribute(lambda obj: CustomFakerProvider().city(obj.country))
#     state = factory.LazyAttribute(lambda obj: CustomFakerProvider().state(obj.city))
# previous code

class LocationFaction(factory.django.DjangoModelFactory):
    class Meta:
        model = Location
    
    city = factory.Faker('city')
    province = factory.Faker('state')
    population = factory.Faker('random_int', min=1000, max=1000000)
    

# DEPARTMENT FACTORY

DEPARTMENT_CODES = {
    "Product": "PROD-124",
    "Business Operations": "OPS-567",
    "Marketing": "MKT-789",
    "Human Resources": "HR-345",
    "Finance & Accounting": "FIN-637",
    "Sales": "SALE-290",
    "Tech & Engineering": "ENG-852",
    "Customer Service": "CS-505",
    "Data Science": "DATA-606",
    "Legal & Complaince": "LEGAL-707",
}
class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department
        
    name = factory.Iterator(DEPARTMENT_CODES.keys())
    department_code = factory.LazyAttribute(lambda obj: DEPARTMENT_CODES[obj.name])


class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Job

    title = factory.Iterator([
        "Data Scientist",
        "Data Analyst",
        "Data Engineer",
        "Sr. Data Scientist",
        "Database Engineer",
        "Database Administrator",
        "Manager",
        "Associate",
        "Social Media Specialist",
        "Finance Analyst",
        "Auditor",
        "Purchase Officer",
        "Risk Analyst",
        "Sr. Finance Officer",
        "Software Developer",
        "ML Engineer",
        "Android Developer",
        "iOS Developer",
        "DevOps",
        "Cloud Architect",
        "Systems Engineer",
        "Associate PM",
        "Technical Product Manager",
        "Scrum Master",
        "Product Analyst",
        "Product Manager I",
        "Product Manager II",
        "Program Manager",
        "Business Compliance Officer",
        "Financial Service Compliance Officer",
        "Admin",
        "HR Generalist",
        "Employee Relation Manager",
        "HR Executive",
        "Sales Associate",
        "Sales Consultant",
        "Retail Sales Consultant",
        "Sales Representative",
        "Account Executive",
        "Business Development Specialist",
        "Client Success Officer",
        "Associate Customer Care Representative",
        # Add more titles as needed
    ])
    description = factory.Faker('sentence')
# EMPLOYEE FACTORY

def random_letters(length):
        letters = string.ascii_uppercase
        return ''.join(random.choice(letters) for _ in range(length))

class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    # employee_id = factory.Sequence(lambda n: n)  # Generates a unique employee_id
    employee_id = factory.Sequence(lambda n: f"EMP - {random_letters(2)}{n:02}{random_letters(2)}")
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = LazyAttribute(lambda obj: f"{obj.first_name.lower()}.{obj.last_name.lower()}@walmart.com")
    # department = models.ForeignKey(Department, to_field='department_code', on_delete=models.CASCADE)
    # department = factory.SubFactory(DepartmentFactory)
    location = factory.SubFactory(LocationFactory)
    hire_date = Faker('date_this_decade')
    salary = FuzzyDecimal(40000.12, 150000.0, precision=2)
    
    @factory.lazy_attribute
    def department(self):
        # Assuming you have departments with unique names in your database
        return Department.objects.order_by('?').first()
    
    @factory.lazy_attribute
    def job(self):
        department_name = self.department.name.lower().split()
        print(f"Department Name: {department_name}")

        # Define custom job titles based on department
        if 'data' in department_name:
            return Job.objects.create(title=random.choice([
                "Data Scientist",
                "Data Analyst",
                "Data Engineer",
                "Sr. Data Scientist",
                "Database Engineer",
                "Database Administrator",
            ]))
        elif 'marketing' in department_name:
            return Job.objects.create(title=random.choice([
                "Manager",
                "Associate",
                "Social Media Specialist",
            ]))
        elif 'finance' in department_name:
            return Job.objects.create(title=random.choice([
                "Finance Analyst",
                "Auditor",
                "Purchase Officer",
                "Risk Analyst",
                "Sr. Finance Officer",
            ]))
        elif 'engineering' in department_name:
            return Job.objects.create(title=random.choice([
                "Software Developer",
                "ML Engineer",
                "Android Developer",
                "iOS Developer",
                "DevOps",
                "Cloud Architect",
                "Systems Engineer",
            ]))
        elif 'product' in department_name:
            return Job.objects.create(title=random.choice([
                "Associate PM",
                "Technical Product Manager",
                "Scrum Master",
                "Product Analyst",
                "Product Manager I",
                "Product Manager II",
                "Program Manager",
            ]))
        elif 'compliance' in department_name:
            return Job.objects.create(title=random.choice([
                "Business Compliance Officer",
                "Financial Service Compliance Officer",
            ]))
        elif 'human' in department_name:
            return Job.objects.create(title=random.choice([
                "Admin",
                "HR Generalist",
                "Employee Relation Manager",
                "HR Executive",
            ]))
        elif 'sales' in department_name:
            return Job.objects.create(title=random.choice([
                "Sales Associate",
                "Sales Consultant",
                "Retail Sales Consultant",
                "Sales Representative",
                "Account Executive",
                "Business Development Specialist",
            ]))
        elif 'customer' in department_name:
            return Job.objects.create(title=random.choice([
                "Client Success Officer",
                "Associate Customer Care Representative",
            ]))
        else:
            return Job.objects.create(title="Default Job Title")

# ---- prev code----
  # @factory.lazy_attribute
    # def job(self):
    #     # Generate job based on department
    #     department_name = self.department.name.lower()
    #     if 'data' in department_name:
    #         return factory.Faker('random_element', elements=["Data Scientist", "Data Analyst", "Data Engineer", "Sr. Data Scientist","Database Engineer", "Database Administrator"])
    #     elif 'marketing' in department_name:
    #         return factory.Faker('random_element', elements=["Manager", "Associate", "Social Media Specialist"])
    #     elif 'finance' in department_name:
    #         return factory.Faker('random_element', elements=["Finance Analyst", "Auditor","Purchase Officer","Risk Analyst", "Sr. Finance Officer"])
    #     elif 'Engineering' in department_name:
    #         # Set job profiles for Finance
    #         self.job = Job.objects.get(title__in=["Software Developer", "ML Engineer", "Android Developer", "ios Developer", "DevOps","Cloud Architect", "Systems Engineer"])
    #     elif 'product' in department_name:
    #         # Set job profiles for Finance
    #         self.job = Job.objects.get(title__in=["Associate PM", "Technical Product Manager", "Scrum Master","Product Analyst","Product Manager I","Product Manager II", "Program Manager"])
    #     elif 'complaince' in department_name:
    #         # Set job profiles for Finance
    #         self.job = Job.objects.get(title__in=["Business Complaince Officer","Financial Service Complaince Officer"])
    #     elif 'human' in department_name:
    #         # Set job profiles for Finance
    #         self.job = Job.objects.get(title__in=["Admin","HR Generalist", "Employee Relation manager", "HR Executive"])
    #     elif 'sales' in department_name:
    #         # Set job profiles for Finance
    #         self.job = Job.objects.get(title__in=["Sales Associate", "Sales Consultant","Retail Sales Consultant","Sales Representative", "Account Executive", "Business Development Specialist"])
    #     elif 'customer' in department_name:
    #         # Set job profiles for Finance
    #         self.job = Job.objects.get(title__in=["Client Success Officer", "Associate Customer Care Representative"])
# ----------------------

# MANAGER FACTORY

from factory import SubFactory
from .models import Manager

# class ManagerFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Manager

#     # You can use a SubFactory to create an Employee and use its data for the Manager
#     employee = factory.SubFactory(EmployeeFactory)  # Assuming EmployeeFactory is defined correctly
#     first_name = factory.SelfAttribute('employee.first_name')
#     last_name = factory.SelfAttribute('employee.last_name')
#     email = factory.SelfAttribute('employee.email')
#     department = factory.Iterator(Department.objects.all())  # Choose a department for the manager

#     # If you want to ensure the manager has the same employee ID as the associated employee,
#     # you can do it like this:
#     @classmethod
#     def create(cls, **kwargs):
#         manager = super().create(**kwargs)
#         manager.employee_id = manager.employee.employee_id
#         manager.save()
#         return manager

# # class ManagerFactory(factory.django.DjangoModelFactory):
# #     class Meta:
# #         model = Manager

# #     employee = factory.SubFactory(EmployeeFactory)
# #     department = factory.SubFactory(DepartmentFactory)

class PerformanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee_Ratings

    # Use LazyAttribute to assign an existing employee to each performance record
    employee = LazyAttribute(lambda obj: Employee.objects.order_by('?').first())

    year = factory.Faker('year')
    performance_rating = LazyAttribute(lambda obj: round(random.uniform(1.0, 5.0), 2))
    numberCompaniesWorkedIn = LazyAttribute(lambda obj: round(random.uniform(1.0, 5.0), 2))
    relationWithManager = LazyAttribute(lambda obj: round(random.uniform(1.0, 5.0), 2))
    yearsAtCompany = LazyAttribute(lambda obj: round(random.uniform(1.0, 5.0), 2))
    yearsSinceLastPromoted = LazyAttribute(lambda obj: round(random.uniform(1.0, 5.0), 2))
    comments = factory.Faker('text')