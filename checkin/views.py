from django.shortcuts import render, HttpResponse, redirect
from checkin import models as checkinModels
import os
import datetime
import time
from login import models as loginModels
from django.core.paginator import Paginator, Page
import math
import json
from io import BytesIO
import shutil
import sys
from management import models as managementModels
from xlwt import *
import zipfile



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


# 打卡数据库检索


def voteListSQL(limitBottom, limitTop, danwei, day):
    sql = '''
        select checkin_picsinfo.pid, login_userinfo.username, 
        checkin_picsinfo.path, checkin_picsinfo.no, 
        checkin_picsinfo.bref, login_userinfo.danwei,
        checkin_picsinfo.date, checkin_picsinfo.state,
        checkin_picsinfo.comment, management_admininfo.username as author_name
        from login_userinfo right join checkin_picsinfo 
        on login_userinfo.`no`=checkin_picsinfo.no
    	left join management_admininfo
    	on management_admininfo.id = checkin_picsinfo.comment_author
    	'''
    if danwei != '':
        sql = sql + " where login_userinfo.danwei=" + "'" + danwei + "'"
        if day != 0:
            sql = sql + ' and checkin_picsinfo.date>=' + str(day) + ' and checkin_picsinfo.date<=' + str(int(day) + 86400)
    else:
        if day != 0:
            sql = sql + ' where checkin_picsinfo.date>=' + str(day) + ' and checkin_picsinfo.date<=' + str(int(day) + 86400)

    result = checkinModels.PicsInfo.objects.raw(sql)
    count = len(list(result))


    sql = sql + ''' 
         ORDER BY checkin_picsinfo.pid desc
    	limit ''' + limitBottom + ',' + limitTop

    result = checkinModels.PicsInfo.objects.raw(sql)
    data = list(result)
    i = 0
    for item in data:
        data[i].date = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item.date + +28800)))
        i = i + 1
    return [data, count]


# 打卡列表查询

def voteList(request):
    # 当前页面
    current_page = int(request.GET.get('page'))
    # 每页显示条目数
    each_page_num = 1
    datas = voteListSQL(str((current_page-1) * each_page_num), str(each_page_num), '', 1538524800)
    data = datas[0]
    # 所有记录条目数

    all_item_num = datas[1]

    # 页面总数
    all_page_num = math.ceil(all_item_num / each_page_num)
    # 显示页码数
    total_page = 6



    paginator = Paginator(data, each_page_num)
    try:
        # current_page = int(request.GET.get('page'))
        posts = paginator.page(1)

    except ValueError as e:
        current_page = 1
        posts = paginator.page(current_page)

    # page_len = all_page_num
    # print(all_page_num)

    #
    # if len(data)/each_page_num < total_page:
    #     page_len = math.ceil(len(data)/ each_page_num)
    #     print(show_page)
    #     print("adfsaf")

    bottom_total_page = round(total_page/2)
    bottom_num = current_page - bottom_total_page
    if bottom_num <= 0:
        bottom_num = 1 #获取低位页面数


    use_num = current_page - bottom_num

    top_num = current_page + total_page-use_num


    real_total_num = round(all_item_num/each_page_num)

    if top_num > all_page_num:
        top_num = all_page_num+1 #获取高位页面数
    if real_total_num < top_num:
        top_num = real_total_num+1


    # print(bottom_num == current_page - round(total_page/2))
    # print(top_num - current_page)
    #
    # print((top_num-current_page)<(total_page-bottom_num))
    # if bottom_num == (current_page - round(total_page/2)) and (top_num-current_page)<round(total_page/2):
    #     bottom_num = bottom_num-top_num+current_page

    has_pre = True
    has_next = True

    if (current_page <= 1):
        has_pre = False

    print("top")
    print(top_num)
    if (current_page >= top_num-1):
        has_next = False

    return render(request, 'vote-list.html', {'posts': posts,
                                              'top_num': range(current_page, top_num),
                                              'bottom_num': range(bottom_num, current_page),
                                              'has_pre': has_pre,
                                              'has_next': has_next,
                                              'pre_page': current_page-1,
                                              'next_page': current_page + 1})


