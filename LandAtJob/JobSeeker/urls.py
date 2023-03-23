
from django.urls import path
from . import views


urlpatterns = [

    

    path('seekerlogin/',views.loginForm, name="jobseeker.login"),
    path('seekersignup/',views.SignupPage,name="jobseeker.signup"),
    
     
    #  path('store/',views.registrationStore,name="registration.store")
] 