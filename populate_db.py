import os
from django.core.wsgi import get_wsgi_application
from datetime import date, timedelta
from faker import Faker
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vacation_system.settings")
application = get_wsgi_application()

from employees.models import Employee, Vacation, VacationReceipt

fake = Faker()

def create_employees(num_employees):
    employees = []
    for _ in range(num_employees):
        name = fake.first_name()
        last_name = fake.last_name()
        address = fake.address()
        phone = fake.phone_number()[:20]
        position = fake.job()
        entry_date = fake.date_between(start_date="-2y", end_date="today")
        
        employee = Employee(name=name, last_name=last_name, address=address, phone=phone, position=position, entry_date=entry_date)
        employees.append(employee)
    Employee.objects.bulk_create(employees)

def assign_vacations_and_receipts():
    employees = Employee.objects.all()
    for employee in employees:
        start_date = fake.date_between_dates(date_start=employee.entry_date, date_end=date.today())
        end_date = start_date + timedelta(days=random.randint(5, 15))
        vacation = Vacation(employee=employee, start_date=start_date, end_date=end_date)
        vacation.save()

        receipt_date = end_date + timedelta(days=random.randint(1, 5))
        vacation_days = (end_date - start_date).days
        receipt = VacationReceipt(employee=employee, vacation_days=vacation_days, receipt_date=receipt_date)
        receipt.save()

if __name__ == "__main__":
    num_employees = 20
    create_employees(num_employees)
    assign_vacations_and_receipts()
    print(f"{num_employees} employees created with vacations and vacation receipts.")
