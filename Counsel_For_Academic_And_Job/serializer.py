from rest_framework import serializers
from Counsel_For_Academic_And_Job.models import Student,Trainer_Counsellor,Professional_Employee,ContentPublisher,Admin
from django.contrib.auth.hashers import make_password



class StudentSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = Student
        fields = ('student_name', 'email', 'mobile', 'password')

    def create(self,validated_data):
        student=Student.objects.create(
            student_name=validated_data['student_name'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=make_password(validated_data['password']),
        )
        student.save()
        return student
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer_Counsellor
        fields=('fullName','email','mobile','password')

    def create(self,validated_data):
        trainer=Trainer_Counsellor.objects.create(
        fullName=validated_data['fullName'],
        email=validated_data['email'],  
        mobile=validated_data['mobile'],
        password=make_password(validated_data['password']),
        # subproject=validated_data['subproject']
        )
        trainer.save()
        return trainer

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Professional_Employee
        fields=('fullName','email','mobile','password')

    def create(self,validated_data):
        professional=Professional_Employee.objects.create(
        fullName=validated_data['fullName'],
        email=validated_data['email'],
        mobile=validated_data['mobile'],
        password=make_password(validated_data['password']),
        # subproject=validated_data['subproject']
        )
        professional.save()
        return professional

class ContentPublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContentPublisher
        fields=('fullName','email','mobile','password')

    def create(self,validated_data):
        content=ContentPublisher.objects.create(
        fullName=validated_data['fullName'],
        email=validated_data['email'],
        mobile=validated_data['mobile'],
        password=make_password(validated_data['password']),
         # subproject=validated_data['subproject']
        )
        content.save()
        return content

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=('fullName','email','mobile','password')

    def create(self,validated_data):
        admin=Admin.objects.create(
        fullName=validated_data['fullName'],
        email=validated_data['email'],
        mobile=validated_data['mobile'],
        password=make_password(validated_data['password']),
         # subproject=validated_data['subproject']
        )
        admin.save()
        return admin


class StudentLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =Student
        fields = ['email','password']

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if Student.objects.filter(email=email,password=password).exists():
            return True
        return False