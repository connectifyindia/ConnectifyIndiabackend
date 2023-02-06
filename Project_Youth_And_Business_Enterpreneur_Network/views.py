from django.shortcuts import render
from Project_Youth_And_Business_Enterpreneur_Network.models import Organisation, Intern_JobkeerStudent, Startup, Consultant
from Project_Youth_And_Business_Enterpreneur_Network.serializer import OrganisationSerializer,Intern_JobkeerStudentSerializer,StartupSerializer,ConsultantSerializer
from rest_framework import generics
 
class OrganisationCreateView(generics.CreateAPIView):
    queryset=Organisation.objects.all()
    serializer_class=OrganisationSerializer

class Intern_JobSeekerStudentCreateView(generics.CreateAPIView):
     queryset=Intern_JobkeerStudent.objects.all()
     serializer_class=Intern_JobkeerStudentSerializer

class StartupCreateView(generics.CreateAPIView):
     queryset=Startup.objects.all()
     serializer_class=StartupSerializer

class ConsultantCreateView(generics.CreateAPIView):
     queryset=Consultant.objects.all()
     serializer_class=ConsultantSerializer
    

# Create your views here.
