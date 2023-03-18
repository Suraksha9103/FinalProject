from django.shortcuts import render

# Create your views here.

def loginform(request):
    data={
        'title':'Member Registration'

    }
    return render(request,"registration/login.html",data)