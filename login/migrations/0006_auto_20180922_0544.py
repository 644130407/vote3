# Generated by Django 2.0 on 2018-09-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20180918_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='danwei',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='jianzhengren',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='jianzhengrenzhiwu',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='keshi',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='mubiao',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='neirong',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='shouji',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='shuiping',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='xiangmu',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='xinbie',
            field=models.CharField(default='男', max_length=10),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='xuanyan',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='yuanyi',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='zhaopian',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='zongshu',
            field=models.IntegerField(default=1),
        ),
    ]
