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
    items_xpath = "//ul[@class='item-cont']"
    title_xpath = "child::li/h2/a"
    tel_xpath = "child::li[@class='item-cont-pin']/p/font"
    addr_xpath = "child::li[@class='item-cont-address']"
    dist_xpath = ""
    time_xpath = ""

    def run(self, url):
        etree = self.get_elemtree(url)
        items = etree.xpath(self.items_xpath)
        for item in items:
            try:
                title_dom = item.xpath(self.title_xpath)[0]
                #href = title_dom.attrib['href']
                #detail_link = self.normalize_url(url, href)
                title = title_dom.text_content().strip()

                tel = ''
                tel_dom = item.xpath(self.tel_xpath)
                if tel_dom:
                    tel = tel_dom[0].text_content().strip()

                addr = ''
                addr_dom = item.xpath(self.addr_xpath)
                if addr_dom:
                    addr = addr_dom[0].text_content().strip()

                dist = ""
                dis = addr.rsplit(',', 2)
                if len(dis) == 3:
                    dist = dis[1]

                open_time = ''

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
                        category=1,
                        source=3
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
        url = "http://dianpu.vanpeople.com/item-list-catid-1-aid-0-order-score-type-normal-num-20-total-3389-page-%s.html"
        people = VanPeople()
        for page in range(start, end+1):
            page_url = url % page
            print "Crawl: %s" % page_url
            people.run(page_url)
