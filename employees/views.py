from datetime import timedelta
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Employee, Vacation, VacationReceipt
from .serializers import EmployeeSerializer, VacationSerializer, VacationReceiptSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class VacationViewSet(viewsets.ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer

    def perform_create(self, serializer):
        employee = serializer.validated_data['employee']
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']

        # Check if the employee has taken vacation in the past
        past_vacations = Vacation.objects.filter(
            employee=employee,
            end_date__lt=timezone.now().date()  # Only consider past vacations
        )

        # Sum the days of past vacations
        past_vacation_days = sum((vacation.end_date - vacation.start_date).days + 1 for vacation in past_vacations)

        # Calculate the remaining vacation days based on the employee's years of service
        remaining_vacation_days = 0
        years_of_service = (timezone.now().date() - employee.entry_date).days // 365
        if 1 <= years_of_service <= 5:
            remaining_vacation_days = 15 - past_vacation_days
        elif 6 <= years_of_service <= 10:
            remaining_vacation_days = 20 - past_vacation_days
        else:
            remaining_vacation_days = 30 - past_vacation_days

        # Check if the requested vacation days exceed the remaining days
        requested_vacation_days = (end_date - start_date).days + 1
        if requested_vacation_days > remaining_vacation_days:
            raise Exception("Not enough remaining vacation days for this employee.")

        serializer.save()

class VacationReceiptViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VacationReceipt.objects.all()
    serializer_class = VacationReceiptSerializer
