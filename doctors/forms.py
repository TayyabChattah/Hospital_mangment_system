from django import forms
from django.core.exceptions import ValidationError
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'available_from': forms.TimeInput(attrs={'type': 'time'}),
            'available_to': forms.TimeInput(attrs={'type': 'time'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        
        # Check time validation
        available_from = cleaned_data.get('available_from')
        available_to = cleaned_data.get('available_to')
        
        if available_from and available_to and available_from >= available_to:
            raise forms.ValidationError("Available 'From' time must be before 'To' time")
        
        # Check for existing doctor
        if Doctor.objects.filter(
            name=cleaned_data.get('name'),
            specialization=cleaned_data.get('specialization'),
            room_number=cleaned_data.get('room_number')
        ).exists():
            raise forms.ValidationError("A doctor with these details already exists")
            
        return cleaned_data