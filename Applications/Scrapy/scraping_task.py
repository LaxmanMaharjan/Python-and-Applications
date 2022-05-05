import scrapy
import json
from scrapy.crawler import CrawlerProcess

class AnnapurnaPostSpider(scrapy.Spider):
    name = "AnnapurnaPost"
    base_url = "https://bg.annapurnapost.com/api/search?title=%E0%A4%96%E0%A5%87%E0%A4%B2%E0%A4%95%E0%A5%81%E0%A4%A6"
    # custom headers
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    }

    posts = {'data':[]}

    # crawler's entry point
    def start_requests(self):
        yield scrapy.Request(
            url = self.base_url,
            headers = self.headers,
            callback = self.parse
        )
    
    def parse(self, response):
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
        
        for page in range(1,totalpage+1):
            url = self.base_url + f"&page={page}"
            request = scrapy.Request(url=url, headers=self.headers, callback= self.parse)
            yield request



if __name__=='__main__':
    #run spider
    process = CrawlerProcess()
    process.crawl(AnnapurnaPostSpider)
    process.start()

