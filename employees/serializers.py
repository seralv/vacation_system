from rest_framework import serializers
from .models import Employee, Vacation, VacationReceipt

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = '__all__'

class VacationReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationReceipt
        fields = '__all__'
