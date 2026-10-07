# region environment set up
#!/usr/bin/env python
### ! Do not edit ! ###
import os
import django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysoftwarecompany.settings")
django.setup()
# endregion

print("Django environment set up successfully.")

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

    # # exercise: loop through the employees and print out all the fields separately
    # for e in employees:
    #     print(f"{e.first_name} {e.last_name} was hired on {e.created_at.strftime('%B %d, %Y')} by {e.company}")

# 3. two ways to insert data into the database
# new_employees_data_acme = [
#     {
#         "first_name": "Alice",
#         "last_name": "Johnson",
#         "email": "alice.johnson@acmetesting.com",
#         "company": "Acme",
#     },
#     {
#         "first_name": "Bob",
#         "last_name": "Smith",
#         "email": "bob.smith@acmetesting.com",
#         "company": "Acme",
#     },
#     {
#         "first_name": "Charlie",
#         "last_name": "Brown",
#         "email": "charlie.brown@acmetesting.com",
#         "company": "Acme",
#     },

# ]
# # for the second part.
# new_employees_data_cat_sitting_int = [
#     {
#         "first_name": "Diana",
#         "last_name": "Prince",
#         "email": "diana.prince@catsittesting.com",
#         "company": "Cat Sitting International",
#         "role": "CEO",
#     },
#     {
#         "first_name": "Ethan",
#         "last_name": "Hunt",
#         "email": "ethan.hunt@catsittesting.com",
#         "company": "Cat Sitting International",
#         "role": "Manager",
#     },
#     {
#         "first_name": "Fiona",
#         "last_name": "Green",
#         "email": "fiona.green@catsittesting.com",
#         "company": "Cat Sitting International",
#         "role": "Developer",
#     },
# ]

# acme_company = Company.objects.get(name="Acme Inc.")
# new_employee_data = new_employees_data_acme[0]
# new_employee = Employee(
#     first_name=new_employee_data['first_name'],
#     last_name=new_employee_data['last_name'],
#     email=new_employee_data['email'],
#     company=acme_company  # Set the company to the acme_company instance
# )
# new_employee.save()
# Create a new employee using the create() method

# another_new_employee_data = new_employees_data_acme[1]  # Get the second employee data which is a dictionary.

# # you can use the create() method to create and save the employee in one step
# new_employee_two = Employee.objects.create(
#     first_name=another_new_employee_data['first_name'],
#     last_name=another_new_employee_data['last_name'],
#     email=another_new_employee_data['email'],
#     company=acme_company  # Set the company to the acme_company instance
# )
