from django.shortcuts import render, HttpResponse, redirect
from checkin import models as checkinModels
import os
import datetime
import time
from login import models as loginModels
from django.core.paginator import Paginator, Page


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
        result = loginModels.UserInfo.objects.filter(no=no)
        return render(request, "upload.html",
                      {'username': result[0].username, 'danwei': result[0].danwei, 'xiangmu': result[0].xiangmu})
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

    ts = str(round(time.time() * 1000))
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
    # from checkin import models
    print("saveInfo")
    path = request.session.get('path')
    no = request.session.get('uno')
    bref = request.POST.get('bref')
    date = datetime.datetime.now().timestamp()
    if (path == ""):
        return HttpResponse(2)
    if (bref == ""):
        return HttpResponse(3)
    print(path, no, bref, date)
    result = checkinModels.PicsInfo.objects.create(no=no, path=path, date=date, bref=bref)
    request.session['path'] = ""
    if result:
        return HttpResponse(1)
    else:
        return HttpResponse(0)


# 打卡列表查询

def voteList(request):
    result = checkinModels.PicsInfo.objects.raw('''
    select checkin_picsinfo.pid, login_userinfo.username, 
    checkin_picsinfo.path, checkin_picsinfo.no, 
    checkin_picsinfo.bref, login_userinfo.danwei,
    checkin_picsinfo.date
    from login_userinfo left join checkin_picsinfo 
    on login_userinfo.`no`=checkin_picsinfo.no limit '''+ str(5) +',' + str(30))


    print(result)
    i = 0
    data = list(result)


    for item in result:
        # data.append(item)
        # print(type(item))
        data[i].date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item.date))

        print(data[i].date)
        i = i + 1

    paginator = Paginator(data, 1)
    try:
        current_page = int(request.GET.get('page'))
        posts = paginator.page(current_page)

    except ValueError as e:
        current_page = 1
        posts = paginator.page(current_page)

    page_len = list(posts.paginator.page_range).__len__()
    show_page = 3
    total_page = 5
    top_num = page_len - current_page
    bottom_num = current_page - 1
    if(bottom_num >= show_page):
        bottom_num = show_page

    rest_page = total_page - bottom_num

    if(top_num >= rest_page):
        top_num = rest_page


    return render(request, 'vote-list.html', {'posts': posts, 'top_num': range(current_page+1, current_page+top_num+1), 'bottom_num': range(current_page-bottom_num, current_page)})

# https://www.cnblogs.com/gregoryli/p/7683732.html
