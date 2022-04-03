from django.urls import path
from .views import SignUpView


urlpatterns=[
    path("signup/", SignUpView.as_view(), name="signup"),
]

#SignUpView is based on built-in UserCreationForm  on projectLevel && generic.Createview Class on app's level
