from django.contrib import admin
from django.urls import path
from login import views as login
from checkin import views as checkin
from management import views as management

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login.login),
    path('upload', checkin.upload),
    path('picUpload/', checkin.picUpload),
    path('checkin/', checkin.checkin),
    path('saveInfo/', checkin.saveInfo),
    path('adminLogin/', management.adminLogin),
    path('voteList/', checkin.voteList),
    path('exportAllExcel/', checkin.exportAllExcel),
    path('approve/', checkin.approve),
    path('refuse/', checkin.refuse),
    path('test/', checkin.test),
    path('member-list/', management.memberList),
    path('exit/', management.exit)

]
