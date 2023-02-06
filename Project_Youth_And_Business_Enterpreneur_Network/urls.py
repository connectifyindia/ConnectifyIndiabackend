from django.urls import path
from Project_Youth_And_Business_Enterpreneur_Network import views


urlpatterns = [
    path('organisation/',views.OrganisationCreateView.as_view()),
    path('intern-jobseeker-student/',views.Intern_JobSeekerStudentCreateView.as_view()),
    path('startup/',views.StartupCreateView.as_view()),
    path('consultant/',views.ConsultantCreateView.as_view()),

]