import scrapy
import json
import csv
from scrapy.crawler import CrawlerProcess

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

class AnnapurnaPostSpider(scrapy.Spider):
    name = "AnnapurnaPost"
    base_url = "https://bg.annapurnapost.com/api/search?title=%E0%A4%96%E0%A5%87%E0%A4%B2%E0%A4%95%E0%A5%81%E0%A4%A6"
    # custom headers
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }

    posts = {'data':[]}

    urls_dicts = []

    # crawler's entry point
    def start_requests(self):
        yield scrapy.Request(
            url = self.base_url,
            headers = self.headers,
            callback = self.parse
        )
    
    def load_csv(self):
        urls_dicts = []
        urls = []
        with open('urls.csv') as file:
            for line in csv.DictReader(file):
                self.urls_dicts.append(line)
        for url_dict in self.urls_dicts:
            urls.append(url_dict['urls'])

        return urls

    def parse(self, response):
        
        urls = self.load_csv()

        data = json.loads(response.body)
        items = data['data']['items']

        # Content is loading sending ajax request so extracting totalpage number of pages to extract all posts related to that search
        totalpage = data['data']['totalPage']

        for index in range(len(items)):
            # To extract every information of that post
            #self.posts['data'].append(items[index])

            # To extract only title of that post
            self.posts['data'].append(items[index]['title'])

        
        information ={'data':self.posts, 'len':len(self.posts['data'])}
        yield information
        
        #urls = ["http://www.httpbin.org/status/404",self.base_url+f"&page=2"]
        for page in range(1,totalpage+1):
        #for url in urls:
            url = self.base_url + f"&page={page}"
            if url in urls:
                continue
            else:
                self.urls_dicts.append({'urls':url})
                with open('urls.csv','a') as file:
                    writer = csv.DictWriter(file, fieldnames=['urls'])
                    writer.writerow({'urls':url})

                request = scrapy.Request(url=url, headers=self.headers, callback= self.parse,errback=self.errback_httpbin)
            #request = scrapy.Request(url=url, headers=self.headers, callback= self.parse,)

                yield request

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)


if __name__=='__main__':
    #run spider
    process = CrawlerProcess()
    process.crawl(AnnapurnaPostSpider)
    process.start()