def exportAllExcel(request):
    data = voteListSQL('0', '100000', '', 0)[0]

    if data:
        # 创建工作薄
        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u"数据报表第一页")
        w.write(0, 0, u"用户名")
        w.write(0, 1, u"警员编号")
        w.write(0, 2, u"提交说明")
        w.write(0, 3, u"所在单位")
        w.write(0, 4, u"提交时间")
        w.write(0, 5, u"当前状态")
        w.write(0, 6, u"审核信息")
        w.write(0, 7, u"审核人")
        # 写入数据
        excel_row = 1

        for obj in data:
            data_username = obj.username
            data_no = obj.no
            data_bref = obj.bref
            data_danwei = obj.danwei
            data_date = obj.date
            data_state = obj.state
            dada_comment = obj.comment
            data_author_name = obj.author_name
            w.write(excel_row, 0, data_username)
            w.write(excel_row, 1, data_no)
            w.write(excel_row, 2, data_bref)
            w.write(excel_row, 3, data_danwei)
            w.write(excel_row, 4, data_date)
            w.write(excel_row, 5, data_state)
            w.write(excel_row, 6, dada_comment)
            w.write(excel_row, 7, data_author_name)

            excel_row += 1

            path = os.path.join('static', 'upload', 'excel')

        exist_file = os.path.exists(os.path.join(path, "test.xls"))
        if exist_file:
            os.remove(os.path.join(path, "test.xls"))
        ws.save(os.path.join(path, "test.xls"))
        sio = BytesIO()
        ws.save(sio)
        sio.seek(0)
        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=test.xls'
        response.write(sio.getvalue())
        return response


def approve(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        result = checkinModels.PicsInfo.objects.filter(pid=pid).update(state=1)
        if result > 0:
            return HttpResponse(True)
    return HttpResponse(False)


def refuse(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        comment = request.POST.get('comment')
        result = checkinModels.PicsInfo.objects.filter(pid=pid).update(state=0, comment=comment)
        if result > 0:
            return HttpResponse(json.dumps({'state': True, 'comment': comment}), content_type="application/json")
    return HttpResponse(False)

# 查找今天的所有数据
# def findTodayData(danwei, )






def test(request):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    print(today)
    yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
    yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
    print(yesterday_end_time)
    print(yesterday_start_time)
    print(yesterday_end_time-yesterday_start_time)
    data = voteListSQL('0', '100000', '', 0)
    for item in data[0]:
        item_date = datetime.datetime.strptime(item.date, '%Y-%m-%d %H:%M:%S')

        year = item_date.date().timetuple().tm_year
        month = item_date.date().timetuple().tm_mon
        day = item_date.date().timetuple().tm_mday

        # print(year, month, day)

        now_year = today.timetuple().tm_year
        now_moth = today.timetuple().tm_mon
        now_day = today.timetuple().tm_mday

        # print(year == now_year)


        if year == now_year and month == now_moth and day == now_day-1:
            new_file = os.path.join(item.path)
            print(new_file)
            new_path = os.path.join('static', 'temp', str(item.no)+'_'+item.username)
            if not os.path.exists(new_path):
                mkdir(new_path)

            shutil.copyfile(new_file, os.path.join(new_path, str(item_date)+ os.path.splitext(item.path)[1]))
            print(item.path)
            print('aa')
    # z = zipfile.ZipFile(os.path.join('static', 'upload', 'files.zip'), 'w')


    z = zipfile.ZipFile(os.path.join('static', 'upload', 'files.zip'), mode='w', compression=zipfile.ZIP_DEFLATED)
    if(os.path.isdir(os.path.join('static', 'temp'))):
        for d in os.listdir(os.path.join('static', 'temp')):
            for d2 in os.listdir(os.path.join('static', 'temp', d)):
                print(os.path.join('static', 'temp', d)+os.sep+d2)
                z.write(os.path.join('static', 'temp', d)+os.sep+d2)
                z.close()
    print(z.filename)
    fread = open(z.filename, 'rb')
    response = HttpResponse(fread, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename={0}'.format('files.zip')
    fread.close()
    return response

# https://www.cnblogs.com/gregoryli/p/7683732.html
