from django.shortcuts import render, HttpResponse, redirect
from checkin import models
import os
# Create your views here.
def upload(request):
    if request.session['uno'] != '':
        return render(request, "pics.html")
    else:
        return redirect('/login/')

def picUpload(request):
    print(request.POST)
    print(request.GET)
    obj = request.FILES.get('file')
    print(obj.size, obj.name)
    file_path = os.path.join('static', 'upload', obj.name)
    f = open(file_path, 'wb')
    for chunk in obj.chunks():
        f.write(chunk)
    f.close()
    # ret = {'status': True, 'path': file_path}
    models.PicsInfo.objects.create(no="1", path=file_path, date="1")
    return HttpResponse(0)

def checkin(request):
    if request.session.get('uno'):
        return render(request, "checkin.html")
    else:
        return redirect('/login/')

# https://www.cnblogs.com/gregoryli/p/7683732.html