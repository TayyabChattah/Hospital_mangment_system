from django.shortcuts import render,redirect,get_object_or_404
from .models import Appointment
# Create your
from .forms import AppointmentForm


def appointment_list(request):
    appointments=Appointment.objects.all()
    return render(request,'appointments/list.html',{'appointments':appointments})
    
def appointment_create(request):
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments:appointment-list')
    else:
        form=AppointmentForm()
    return render(request,'appointments/form.html',{'form':form})
def appointment_detail(request,pk):
    appointment=get_object_or_404(Appointment,pk=pk)
    return render(request,'appointments/detail.html',{'appointment':appointment})
def appointment_update(request,pk):
    appointment=get_object_or_404(Appointment,pk=pk)
    if request.method=='POST':
        form=AppointmentForm(request.POST,instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments:appointment-detail',pk=appointment.pk)
    else:
        form=AppointmentForm(instance=appointment)
    return render(request,'appointments/form.html',{'form':form})
def appointment_delete(request,pk):
    appointment=get_object_or_404(Appointment,pk=pk)
    if request.method=='POST':
        appointment.delete()
        return redirect('appointments:appointment-list')
    return render(request,'appointments/confirm_delete.html',{'appointment':appointment})  
 