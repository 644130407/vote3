# Generated by Django 2.0 on 2018-10-05 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_admininfo_danwei'),
    ]

    operations = [
        migrations.AddField(
            model_name='admininfo',
            name='xinming',
            field=models.CharField(default='', max_length=50),
        ),
    ]
