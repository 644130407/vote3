from django.db import models

# Create your models here.
class PicsInfo(models.Model):

    pid = models.BigAutoField(primary_key=True)
    path = models.CharField(max_length=256)
    date = models.IntegerField()
    no = models.CharField(max_length=32)
