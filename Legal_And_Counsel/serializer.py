from rest_framework import serializers
from Legal_And_Counsel.models import Student_Intern, Advocate_Lawyer, Consumer_User, Content_PublishingUpload


class Student_InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Intern
        fields = ('student_name', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        student = Student_Intern.objects.create(
            student_name=validated_data['student_name'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']   

        )
        student.save()
        return student


class Advocate_LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate_Lawyer
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        advocate = Advocate_Lawyer.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']
        )
        advocate.save()
        return advocate


class Consumer_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer_User
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        consumer = Consumer_User.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']
        )
        consumer.save()
        return  consumer


class Content_PublishingUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content_PublishingUpload
        fields = ('fullName', 'email', 'mobile', 'password', 'subproject')

    def create(self, validated_data):
        content = Content_PublishingUpload.objects.create(
            fullName=validated_data['fullName'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            subproject=validated_data['subproject']
        )
        content.save()
        return content
