# -*- coding:utf-8 -*-

# StdLib imports
import time
import random
import urllib2
import requests
import urlparse
from lxml.html import fromstring


class CreeperBase(object):
    USER_AGENTS = [(
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) "
        "Gecko/20071127 Firefox/2.0.0.11"), (
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.17) "
        "Gecko/20110422 Ubuntu/10.04 (lucid) Firefox/3.6.17"),
        'Opera/9.25 (Windows NT 5.1; U; en)',
    ]

    MAX_RETRY_TIMES = 3
    DEFAULT_CHARSET = 'utf-8'
    charset = DEFAULT_CHARSET

    def __init__(self):
        self.session = requests.session()
        self.session.headers['User-Agent'] = random.choice(self.USER_AGENTS)

    def tryAgain(self, req, retries=0):
        """
         尝试最大次数(MAX_RETRY_TIMES)后请求退出
        """
        content = ''
        if retries < self.MAX_RETRY_TIMES:
            try:
                time.sleep(5)
                content = urllib2.urlopen(req).read()
            except:
                retries += 1
                content = self.tryAgain(req, retries)
        return content

    def get_content(self, url, data=None, timeout=3*60):
        """
        给请求加载USER-AGENT, 获取页面内容，
        """
        content = ''
        try:
            if data is not None:
                ack = self.session.post(url, data, timeout=timeout)
            else:
                ack = self.session.get(url, timeout=timeout)
            content = ack.content
        except:
            pass
        return content

    def normalize_url(self, source, url):
        """
        >>> urlparse.urljoin('http://www.baidu.com/?a=1', '/page/1?query=a')
            http://www.baidu.com/page/1?query=a
        >>> urlparse.urljoin('http://www.baidu.com/?a=1',
                'http://www.baidu.com/page/1?query=a')
            http://www.baidu.com/page/1?query=a
        """
        return urlparse.urljoin(source, url)

    def get_elemtree(self, url, data=None, ignore=False, charset=False):
        """
        生成dom树方便xpath分析
        """
        etree = None
        content = self.get_content(url, data)
        if charset:
            content = content.decode(self.charset)
        if ignore:  # 针对页面存在错误编码和多编码现象处理
            content = content.decode(self.charset, 'ignore')
        if content:
            try:
                etree = fromstring(content)
            except:
                pass
        return etree

    def __del__(self):
        self.session.close()
