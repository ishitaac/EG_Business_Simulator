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
from django.db import connection
import worker
from data.location import *
from faker.generator import Generator
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
class CustomFakerProvider(BaseProvider):
    # def postalCode(self, country):
    #     if country.lower() == 'canada':
    #         return random.choice(['A1A 1A1', 'B2B 2B2', 'C3C 3C3', 'D4D 4D4', 'E5E 5E5'])
    #     elif country.lower() == 'usa':
    #         return random.choice(['12345', '54321', '67890', '98765', '45678'])
    
    def city(self, provience):
        result = random.choices([i[0] for i in locations[provience]], [i[1] for i in locations[provience]])
        return result
    

        # random.choice(i[0] for i in locations[provience])
    # def population
    # def population(self, provience):
    #     return random.choices([i[0] for i in locations[provience]], weights=[i[1] for i in locations[provience]], k=1)[0]

    # def city(self, provience):
    #     if provience.lower() == 'ontario':
    #         return random.choice(ontario)
    #     elif provience.lower() == 'quebec':
    #         return random.choice(quebec)
    #     elif provience.lower() == 'alberta':
    #         return random.choice(alberta)
    #     elif provience.lower() == 'british columbia':
    #         return random.choice(britishColumbia)
    #     elif provience.lower() == 'manitoba':
    #         return random.choice(manitoba)
    #     elif provience.lower() == 'nova scotia':
    #         return random.choice(novaScotia)
    #     elif provience.lower() == 'Saskatchewan':
    #         return random.choice(saskatchewan)
    #     elif provience.lower() == 'newfoundland and labrador':
    #         return random.choice(newfoundland)
    #     elif provience.lower() == 'new brunswick':
    #         return random.choice(new_Brunswick)
    #     elif provience.lower() == 'prince edward island':
    #         return random.choice(princeEdward)
    #     elif provience.lower() == 'Alberta / Saskatchewan':
    #         return random.choice(alberta_Saskatchewan)
    #     elif provience.lower() == 'ontario / quebec':
    #         return random.choice(ontarioQuebec)
            
            

    # without writing so much code: 
    # def __init__(self, generator: Generator):
    #     super().__init__(generator)
    #     self.generated_cities = {}

    # def city(self, province):
    #         if province in self.generated_cities:
    #             return self.generated_cities[province]
    #         else:
    #             return f"No city generated for {province}"

    # def generate_city(self, province):
    #         if province.lower() == 'ontario':
    #             self.generated_cities[province] = random.choice(ontario)
    #         elif province.lower() == 'quebec':
    #             self.generated_cities[province] = random.choice(quebec)
    #         elif province.lower() == 'alberta':
    #             self.generated_cities[province] = random.choice(alberta)
    #         elif province.lower() == 'british columbia':
    #             self.generated_cities[province] = random.choice(britishColumbia)
    #         elif province.lower() == 'manitoba':
    #             self.generated_cities[province] = random.choice(manitoba)
    #         elif province.lower() == 'nova scotia':
    #             self.generated_cities[province] = random.choice(novaScotia)
    #         elif province.lower() == 'saskatchewan':
    #             self.generated_cities[province] = random.choice(saskatchewan)
    #         elif province.lower() == 'newfoundland and labrador':
    #             self.generated_cities[province] = random.choice(newfoundland)
    #         elif province.lower() == 'new brunswick':
    #             self.generated_cities[province] = random.choice(new_Brunswick)
    #         elif province.lower() == 'prince edward island':
    #             self.generated_cities[province] = random.choice(princeEdward)
    #         elif province.lower() == 'alberta / saskatchewan':
    #             self.generated_cities[province] = random.choice(alberta_Saskatchewan)
    #         elif province.lower() == 'ontario / quebec':
    #             self.generated_cities[province] = random.choice(ontarioQuebec)
    #         else:
    #             return f"No data for province {province}"

    #         return self.generated_cities[province]
    
    # def population(self, province):
    #     generated_city = self.city(province)
        
    #     if generated_city != f"No city generated for {province}":
    #         city_data = locations.get(province, [])
    #         for city_tuple in city_data:
    #             if city_tuple[0] == generated_city:
    #                 return city_tuple[1]
            
    #         return f"No data for province {province} and city {generated_city}"
        
    #     return f"No data for province {province}"

    
    




    # def population(self,city):
    #     if provience.lower() == 'ontario':
    #         return random.choice(ontario)
    #     elif provience.lower() == 'quebec':
    #         return random.choice(quebec)
    #     elif provience.lower() == 'alberta':
    #         return random.choice(alberta)
    #     elif provience.lower() == 'british columbia':
    #         return random.choice(britishColumbia)
    #     elif provience.lower() == 'manitoba':
    #         return random.choice(manitoba)
    #     elif provience.lower() == 'nova scotia':
    #         return random.choice(novaScotia)
    #     elif provience.lower() == 'Saskatchewan':
    #         return random.choice(saskatchewan)
    #     elif provience.lower() == 'newfoundland and labrador':
    #         return random.choice(newfoundland)
    #     elif provience.lower() == 'new brunswick':
    #         return random.choice(new_Brunswick)
    #     elif provience.lower() == 'prince edward island':
    #         return random.choice(princeEdward)
    #     elif provience.lower() == 'Alberta / Saskatchewan':
    #         return random.choice(alberta_Saskatchewan)
    #     elif provience.lower() == 'ontario / quebec':
    #         return random.choice(ontarioQuebec)

    # def city(self, country):
    #     if country.lower() == 'canada':
    #         return random.choice(['Toronto', 'Montreal', 'Vancouver', 'Calgary', 'Ottawa'])
    #     elif country.lower() == 'usa':
    #         return random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'])

    # def state(self, city):
    #     if city.lower() in ['toronto', 'ottawa']:
    #         return 'Ontario'
    #     elif city.lower() =="montreal":
    #         return 'Quebec'
    #     elif city.lower() == 'calgary':
    #         return 'Alberta'
    #     elif city.lower() == 'vancouver':
    #         return 'British Columbia'
    #     elif city.lower() == 'miami':
    #         return 'Florida'
    #     elif city.lower() == 'new york':
    #         return 'New York state'
    #     elif city.lower() == 'chicago':
    #         return 'Illnois'
    #     elif city.lower() == 'los angeles':
    #         return 'California'
    #     elif city.lower() == 'houston':
    #         return 'Texas'



