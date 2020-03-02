import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.google.com/search?q=dog&source=lnms&tbm=isch']


    selector = ".rg_ic.rg_i"

    def parse(self, response):

        images = []

        # for img in response.css('img'):
        #     images.append({'url': img.attrib['src']})

        print("-------------------------------------------------------------")
        print(len(response.css('imgs')))
        print("-------------------------------------------------------------")

        return images

        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)