from django.contrib import admin
from django.urls import path
from login.views import login
from checkin import views as checkin
from management import views as adminLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('upload', checkin.upload),
    path('picUpload/', checkin.picUpload),
    path('checkin/', checkin.checkin),
    path('saveInfo/', checkin.saveInfo),
    path('adminLogin/', adminLogin.adminLogin),
    path('voteList/', checkin.voteList)

]
