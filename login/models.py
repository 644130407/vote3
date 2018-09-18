from django.db import models

# Create your models here.


class UserInfo(models.Model):

    nid = models.BigAutoField(primary_key=True)
    no = models.CharField(max_length=32, default='')
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    bref = models.CharField(max_length=2048)

# Create your models here.
