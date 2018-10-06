import hashlib
from django.shortcuts import HttpResponse


def getMd5(data):
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()


# -*- coding: UTF-8 -*-



def isLogin(request):
    if request.session['username'] == "":
        return HttpResponse(request, "404")
