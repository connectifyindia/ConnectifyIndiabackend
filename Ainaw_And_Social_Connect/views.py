from django.shortcuts import render
from Ainaw_And_Social_Connect.models import RegisterNGO, NonRegisterNGO, SocialActivist_Enterpreneur, Business_Manpower
from Ainaw_And_Social_Connect.serializer import RegisterNGOSerializer,NonRegisterNGOSerializer,SocialActivist_EnterpreneurSerializer,Business_ManpowerSerializer
from rest_framework import generics

class  RegisterNGOCreateView(generics.CreateAPIView):
    queryset = RegisterNGO.objects.all()
    serializer_class =  RegisterNGOSerializer

class  NonRegisterNGOCreateView(generics.CreateAPIView):
    queryset =  NonRegisterNGO.objects.all()
    serializer_class = NonRegisterNGOSerializer

class SocialActivistCreateView(generics.CreateAPIView):
    queryset = SocialActivist_Enterpreneur.objects.all()
    serializer_class = SocialActivist_EnterpreneurSerializer

class BusinessCreateView(generics.CreateAPIView):
    queryset = Business_Manpower.objects.all()
    serializer_class = Business_ManpowerSerializer


# Create your views here.
