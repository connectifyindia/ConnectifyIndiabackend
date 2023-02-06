from django.db import models

# Create your models here.


class RegisterNGO(models.Model):
    sub_project_choices = [
        ('NGO(Reg)', 'NGO(Reg'),
        ('NGO(Non Reg)', 'NGO(Non Reg)'),
        ('Social Activist/Enterpreneur', 'Social Activist/Enterpreneur'),
        ('Business/Manpower', 'Business/Manpower'),
    ]
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class NonRegisterNGO(models.Model):

    sub_project_choices = [
        ('NGO(Reg)', 'NGO(Reg'),
        ('NGO(Non Reg)', 'NGO(Non Reg)'),
        ('Social Activist/Enterpreneur', 'Social Activist/Enterpreneur'),
        ('Business/Manpower', 'Business/Manpower'),
    ]

    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class SocialActivist_Enterpreneur(models.Model):
    sub_project_choices = [
        ('NGO(Reg)', 'NGO(Reg'),
        ('NGO(Non Reg)', 'NGO(Non Reg)'),
        ('Social Activist/Enterpreneur', 'Social Activist/Enterpreneur'),
        ('Business/Manpower', 'Business/Manpower'),
    ]
    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email


class Business_Manpower(models.Model):
    sub_project_choices = [
        ('NGO(Reg)', 'NGO(Reg'),
        ('NGO(Non Reg)', 'NGO(Non Reg)'),
        ('Social Activist/Enterpreneur', 'Social Activist/Enterpreneur'),
        ('Business/Manpower', 'Business/Manpower'),
    ]

    fullName = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=254)
    subproject = models.CharField(max_length=254, choices=sub_project_choices)

    def __str__(self):
        return self.email
