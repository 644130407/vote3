from django.shortcuts import render,redirect
from login import models
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        no = request.POST.get('shouji')
        password = request.POST.get('password')

        result = models.UserInfo.objects.filter(shouji=no).filter(password=password)
        if(len(result)>0):
            request.session['uno'] = result[0].shouji
            request.session['user'] = result[0].username
            return redirect('/checkin/')
        return redirect('/login/')