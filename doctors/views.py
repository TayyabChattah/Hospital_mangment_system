from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Doctor
from .forms import DoctorForm

# Create your views here.
# Web Views
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/list.html', {'doctors': doctors})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors:doctor-list')
    else:
        form = DoctorForm()
    return render(request, 'doctors/form.html', {'form': form})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctors/detail.html', {'doctor': doctor})

def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors:doctor-detail', pk=doctor.pk)
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/form.html', {'form': form})

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors:doctor-list')
    return render(request, 'doctors/confirm_delete.html', {'doctor': doctor})

def doctor_availability(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    date = request.GET.get('date')
    
    # In a full implementation, you would calculate actual available slots
    # Here we just return the doctor's standard availability
    return JsonResponse({
        'available_days': doctor.available_days,
        'available_from': doctor.available_from.strftime('%H:%M'),
        'available_to': doctor.available_to.strftime('%H:%M'),
    })
