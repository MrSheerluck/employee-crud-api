# employee/models.py
from django.db import models


class Employee(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Work Details (useful for filtering/sorting)
    position = models.CharField(
        max_length=100, help_text="e.g., Software Engineer, HR Manager"
    )
    department = models.CharField(max_length=100, help_text="e.g., Technology, Finance")
    hire_date = models.DateField()
    salary = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Suitable for sorting

    # Profile Image (Requires MEDIA_URL and MEDIA_ROOT setup in settings.py)
    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
        help_text="Upload employee profile image",
    )

    # Automatically set fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Define the default sorting order
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"
