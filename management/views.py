from django.shortcuts import render
from common import utils
from management import models

# Create your views here.
def adminLogin(request):
    if request.method == 'GET':
        return render(request, 'admin_login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5_password = utils.getMd5(password)
        result = models.AdminInfo.objects.filter(username=username).filter(password=md5_password)
        if(result):
            request.session['username'] = username
            return render(request, 'admin-index.html')
        else:
            return render(request, 'admin-login.html', {'info': "用户名或密码错误"})