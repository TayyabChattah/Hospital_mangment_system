from django.contrib import admin
from .models import Appointment
# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'appointment_time', 'status')
    list_filter = ('doctor', 'appointment_date', 'appointment_time', 'status')
    search_fields = ('patient__name', 'doctor__name', 'appointment_date', 'appointment_time')
    ordering = ('appointment_date', 'appointment_time')