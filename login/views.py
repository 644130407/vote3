from django.shortcuts import render,redirect
from login import models
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        no = request.POST.get('no')
        password = request.POST.get('password')
        print(no)
        print(password)
        result = models.UserInfo.objects.filter(no=no).filter(password=password)
        print(result[0].password)

        return redirect('/login/')