# -*- coding:utf-8 -*-


# StdLib imports
import traceback
from optparse import make_option

# Django imports
from django.core.management.base import BaseCommand

# Project imports
from spiderman.models import Shop
from base import CreeperBase


class Kb51(CreeperBase):
    items_xpath = "//div[@id='tab_all_div']/ul/li"
    title_xpath = "descendant::div[@class='tit']/a"
    tel_xpath = "descendant::p[@class='phone']/span[last()]"
    addr_xpath = "descendant::p[@class='addr']/span[2]"
    dist_xpath = "descendant::p[@class='itemtags']/a[last()]"
    time_xpath = "//div[@class='todayhours']/b[@class='enfont']"

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
                        open_time = open_dom[0].text_content().strip()
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
        url = "http://kb.51.ca/item/list-catid-1-aid-0-type-normal-num-15-total-1847-page-%s"
        kb51 = Kb51()
        for page in range(start, end+1):
            page_url = url % page
            print "Crawl: %s" % page_url
            kb51.run(page_url)
