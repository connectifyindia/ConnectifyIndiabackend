from django.shortcuts import render
from Counsel_For_Academic_And_Job.models import Student, Trainer_Counsellor, Professional_Employee, ContentPublisher,Admin
from Counsel_For_Academic_And_Job.serializer import StudentSerializer, TrainerSerializer, ProfessionalSerializer, ContentPublisherSerializer,AdminSerializer,StudentLoginSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TrainerCreateView(generics.CreateAPIView):
    queryset = Trainer_Counsellor.objects.all()
    serializer_class = TrainerSerializer

class ProfessionalCreateView(generics.CreateAPIView):
    queryset = Professional_Employee.objects.all()
    serializer_class = ProfessionalSerializer

class ContentPublisherCreateView(generics.CreateAPIView):
    queryset = ContentPublisher.objects.all()
    serializer_class = ContentPublisherSerializer

class AdminCreateView(generics.CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class=AdminSerializer


# Create your views here.
@api_view(['POST'])
def login_view(request):
    if request.method=="POST":
        serializer =StudentLoginSerializer(data=request.data)
        require_fields = {
            "email" : "email"
        }
        qs_fields_data = {}
        for k,v  in require_fields.items():
            qs_fields_data[v] = request.data.get(k)

        pwd = request.data.get('password')
        qs_fields_data['password'] = pwd

        # from django.conf import settings
        # password = make_password(pwd, salt=settings.SECRET_KEY)
        # qs_fields_data['password'] = password

        account_instance = Student.objects.filter(**qs_fields_data)
        response = {}
        if account_instance:
            response["message"]="User successfully login"
            response["status"] = status.HTTP_200_OK
            return Response(response, status=status.HTTP_200_OK)
        else:
            response["message"] = "You have entered an invalid username or password"
            response["status"] = status.HTTP_400_BAD_REQUEST
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
