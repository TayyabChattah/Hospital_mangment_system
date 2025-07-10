from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
