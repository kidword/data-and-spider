from scrapy.cmdline import execute

if __name__ == '__main__':
    execute('scrapy crawl lianjia -o bejingqita_yanqing.csv'.split())