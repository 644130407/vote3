# Generated by Django 2.0 on 2018-09-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
