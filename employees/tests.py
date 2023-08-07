import datetime
import unittest
from django.test import TestCase
from .models import Employee, Vacation

class EmployeeTestCase(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create(
            name="John",
            last_name="Doe",
            address="123 Main St",
            phone="555-1234",
            position="Manager",
            entry_date=datetime.date(2020, 1, 1)
        )

    def test_is_on_vacation(self):
        # Crea un período de vacaciones para el empleado en la fecha actual
        today = datetime.date.today()
        vacation = Vacation.objects.create(
            employee=self.employee,
            start_date=today - datetime.timedelta(days=1),
            end_date=today + datetime.timedelta(days=1)
        )

        # Verifica si el método is_on_vacation devuelve True
        self.assertTrue(self.employee.is_on_vacation)

        # Elimina el período de vacaciones
        vacation.delete()

        # Verifica si el método is_on_vacation devuelve False
        self.assertFalse(self.employee.is_on_vacation)

    def test_not_on_vacation(self):
        # Verifica que el método is_on_vacation devuelva False si no hay período de vacaciones
        self.assertFalse(self.employee.is_on_vacation)

if __name__ == '__main__':
    unittest.main()
