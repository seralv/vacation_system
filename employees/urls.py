from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, VacationViewSet, VacationReceiptViewSet, VacationListByEmployee

router = DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('vacations', VacationViewSet)
router.register('receipts', VacationReceiptViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vacations/employee/<int:employee_id>/', VacationListByEmployee.as_view(), name='vacation-list-by-employee'),
]
