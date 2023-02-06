from django.urls import path
from Ainaw_And_Social_Connect import views


urlpatterns = [
    path('register-ngo/',views. RegisterNGOCreateView.as_view()),
    path('non-register-ngo/',views.NonRegisterNGOCreateView.as_view()),
    path('social-activist/',views.SocialActivistCreateView.as_view()),
    path('business/',views.BusinessCreateView.as_view()),

]