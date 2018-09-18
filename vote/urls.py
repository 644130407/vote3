from django.contrib import admin
from django.urls import path
from login.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login)
]
