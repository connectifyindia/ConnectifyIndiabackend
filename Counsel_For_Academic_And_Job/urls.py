from django.urls import path
from Counsel_For_Academic_And_Job import views


urlpatterns = [
    path('student-register/',views.StudentCreateView.as_view()),
    path('trainer/',views.TrainerCreateView.as_view()),
    path('professional/',views.ProfessionalCreateView.as_view()),
    path('content-publisher/',views.ContentPublisherCreateView.as_view()),
    path('admin/',views.AdminCreateView.as_view()),
    path('student-login/',views.login_view),




]