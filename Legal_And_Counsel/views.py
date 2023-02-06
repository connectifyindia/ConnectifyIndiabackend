from django.shortcuts import render
from Legal_And_Counsel.models import Student_Intern, Advocate_Lawyer, Consumer_User, Content_PublishingUpload
from Legal_And_Counsel.serializer import Student_InternSerializer, Advocate_LawyerSerializer, Consumer_UserSerializer, Content_PublishingUploadSerializer
from rest_framework import generics

class Student_InternCreateView(generics.CreateAPIView):
    queryset = Student_Intern.objects.all()
    serializer_class = Student_InternSerializer

class Advocate_LawyerCreateView(generics.CreateAPIView):
    queryset = Advocate_Lawyer.objects.all()
    serializer_class = Advocate_LawyerSerializer

class Consumer_UserCreateView(generics.CreateAPIView):
    queryset = Consumer_User.objects.all()
    serializer_class = Consumer_UserSerializer

class Content_ManagerCreateView(generics.CreateAPIView):
    queryset = Content_PublishingUpload.objects.all()
    serializer_class = Content_PublishingUploadSerializer


# Create your views here.
