from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=100)
    entry_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.last_name}"
    
class Vacation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Vacación para {self.employee}: {self.start_date} a {self.end_date}"
    
class VacationReceipt(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    vacation_days = models.PositiveIntegerField()
    receipt_date = models.DateField()

    def __str__(self):
        return f"Recibo de vacación para {self.employee}: {self.vacation_days} días."
