# Generated by Django 2.2 on 2019-07-18 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartCareApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='callcentre',
            name='Address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='callcentre',
            name='City',
            field=models.CharField(default='', max_length=50),
        ),
    ]
