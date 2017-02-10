# -*- coding: UTF-8 -*-
from django.db import models

class Users(models.Model):
    """
    Usage:住户登记
    """
    u_name = models.CharField(max_length=20, blank=False, help_text='户主姓名', verbose_name='户主姓名')
    u_phone = models.CharField(max_length=11, default='', unique=True, help_text='户主电话')
    watermeter_id = models.CharField(max_length=20, blank=False, unique=True, help_text='水表编号')
    u_address = models.CharField(max_length=100, blank=False, help_text='户主地址')
    u_people = models.IntegerField(default=1, help_text='户主家人口数')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.u_name

class Fees(models.Model):
    """
    Usage:收费记录
    """
    # f_watermeter_id = models.CharField(max_length=20, blank=False, help_text='水表编号')
    watermeter_id = models.ForeignKey(Users, db_column='watermeter_id')
    f_money = models.IntegerField(default=0, help_text='收费金额')
    f_staff = models.CharField(max_length=20, blank=False, help_text='收费人姓名')
    f_user_name = models.CharField(max_length=20, blank=False, help_text='住户姓名')
    f_memo = models.CharField(max_length=200, default='', help_text='备注')
    f_s_date = models.DateTimeField(help_text='收费起始时间')
    f_e_date = models.DateTimeField(help_text='收费结束时间')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Watermeter(models.Model):
    """
    Usage:抄表记录
    """
    # watermeter_id = models.CharField(max_length=20, blank=False, help_text='水表编号')
    watermeter_id = models.ForeignKey(Users, db_column='watermeter_id')
    w_number = models.IntegerField(default=0, blank=False, help_text='抄表度数')
    w_date = models.DateTimeField(help_text='抄表日期')
    w_staff = models.CharField(max_length=20, blank=False, help_text='抄表人姓名')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



