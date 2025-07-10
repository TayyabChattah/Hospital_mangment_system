from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')
    ]
    # Store days as comma-separated string, or use a 3rd party MultiSelectField
    available_days = models.CharField(max_length=100)

    available_from = models.TimeField()
    available_to = models.TimeField()
    room_number = models.CharField(max_length=20)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'specialization', 'room_number'],
                name='unique_doctor'
            )
        ]

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
