from django.contrib import admin
from django.urls import path
from login.views import login
from checkin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('upload', views.upload),
    path('picUpload/', views.picUpload),
    path('checkin/', views.checkin),
    path('saveInfo/', views.saveInfo),
]
