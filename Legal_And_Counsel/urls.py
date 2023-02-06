from django.urls import path
from Legal_And_Counsel import views


urlpatterns = [
    path('student_intern/',views.Student_InternCreateView.as_view()),
    path('advocate/',views.Advocate_LawyerCreateView.as_view()),
    path('consumer/',views.Consumer_UserCreateView.as_view()),
    path('content-publisher/',views.Content_ManagerCreateView.as_view()),

]