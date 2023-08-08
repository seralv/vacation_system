from django.db import models
import datetime

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

    @property
    def is_on_vacation(self):
        today = datetime.date.today()
        return Vacation.objects.filter(employee=self, start_date__lte=today, end_date__gte=today).exists()
    
    def remaining_vacation_days(self):
        today = datetime.date.today()
        years_of_service = (today - self.entry_date).days // 365

        past_vacations = Vacation.objects.filter(
            employee=self,
            end_date__lt=today,
        )

        past_vacation_days = sum((vacation.end_date - vacation.start_date).days + 1 for vacation in past_vacations)

        if 1 <= years_of_service <= 5:
            return 15 - past_vacation_days
        elif 6 <= years_of_service <= 10:
            return 20 - past_vacation_days
        else:
            return 30 - past_vacation_days
    
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
