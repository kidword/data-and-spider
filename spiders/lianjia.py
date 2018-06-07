import scrapy
import re
import time
from Fangyuan.items import FangyuanItem
class FanyuanSpider(scrapy.Spider):
    name = 'lianjia'
    start_urls = [
            'https://bj.5i5j.com/zufang/yanqing/'
         ]

    def parse(self, response):
        news_herf = response.css("div.pListBox.mar.main > div.lfBox.lf > div.list-con-box > ul > li > div.listCon > h3 > a::attr('href')").extract()
        #print(news_herf)
        for href in news_herf:
            allhref = 'https://bj.5i5j.com'+href
            yield response.follow(allhref,self.deatil)

        #next_page = response.css(' div.pageBox > div.pageSty.rf > a.cPage::attr("href")').extract_first()

        next_page = response.css('div.lfBox.lf > div.pageBox > div.pageSty.rf > a.cPage::attr("href")').extract_first()
        allpage = 'https://bj.5i5j.com' + next_page
        if next_page is not None:

            yield response.follow(next_page, self.parse)
        #n = allpage[:38]
        # for i in range(1,73):
        #     N = allpage + str(i)
        #     S ='https://bj.5i5j.com/zufang/xichengqu/n73'
        #     if N==S:
        #         break
        # yield response.follow(N,self.parse)

    def deatil(self,response):
            xiaoqu = response.css('div.content.fr > div.zushous > ul > li:nth-child(1) > a::text').extract_first()
            jiage = response.css('div.content.fr > div.housesty > div.jlyou.fl > div > p.jlinfo::text').extract_first()
            mianji = response.css('div.content.fr > div.housesty > div:nth-child(3) > div > p.jlinfo::text').extract_first()
            fukuan = response.css('div.content.fr > div.housesty > div:nth-child(4) > div > p.jlinfo.font18::text').extract_first()
            zhuangxiu = response.css('div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-child(4)::text').extract_first()
            louceng = response.css('div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-child(2)::text').extract_first()
            chuzu = response.css('div.details-view.clear > div.content.fr > div.zushous > ul > li:nth-child(6)::text').extract_first()
            ditie = response.css('div.details-view.clear > div.content.fr > div.zushous > ul > li.traffic::text').extract_first()
            item = FangyuanItem()
            #time.sleep(0.5)
            item['xiaoqu'] = xiaoqu
            item['jiage' ]= jiage
            item['mianji'] = mianji
            item['fukuan'] = fukuan
            item['zhuangxiu'] =zhuangxiu
            item['louceng'] = louceng
            item['chuzu'] = chuzu
            item['ditie'] = ditie
            yield item
