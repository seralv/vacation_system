from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, VacationViewSet, VacationReceiptViewSet

router = DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('vacations', VacationViewSet)
router.register('receipts', VacationReceiptViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
