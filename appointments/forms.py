from django import forms
from django.core.exceptions import ValidationError
from .models import Appointment
from doctors.models import Doctor
import datetime

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get('doctor')
        date = cleaned_data.get('appointment_date')
        time = cleaned_data.get('appointment_time')

        if doctor and date and time:
            # Check if date is in doctor's available days
            weekday = date.strftime('%a')
            if weekday not in doctor.available_days.split(','):
                raise ValidationError(f"Doctor is not available on {date.strftime('%A')}")
            
            # Check time against doctor's availability
            if time < doctor.available_from or time > doctor.available_to:
                raise ValidationError(
                    f"Doctor only available between {doctor.available_from.strftime('%H:%M')} "
                    f"and {doctor.available_to.strftime('%H:%M')}"
                )
            
            # Check for existing appointments
            if Appointment.objects.filter(
                doctor=doctor,
                appointment_date=date,
                appointment_time=time
            ).exists():
                raise ValidationError("This time slot is already booked")
        
        return cleaned_data
