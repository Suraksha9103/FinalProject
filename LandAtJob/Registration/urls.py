
from django.urls import path
from . import views


urlpatterns = [
    path('',views.loginform, name="registration.login"),
    path('signup/',views.signform,name="registration.signup"),
    path('store/',views.registrationStore,name="registration.store")
] 