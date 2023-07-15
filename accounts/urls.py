from django.urls import path
from .views import SignUpView 
from django.views.generic import TemplateView

app_name="accounts"
urlpatterns=[
    #path("signup/", SignUpView.as_view(), name="signup"),
    path('myprofile/', TemplateView.as_view(template_name='myprofile.html'), name='myprofile'),
    #path("profile/",ProfileView.as_view(),name="profile" )
]

#SignUpView is based on built-in UserCreationForm  on projectLevel && generic.Createview Class on app's level
