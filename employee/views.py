# employee/views.py
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeSerializer


# --- Custom Pagination ---
class StandardResultsSetPagination(PageNumberPagination):
    # Number of items per page
    page_size = 10
    # Optional: allows client to override page size up to a max
    page_size_query_param = "page_size"
    max_page_size = 100


# --- Employee ViewSet (CRUD, Filtering, Sorting, Pagination) ---
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = StandardResultsSetPagination  # 1. Pagination

    # 2. Filtering and Sorting Backend Setup
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Enable filtering by specific fields
    filterset_fields = ["department", "position", "hire_date"]

    # Enable searching across these fields
    search_fields = ["first_name", "last_name", "email", "department", "position"]

    # Enable ordering (sorting) by these fields. Defaults to the model's Meta ordering.
    ordering_fields = ["last_name", "hire_date", "salary"]

    # Default ordering if none is provided in the URL query parameters
    ordering = ["last_name"]
