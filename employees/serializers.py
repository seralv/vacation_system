from rest_framework import serializers
from .models import Employee, Vacation, VacationReceipt

class EmployeeSerializer(serializers.ModelSerializer):
    is_on_vacation = serializers.BooleanField(read_only=True)
    remaining_vacation_days = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    def get_remaining_vacation_days(self, obj):
        return obj.remaining_vacation_days()

class VacationSerializer(serializers.ModelSerializer):
    remaining_vacation_days = serializers.SerializerMethodField()

    class Meta:
        model = Vacation
        fields = '__all__'

    def get_remaining_vacation_days(self, vacation):
        return vacation.employee.remaining_vacation_days()

class VacationReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationReceipt
        fields = '__all__'
