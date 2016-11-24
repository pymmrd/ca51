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
    items_xpath = "//ol[@class='mainList-item']"
    title_xpath = "child::li/h2/a"
    tel_xpath = "child::li/div/ul[@class='item-cont']/li[@class='item-cont-phone']/font"
    addr_xpath = "child::li/div/ul[@class='item-cont']/li[@class='item-cont-address']"
    dist_xpath = ""
    time_xpath = ""

    def run(self, url, source, category):
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
                        category=category,
                        source=source
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
        category = 4 
        source = 3
        url = "http://info.yorkbbs.ca/default/%E6%8E%A5%E9%80%81%E6%9C%BA%E7%A5%A8"
        people = VanPeople()
        people.run(url, source, category)
        #for page in range(start, end+1):
        #    page_url = url % page
        #    print "Crawl: %s" % page_url
        #    people.run(page_url)
