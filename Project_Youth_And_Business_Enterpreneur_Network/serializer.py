from rest_framework import serializers
from Project_Youth_And_Business_Enterpreneur_Network.models import Organisation, Intern_JobkeerStudent, Startup, Consultant


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        organisation = Organisation.objects.create(
            fullName=validated_data['fullName'],    
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']
        )
        organisation.save()
        return organisation


class Intern_JobkeerStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern_JobkeerStudent
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        intern = Intern_JobkeerStudent.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']
        )
        intern.save()
        return intern


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        startup = Startup.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']
        )
        startup.save()
        return startup


class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        consultant = Consultant.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']
        )
        consultant.save()
        return consultant