# Location Factory
class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    # country = factory.Faker('random_element', elements=['Canada', 'USA'])
    # postalCode = factory.LazyAttribute(lambda obj: CustomFakerProvider().postalCode(obj.country))
    # city = factory.LazyAttribute(lambda obj: CustomFakerProvider().city(obj.country))
    # state = factory.LazyAttribute(lambda obj: CustomFakerProvider().state(obj.city))

    provience = factory.Faker('random_element', elements= province)
    city = factory.LazyAttribute(lambda obj: CustomFakerProvider().city(obj.provience))
    population = factory.LazyAttribute(lambda obj: CustomFakerProvider().city(obj.provience))
    # # # population = factory.Faker('random_int', min=100000, max=10000000)
    # @factory.lazy_attribute
    # def city(self):
    #     return CustomFakerProvider(self.generator).city(self.provience)

    # @factory.lazy_attribute
    # def population(self):
    #     return CustomFakerProvider(self.generator).city_population(self.provience)

    # @classmethod
    # def _get_generator(cls):
    #     return cls._meta.declarations.get('generator', None)


# class LocationFactory(factory.django.DjangoModelFactory):
#     class Meta:

#         model = Location
    

#     @classmethod
#     def create(cls):
        # Execute the SQL query to fetch location data
        # with connection.cursor() as cursor:
        #     cursor.execute("SELECT Population_Center, Province, Population_2021 FROM mdm.raw_wikipedia_canada_cities")
        #     location_data = cursor.fetchall()
        # if __name__ == "__main__":
        #     stmt = """
        #     # SELECT Populta FROM raw_wikipedia_canada_cities;
        #     `Population center` AS population_center, `Province` AS province, `Size Group` AS size_group
        #     """
        #     import mysql.connector
        #     from mysql.connector import errorcode

        #     try:
        #         cnx = mysql.connector.connect(host='gta-ins07.fadm.usherbrooke.ca', port='3307', user='choi1602', password='L5_lb*_NLTK',
        #                                         database='mdm')
        #         cur = cnx.cursor()
        #         msg = cur.execute(stmt)
        #         rs = cur.fetchall()
        #         # for i in rs:
        #         #     print(i)

        #     except mysql.connector.Error as err:
        #         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        #             print("Something is wrong with your user name or password")
        #         elif err.errno == errorcode.ER_BAD_DB_ERROR:
        #             print("Database does not exist")
        #         else:
        #             print(err)
        #     else:
        #         cnx.close()
        
        # using the exact module from the worker factory - get the fetched data

        # Create a Location instance using the fetched data
        # return cls(
        #     city=rs[0],
        #     provience=rs[1],
        #     population=rs[2],
        # )


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

# JOB FACTORY
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

from factory import SubFactory, LazyAttribute
from .models import Manager, Employee, Department

class ManagerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Manager

    # Use LazyAttribute to assign an existing employee to each manager record
    employee = LazyAttribute(lambda obj: Employee.objects.order_by('?').first())

    # Use LazyAttribute to ensure only one manager is created per department
    department = LazyAttribute(lambda obj: Department.objects.order_by('?').first())

    @factory.lazy_attribute
    def first_name(self):
        return self.employee.first_name

    @factory.lazy_attribute
    def last_name(self):
        return self.employee.last_name

    @factory.lazy_attribute
    def email(self):
        return self.employee.email

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
