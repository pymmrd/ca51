# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.

class Shop(models.Model):
    MEISHI = 1
    XIUXIAN = 2
    CAR = 3
    AIRPORT = 4
    HOUSE = 5
    LIVE = 6
    BUSINESS = 7
    LAW = 8
    DOCTOR = 9
    TRAIN = 10
    OLD = 11
    SHOPPING = 12
    FASHION = 13
    JOB = 14

    CATEGORY_CHOICES = (
        (MEISHI, u'餐饮美食'),
        (XIUXIAN, u'休闲娱乐'),
        (CAR,  u'汽车服务'),
        (AIRPORT,  u'接送机票'),
        (HOUSE,  u'房产家居'),
        (LIVE,  u'生活服务'),
        (BUSINESS,  u'生意服务'),
        (LAW,  u'财会法律'),
        (DOCTOR,  u'医疗保健'),
        (TRAIN,  u'教育培训'),
        (OLD,  u'商城二手'),
        (SHOPPING, u'商场购物'),
        (FASHION, u'时尚美容'),
        (JOB, u'工作招聘'),
    )

    CA51 = 1
    VAN = 2
    YORKBBS = 3
    SOURCE_CHOICES = (
        (CA51, 'kb.51.ca'),
        (VAN, 'dianpu.vanpeople.com'),
        (YORKBBS, 'info.yorkbbs.ca'),
    )

    category = models.IntegerField(
        verbose_name=u'分类',
        default=MEISHI,
        choices=CATEGORY_CHOICES,
    )

    name = models.CharField(
        verbose_name=u'名称',
        max_length=255,
    )

    tel = models.CharField(
        verbose_name=u'电话',
        max_length=100
    )

    address = models.CharField(
        verbose_name=u'地址',
        max_length=200,
    )

    opentime = models.CharField(
        verbose_name=u'营业时间',
        max_length=200,
    )
    
    district = models.CharField(
        verbose_name=u'商圈',
        max_length=30,
    )

    source = models.IntegerField(
        verbose_name=u'来源',
        default=CA51,
        choices=SOURCE_CHOICES,
    )

    created_date = models.DateTimeField(
        verbose_name=u'创建时间',
        auto_now=True,
    )

    class Meta:
        db_table = 'shop'
        verbose_name = u'商家'
        verbose_name_plural = u'商家'



