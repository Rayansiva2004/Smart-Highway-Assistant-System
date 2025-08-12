from django.db import models

class Bill(models.Model):
    user_id = models.CharField(max_length=255, default="UNKNOWN_USER")  # Default user ID
    booking_user_id = models.CharField(max_length=255, default="UNKNOWN_BOOKING_USER")  # Default booking user ID
    entry_id = models.IntegerField(default=0)  # Default entry ID as 0
    bill_data = models.JSONField(default=list)  # Default to an empty list
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Default to 0.00

    def __str__(self):
        return f"Bill for Entry ID: {self.entry_id}"

    class Meta:
        db_table = "bills"
