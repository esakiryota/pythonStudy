# -*- coding: utf-8 -*-
import scrapy, pprint
from ..selenium_middleware import *

USER = "ryota"
PASS = "esaki1217"

class GetallSpider(scrapy.Spider):
    name = 'getall'
    # allowed_domains = ['uta.pw']
    # start_urls = ['http://uta.pw/']
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES" : {
            "sakusibbs.selenium_middleware.seleniumMiddleware": 0
        }
    }

    def start_requests(self):
        url = 'https://uta.pw/sakusibbs/users.php?action=login'
        selenium_get(url)
        user = get_dom('#user')
        user.send_keys(USER)
        pw = get_dom('#pass')
        pw.send_keys(PASS)
        btn = get_dom('#loginForm input[type=submit]')
        btn.click()
        a = get_dom('.islogin a')
        mypage = a.get_attribute('href')
        print("mypage=", mypage)
        yield scrapy.Request(mypage, self.parse)

    def parse(self, response):
        alist = response.css('li a')
        print("alist=", alist)
        for a in alist:
            url = a.css('::attr(href)').extract_first()
            url2 = response.urljoin(url)
            yield response.follow(
                url2, self.parse_sakusin)

    def parse_sakusin(self, response):
        title = response.css('title::text').extract_first()
        print("---", title)
        src = response.css('iframe::attr(src)').extract_first()
        src2 = response.urljoin(src)
        req = scrapy.Request(src2, self.parse_download)
        req.meta["title"] = title
        yield req

    def parse_download(self, response):
        title = response.meta["title"]
        fname = title + ".html"
        with open(fname, "wt") as f:
            f.write(response.body)

    def closed(self, reason):
        selenium_close()
