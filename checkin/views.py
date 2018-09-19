from django.shortcuts import render, HttpResponse
import os
# Create your views here.
def upload(request):
    return render(request, "pics.html")

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
    ret = {'status': True, 'path': file_path}
    return HttpResponse(0)

# https://www.cnblogs.com/gregoryli/p/7683732.html