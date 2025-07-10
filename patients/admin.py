from django.contrib import admin
from .models import Patient
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=('name','gender','age','phone_number')
    list_filter=('gender','age','name','phone_number')
    search_fields=('name','phone_number')