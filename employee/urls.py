# employee/urls.py
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
# Register the ViewSet, this creates:
# /employees/ (GET, POST)
# /employees/{id}/ (GET, PUT, PATCH, DELETE)
router.register(r"employees", EmployeeViewSet)

urlpatterns = router.urls
