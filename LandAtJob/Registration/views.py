from django.http import HttpResponse
from django.shortcuts import redirect, render

from Registration.models import Registration

# Create your views here.

def loginform(request): 
    data={
        'title':'Member Registration'

    }
    return render(request,"registration/login.html",data)

def signform(request):
    date={
        'title': 'signup'
    }
    return render(request,"Registration/signup.html",date)

def registrationStore(request):
    if request.method=="POST":
        password=request.POST['password']
        cpassword=request.POST['cpassword']

    if password != cpassword:
        return HttpResponse("Your Password Does not Match") 

    else:
        registration=Registration(
            email= request.POST['email'],
            full_name= request.POST['full_name'],
            dob =request.POST['dob'],
            password= request.POST['password'],
            cpassword= request.POST['cpassword'],
            created_at= request.POST.get('created_at', False),
            updated_at= request.POST.get('updated_at', False)
        )
        registration.save()
        return redirect('registration.login')
    return render(request,'registration/signup.html')
            