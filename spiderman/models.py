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
    #
    LMEISHI = 15
    DICHAN = 16
    LAWER = 17
    TOUR = 18
    CDOCTOR = 19
    INS = 20
    HFIANCE = 21
    YUEZI = 22
    CAR2 = 23
    KUAIDI = 24
    BANJIA = 25
    TOUR2 = 26
    JIAZHU = 27
    HTOUR3 = 28
    CAR_Z = 29
    CAR_W = 30
    LIUXUE = 31
    CAMERA = 32
    CLEAN = 33
    BANK = 34
    HAIR = 35



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
        (LMEISHI, u'洛杉矶美食'),
        (DICHAN, u'地产经纪'),
        (LAWER, u'华人律师'),
        (TOUR, u'华人旅行社'),
        (CDOCTOR, u'华人医生'),
        (INS, u'保险经纪'),
        (HFIANCE, u'华人会计师'),
        (YUEZI, u'月子中心'),
        (CAR2, u'驾驶教练/学校'),
        (KUAIDI, u'快递公司'),
        (BANJIA, u'搬家公司'),
        (TOUR2, u'洛杉矶旅游'),
        (JIAZHU, u'建筑装修/建筑师 '),
        (HTOUR3, u'华人旅游接送'),
        (CAR_Z, u'汽车租赁'),
        (CAR_W, u'汽车维修'),
        (LIUXUE, u'留学服务'),
        (CAMERA, u'照相馆'),
        (CLEAN, u'清洁公司'),
        (BANK, u'贷款银行/代理'),
        (HAIR, u'美容美发'),
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

    address2 = models.CharField(
        verbose_name=u'地址',
        max_length=200,
    )

    address3 = models.CharField(
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
