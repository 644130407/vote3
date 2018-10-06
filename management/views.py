from django.shortcuts import render, redirect
from common import utils
from management import models as managementModels

# Create your views here.
def adminLogin(request):
    if request.method == 'GET':
        print("adfsafdsaf")
        print(request.session.get('username'))
        if request.session.get('username'):
            return render(request, 'admin-index.html', {'username': request.session['username']})
        return render(request, 'admin-login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5_password = utils.getMd5(password)
        result = managementModels.AdminInfo.objects.filter(username=username).filter(password=md5_password)
        print(result[0].username)
        if(len(result)>0):
            request.session['username'] = username
            print(request.session['username'])
            return render(request, 'admin-index.html', {'username': result[0].username})
        else:
            return render(request, 'admin-login.html', {'info': "用户名或密码错误"})


def memberList(request):
    utils.isLogin(request)
    print(request.session.get('username'))

    result = managementModels.AdminInfo.objects.filter(username=request.session.get('username'))
    print(result)
    return render(request, 'member-list.html', {'data': result[0]})

def exit(request):
    del request.session["username"]
    return redirect('/adminLogin/')