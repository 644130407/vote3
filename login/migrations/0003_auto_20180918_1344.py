# Generated by Django 2.1.1 on 2018-09-18 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180918_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('nid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
                ('bref', models.CharField(max_length=2048)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
