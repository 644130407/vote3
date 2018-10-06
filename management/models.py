from django.db import models


# Create your models here.
class AdminInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    danwei = models.CharField(max_length=50, default="指 挥 部")
    xinming = models.CharField(max_length=50, default="")