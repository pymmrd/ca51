# -*- coding:utf-8 -*-

import StringIO

# ThirdParty imports
import xlwt

from django.contrib import admin
from django.http import HttpResponse

from spiderman.models import Shop


def output_shop(modeladmin, request, queryset):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('Sheet1')
    sheet.write(0, 0, label=u'名称')
    sheet.write(0, 1, label=u'电话')
    sheet.write(0, 2, label=u'地址')
    sheet.write(0, 3, label=u'开业时间')
    sheet.write(0, 4, label=u'商圈')
    sheet.write(0, 5, label=u'分类')
    sheet.write(0, 6, label=u'来源')
    queryset = Shop.objects.all()
    row = 1
    for item in queryset:
        sheet.write(row, 0, item.name)
        sheet.write(row, 1, item.tel)
        sheet.write(row, 2, item.address)
        sheet.write(row, 3, item.opentime)
        sheet.write(row, 4, item.district)
        sheet.write(row, 5, dict(Shop.CATEGORY_CHOICES)[item.category])
        sheet.write(row, 6, dict(Shop.SOURCE_CHOICES)[item.source])
        row += 1
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment;filename=shop.xls'
    output = StringIO.StringIO()
    workbook.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response
output_shop.short_description = u'导出商店'


class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'tel', 'address', 'opentime',
        'district',  'category', 'created_date', 'source'
    )
    actions = [
        output_shop,
    ]

admin.site.register(Shop, ShopAdmin)
