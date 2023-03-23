
from django.urls import path
from . import views


urlpatterns = [

    path('',views.loginForm1, name="first"),

    path('login/',views.loginForm, name="registration.login"),
    path('signup/',views.SignUpForm,name="registration.signup"),
     
    #  path('store/',views.registrationStore,name="registration.store")
] 