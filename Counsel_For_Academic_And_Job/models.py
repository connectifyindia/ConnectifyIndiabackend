from django.db import models

# Create your models here.


class Student(models.Model):

    student_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)

    def __str__(self):
        return self.email


class Trainer_Counsellor(models.Model):
    # sub_project_choices = [
    #     ('student/parents', 'student/parents'),
    #     ('trainer/counsellor', 'trainer/counsellor'),
    #     ('professional/employee', 'professional/employee'),
    #     ('content publisher', 'content publisher'),
    # ]

    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class Professional_Employee(models.Model):
    # sub_project_choices = [
    #     ('student/parents', 'student/parents'),
    #     ('trainer/counsellor', 'trainer/counsellor'),
    #     ('professional/employee', 'professional/employee'),
    #     ('content publisher', 'content publisher'),
    # ]
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class ContentPublisher(models.Model):
    # sub_project_choices = [
    #     ('student/parents', 'student/parents'),
    #     ('trainer/counsellor', 'trainer/counsellor'),
    #     ('professional/employee', 'professional/employee'),
    #     ('content publisher', 'content publisher'),
    # ]

    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email

class Admin(models.Model):
    # sub_project_choices = [
    #     ('student/parents', 'student/parents'),
    #     ('trainer/counsellor', 'trainer/counsellor'),
    #     ('professional/employee', 'professional/employee'),
    #     ('content publisher', 'content publisher'),
    # ]

    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    # subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email
