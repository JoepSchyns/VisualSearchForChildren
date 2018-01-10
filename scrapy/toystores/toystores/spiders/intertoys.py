import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from toystores.items import ToystoresItem

class IntertoysSpider(CrawlSpider):
    name = 'intertoys'
    allowed_domains = ['intertoys.nl']
    start_urls = ['https://www.intertoys.nl']

    rules = (
        # Main menu
        Rule(
            LinkExtractor(
                allow=("^https://www\.intertoys\.nl/c/",),
                restrict_xpaths=("//nav[@class='megamenu']",),
                unique=True,
                canonicalize=True,
            )
        ),
        # Pagination of categories
        Rule(
            LinkExtractor(
                allow=("^https://www\.intertoys\.nl/c/",),
                restrict_xpaths=("//div[@id='pagination']",),
                unique=True,
                canonicalize=True,
            )
        ),
        # Actual products
        Rule(
            LinkExtractor(
                allow=("^https://www\.intertoys\.nl/p/",),
                restrict_xpaths=("//div[@id='hits']",),
                unique=True,
                canonicalize=True,
            ),
            callback="parse_product"
        )
    )    

    def parse_product(self, response):
        l = ItemLoader(item=ToystoresItem(), response=response)
        l.add_xpath('name', "normalize-space(//h1[@class='ui header pdp']/div[1]/text())")
        l.add_xpath('price', "concat(normalize-space(//div[@class='ui price']/text()),normalize-space(//div[@class='ui price']/span/text()))")
        urls = response.xpath("//div[contains(@class,'pdp') and contains(@class,'thumb')]//img/@src").extract()
        urls = ['https://www.intertoys.nl' + url.replace('thumb', 'full') for url in urls]
        l.add_value('image_urls', urls)
        # referer = response.request.headers.get('Referer', '')
        # # referer = referer.split('/')
        # l.add_value('category', type(referer)) #[referer[-3], referer[-2]])
        return l.load_item()

    # def parse(self, response):
    #     pass
