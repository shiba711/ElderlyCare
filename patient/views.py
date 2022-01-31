from django.shortcuts import render
# Create your views here.
from patient.models import Patient, Task, TaskSerializer
from django.http import Http404
from rest_framework.generics import UpdateAPIView


def index(request):
    latest_patients = Patient.objects.order_by('name')
    data = {'latest_patients': latest_patients}
    return render(request, 'patient/index.html', data)

def image1(request):
    return render(request, '/patient/patient-image.jpg')

def detail(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    return render(request, 'patient/detail.html', {'patient': patient, 'patient_id':patient_id})


class UpdateTaskAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific task by passing in the id of the task to update"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

