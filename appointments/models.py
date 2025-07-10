from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        return f"{self.patient.name} with Dr. {self.doctor.name} on {self.appointment_date}"

    class Meta:
        unique_together = ['doctor', 'appointment_date', 'appointment_time']
        ordering = ['appointment_date', 'appointment_time']
