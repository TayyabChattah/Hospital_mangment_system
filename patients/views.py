from django.shortcuts import render,redirect,get_object_or_404
from .models import Patient
from .forms import PatientForm

# Create your views here.
def patient_list(request):
    patients=Patient.objects.all()
    return render(request,'patients/list.html',{'patients':patients})

def patient_create(request):
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients:patient-list')
    else:
        form=PatientForm()
    return render(request,'patients/form.html',{'form':form})

def patient_detail(request,pk):
    patient=get_object_or_404(Patient,pk=pk)
    return render(request,'patients/detail.html',{'patient':patient})

def patient_update(request,pk):
    patient=get_object_or_404(Patient,pk=pk)
    if request.method=='POST':
        form=PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients:patient-detail',pk=patient.pk)
    else:
        form=PatientForm(instance=patient)
    return render(request,'patients/form.html',{'form':form})

def patient_delete(request,pk):
    patient=get_object_or_404(Patient,pk=pk)
    if request.method=='POST':
        patient.delete()
        return redirect('patients:patient-list')
    return render(request,'patients/confirm_delete.html',{'patient':patient})