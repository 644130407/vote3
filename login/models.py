from django.db import models

# Create your models here.


class UserInfo(models.Model):

    nid = models.BigAutoField(primary_key=True)
    zongshu = models.IntegerField(default=1)
    bendanweirenshu = models.IntegerField(default=1)
    username = models.CharField(max_length=32)
    xinbie = models.CharField(max_length=10, default='男')
    nianlingduan = models.CharField(max_length=20, null=True, default=" ")
    shouji = models.CharField(max_length=20, null=True, default=" ")
    no = models.CharField(max_length=32, null=True, default='')
    danwei = models.CharField(max_length=50, null=True, default=" ")
    keshi = models.CharField(max_length=50, null=True, default=" ")
    xiangmu = models.CharField(max_length=50, null=True, default=" " )
    neirong = models.CharField(max_length=1000, null=True, default="")
    yuanyin = models.CharField(max_length=1000, null=True, default=" ")
    shuiping = models.CharField(max_length=200, null=True, default=" ")
    mubiao = models.CharField(max_length=500, null=True, default=" ")
    xuanyan = models.CharField(max_length=1000, null=True, default=" ")
    zhaopian = models.CharField(max_length=1000, null=True, default=" ")
    jianzhengren = models.CharField(max_length=20, null=True, default=" ")
    jianzhengrenzhiwu = models.CharField(max_length=50, null=True, default=" ")
    password = models.CharField(max_length=64)


# Create your models here.
