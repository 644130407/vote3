from django.shortcuts import render, HttpResponse, redirect
from checkin import models
import os
import datetime
import time
from login import models
# Create your views here.

def mkdir(path):
    path = path.strip()

    path = path.rstrip("\\")
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        print(path + ' 目录已存在')
        return False


def upload(request):
    if request.session.get('uno'):
        print(request.session.get('uno'))
        no = request.session.get('uno')
        result = models.UserInfo.objects.filter(no=no)
        return render(request, "upload.html", {'username': result[0].username, 'danwei': result[0].danwei, 'xiangmu': result[0].xiangmu})
    else:
        return redirect('/login/')

def picUpload(request):

    obj = request.FILES.get('file')
    print(obj.size, obj.name)

    path = os.path.join('static', 'upload', str(request.session.get('uno')))
    mkdir(path)

    file_path = os.path.join('static', 'upload', str(request.session.get('uno')), obj.name)
    f = open(file_path, 'wb')
    for chunk in obj.chunks():
        result = f.write(chunk)
    f.close()
    print(result)
    ext = os.path.splitext(file_path)[1]

    ts = str(round(time.time()*1000))
    print(ts)

    new_file = os.path.join('static', 'upload', str(request.session.get('uno')), ts + ext)

    os.rename(file_path, new_file)
    # ret = {'status': True, 'path': file_path}

    # models.PicsInfo.objects.create(no="1", path=file_path, date="1")
    request.session['path'] = new_file

    return HttpResponse(0)

def checkin(request):
    if request.session.get('uno'):
        print('uno')
        return render(request, "checkin.html")
    else:
        return redirect('/login/')

def saveInfo(request):
    from checkin import models
    print("saveInfo")
    path = request.session.get('path')
    no = request.session.get('uno')
    bref = request.POST.get('bref')
    date = datetime.datetime.now().timestamp()
    if(path == ""):
        return HttpResponse(2)
    if(bref == ""):
        return HttpResponse(3)
    print(path, no, bref, date)
    result = models.PicsInfo.objects.create(no=no, path=path, date=date, bref=bref)
    request.session['path'] = ""
    if result:
        return HttpResponse(1)
    else:
        return HttpResponse(0)





# https://www.cnblogs.com/gregoryli/p/7683732.html