# region environment set up
#!/usr/bin/env python
### ! Do not edit ! ###
import os
import django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()
print("Django environment set up successfully.")
# endregion


from clients.models import Employee, Company

# 1. objects.all() and objects.filter - BOTH RETURN QUERYSETS
# companies = Company.objects.all()
# companies = Company.objects.filter(name="Acme Inc.")
# if companies:
#     company = companies[0]
#     print(company.email)
# else:
#     print("No companies to display.")
# 2. objects.get, filtering by passing a model, and looping through a queryset
# acme = Company.objects.get(name="Acme Inc.")
# print(acme)
# employees = Employee.objects.filter(company=acme)
# print(employees)
# # exercise: loop through the employees and print out all the fields separately
# for e in employees:
#     print(f"{e.first_name} {e.last_name} was hired on {e.created_at.strftime('%B %d, %Y')} by {e.company}")

# 3. two ways to insert data into the database
new_employees_data_acme = [
    {   "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@acmetesting.com",
        "company": "Acme",
    },
    {   "first_name": "Bob",
        "last_name": "Smith",
        "email": "bob.smith@acmetesting.com",
        "company": "Acme",
    },
    {   "first_name": "Charlie",
        "last_name": "Brown",
        "email": "charlie.brown@acmetesting.com",
        "company": "Acme",
    },

]
# for the second part.
new_employees_data_cat_sitting_int = [
    {
        "first_name": "Diana",
        "last_name": "Prince",
        "email": "diana.prince@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "CEO",
    },
    {
        "first_name": "Ethan",
        "last_name": "Hunt",
        "email": "ethan.hunt@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "Manager",
    },
    {
        "first_name": "Fiona",
        "last_name": "Green",
        "email": "fiona.green@catsittesting.com",
        "company": "Cat Sitting International",
        "role": "Developer",
    },
]

# part 2, #1, adding an employee by creating a Model object first
# new_employee_data = new_employees_data_acme[0]
# new_employee = Employee(
#     first_name="Alice",
#     last_name="Johnson",
#     email="alice.johnson@acmetesting.net",
#     company=acme_company  # Set the company to the acme_company instance
# )
# new_employee.save()

# part 2, #2, adding an employee the common way, using get_or_create
    # another_new_employee_data = new_employees_data_acme[1]  # Get the second employee data which is a dictionary.
    # acme_company = Company.objects.get(name="Acme Inc.")
    # # # you can use the create() method to create and save the employee in one step
    # new_employee_two, created = Employee.objects.get_or_create(
    #     first_name="Bob",
    #     last_name="Smith",
    #     email="bobbb@acme.com",
    #     company=acme_company  # Set the company to the acme_company instance
    # )
    # print(created)
# part 2, #3 adding a bunch of Roles using get_or_create in a loop
    # from clients.models import Role

    # roles_data = [
    #     {"name": "CEO", "description": "Chief Executive Officer"},
    #     {"name": "Manager", "description": "Manages a team of employees"},
    #     {"name": "Developer", "description": "Writes code and develops software"}
    # ]

    # for role_data in roles_data:
    #     role, created = Role.objects.get_or_create(
    #         name=role_data['name'],
    #         description=role_data['description']
    #     )
    #     if created:
    #         print(f"Created role: {role.name}")
    #     else:
    #         print(f"Role already exists: {role.name}")

# part 2, #4 assigning roles to employees
# Let's get the employees we created earlier
from clients.models import Employee, Role

# here we're filtering on the "name" field on the "company" model
# with the "company__name" lookup.
acme_employees = Employee.objects.filter(company__name="Acme Inc.")

# Let's get the roles we created earlier
roles = Role.objects.all()

# let's get the first employee and assign the ceo role to them

# Get the first employee, .first() returns first object in the QuerySet or None if no objects exist
first_employee = acme_employees.first()

role_ceo = roles.get(name="CEO")  # Get the CEO role

# let's update the first employee's role to the CEO role
first_employee.role = role_ceo
first_employee.save()  # Save the changes to the employee
# Let's print the first employee's role to verify
print(f"{first_employee.first_name} {first_employee.last_name} is now assigned the role of {first_employee.role.name}")
