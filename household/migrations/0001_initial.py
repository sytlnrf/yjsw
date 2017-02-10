# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_money', models.IntegerField(default=0, help_text=b'\xe6\x94\xb6\xe8\xb4\xb9\xe9\x87\x91\xe9\xa2\x9d')),
                ('f_staff', models.CharField(help_text=b'\xe6\x94\xb6\xe8\xb4\xb9\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d', max_length=20)),
                ('f_user_name', models.CharField(help_text=b'\xe4\xbd\x8f\xe6\x88\xb7\xe5\xa7\x93\xe5\x90\x8d', max_length=20)),
                ('f_memo', models.CharField(default=b'', help_text=b'\xe5\xa4\x87\xe6\xb3\xa8', max_length=200)),
                ('f_s_date', models.DateTimeField(help_text=b'\xe6\x94\xb6\xe8\xb4\xb9\xe8\xb5\xb7\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('f_e_date', models.DateTimeField(help_text=b'\xe6\x94\xb6\xe8\xb4\xb9\xe7\xbb\x93\xe6\x9d\x9f\xe6\x97\xb6\xe9\x97\xb4')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_name', models.CharField(help_text=b'\xe6\x88\xb7\xe4\xb8\xbb\xe5\xa7\x93\xe5\x90\x8d', max_length=20)),
                ('u_phone', models.CharField(default=b'', help_text=b'\xe6\x88\xb7\xe4\xb8\xbb\xe7\x94\xb5\xe8\xaf\x9d', unique=True, max_length=11)),
                ('watermeter_id', models.CharField(help_text=b'\xe6\xb0\xb4\xe8\xa1\xa8\xe7\xbc\x96\xe5\x8f\xb7', unique=True, max_length=20)),
                ('u_address', models.CharField(help_text=b'\xe6\x88\xb7\xe4\xb8\xbb\xe5\x9c\xb0\xe5\x9d\x80', max_length=100)),
                ('u_people', models.IntegerField(default=1, help_text=b'\xe6\x88\xb7\xe4\xb8\xbb\xe5\xae\xb6\xe4\xba\xba\xe5\x8f\xa3\xe6\x95\xb0')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Watermeter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('w_number', models.IntegerField(default=0, help_text=b'\xe6\x8a\x84\xe8\xa1\xa8\xe5\xba\xa6\xe6\x95\xb0')),
                ('w_date', models.DateTimeField(help_text=b'\xe6\x8a\x84\xe8\xa1\xa8\xe6\x97\xa5\xe6\x9c\x9f')),
                ('w_staff', models.CharField(help_text=b'\xe6\x8a\x84\xe8\xa1\xa8\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('watermeter_id', models.ForeignKey(to='household.Users', db_column=b'watermeter_id')),
            ],
        ),
        migrations.AddField(
            model_name='fees',
            name='watermeter_id',
            field=models.ForeignKey(to='household.Users', db_column=b'watermeter_id'),
        ),
    ]
