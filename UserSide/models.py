from django.db import models

class Contact(models.Model):
    user_id = models.CharField(max_length=255)  # Store user ID as a string
    request = models.TextField()  # Store request details
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"{self.name} - {self.request}"
    
    class Meta:
        db_table = 'requests'


class Booking(models.Model):
    shop_id = models.CharField(max_length=255, default="Unknown Shop")  # Default value for shop_id
    user_id = models.CharField(max_length=255, default="Unknown User")  # Default value for user_id
    name = models.CharField(max_length=255, default="Anonymous")  # Default value for name
    phone_number = models.CharField(max_length=15, default="0000000000")  # Default phone number
    email = models.EmailField(max_length=255, default="unknown@example.com")  # Default email
    vehicle_model = models.CharField(max_length=255, default="Unknown Model")  # Default vehicle model
    vehicle_number = models.CharField(max_length=50, default="Unknown Number")  # Default vehicle number
    location = models.CharField(max_length=255, default="Unknown Location")  # Default location
    problem_description = models.TextField(blank=True, null=True, default="No description provided")  # Default problem description
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-sets timestamp when created

    class Meta:
        db_table = "bookings"  # Specify custom table name

    def __str__(self):
        return f"Booking for {self.vehicle_model} by {self.name} (User ID: {self.user_id})"
