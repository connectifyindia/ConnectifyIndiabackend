from django.db import models

# Create your models here.


class Student_Intern(models.Model):
    sub_project_choices = [
        ('Student/Intern', 'Student/Intern'),
        ('Advocate/Lawyer', 'Advocate/Lawyer'),
        ('Consumer/User', 'Consumer/User'),
        ('Content PublishingUpload', 'Content PublishingUpload'),
    ]

    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class Advocate_Lawyer(models.Model):
    sub_project_choices = [
        ('Student/Intern', 'Student/Intern'),
        ('Advocate/Lawyer', 'Advocate/Lawyer'),
        ('Consumer/User', 'Consumer/User'),
        ('Content PublishingUpload', 'Content PublishingUpload'),
    ]

    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class Consumer_User(models.Model):
    sub_project_choices = [
        ('Student/Intern', 'Student/Intern'),
        ('Advocate/Lawyer', 'Advocate/Lawyer'),
        ('Consumer/User', 'Consumer/User'),
        ('Content PublishingUpload', 'Content PublishingUpload'),
    ]
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class Content_PublishingUpload(models.Model):
    sub_project_choices = [
        ('Student/Intern', 'Student/Intern'),
        ('Advocate/Lawyer', 'Advocate/Lawyer'),
        ('Consumer/User', 'Consumer/User'),
        ('Content PublishingUpload', 'Content PublishingUpload'),
    ]

    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email
