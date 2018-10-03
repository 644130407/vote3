from django.db import models


# Create your models here.
class PicsInfo(models.Model):
    pid = models.BigAutoField(primary_key=True)
    path = models.CharField(max_length=256)
    date = models.IntegerField()
    no = models.CharField(max_length=32)
    bref = models.CharField(max_length=2048, default="")
    state = models.IntegerField(default=0)
    comment = models.CharField(max_length=218, default="通过")
    comment_author = models.IntegerField(default=1)
