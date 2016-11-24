# -*- coding:utf-8 -*-


# StdLib imports
import traceback
from optparse import make_option

# Django imports
from django.core.management.base import BaseCommand

# Project imports
from spiderman.models import Shop
from base import CreeperBase


class VanPeople(CreeperBase):
    items_xpath = "//dd/ul[@class='detail']"
    title_xpath = "child::li[@class='shopname']/a[1]"
    tel_xpath = "child::li[@class='address'][2]"
    addr_xpath = "child::li[@class='address'][1]"
    dist_xpath = "child::li[@class='address'][1]/a[@class='Black-h']"
    time_xpath = "//address/p[last()]"

    def run(self, url):
        etree = self.get_elemtree(url)
        items = etree.xpath(self.items_xpath)
        for item in items:
            try:
                title_dom = item.xpath(self.title_xpath)[0]
                href = title_dom.attrib['href']
                detail_link = self.normalize_url(url, href)
                title = title_dom.text_content().strip()

                tel = ''
                tel_dom = item.xpath(self.tel_xpath)
                if tel_dom:
                    tel = tel_dom[0].text_content().strip()

                addr = ''
                addr_dom = item.xpath(self.addr_xpath)
                if addr_dom:
                    addr = addr_dom[0].text_content().strip()

                dist = ''
                dist_dom = item.xpath(self.dist_xpath)
                if dist_dom:
                    dist = dist_dom[0].text_content().strip()

                open_time = ''
                try:
                    dtree = self.get_elemtree(detail_link)
                    open_dom = dtree.xpath(self.time_xpath)
                    if open_dom:
                        raw_string = open_dom[0].text_content().strip()
                        if raw_string.startswith(u'营业时间'):
                            open_time = raw_string.split(u': ', 1)[-1]
                except:
                    pass

                try:
                    shop = Shop.objects.get(
                        name=title,
                        address=addr,
                    )
                except:
                    shop = Shop(
                        name=title,
                        address=addr,
                        tel=tel,
                        district=dist,
                        opentime=open_time,
                        category=2,
                        source=2,
                    )
                    shop.save()
            except Exception:
                print traceback.print_exc()
                print 'Error: %s' % url.encode('utf-8')


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--start', dest='start'),
        make_option('--end', dest='end'),
    )

    def handle(self, **options):
        start = int(options.get('start'))
        end = int(options.get('end'))
        url = "http://dianpu.vanpeople.com/item-list-catid-16-aid-0-order-score-type-normal-num-20-total-495-page-%s.html"
        people = VanPeople()
        for page in range(start, end+1):
            page_url = url % page
            print "Crawl: %s" % page_url
            people.run(page_url)
