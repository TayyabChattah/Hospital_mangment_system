from django.contrib import admin
from .models import Doctor
# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=('name','specialization','available_days','available_from','available_to','room_number')
    list_filter=('specialization','available_days')
    search_fields=('name','specialization')