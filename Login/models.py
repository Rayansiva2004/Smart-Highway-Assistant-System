from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=20, unique=True)  # Add user_id field
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    # Extra fields renamed to attribute1 to attribute5
    attribute1 = models.CharField(max_length=255, null=True, blank=True)
    attribute2 = models.CharField(max_length=255, null=True, blank=True)
    attribute3 = models.CharField(max_length=255, null=True, blank=True)
    attribute4 = models.CharField(max_length=255, null=True, blank=True)
    attribute5 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'users'
