import scrapy
from time import sleep
from selenium import webdriver

class WebCrawler(scrapy.Spider):
    name = 'crawler'
    start_urls = ['https://maxbet.rs']

    def parse(self, response):
        driver = webdriver.Firefox()
        driver.get('https://maxbet.rs')
        sleep(8)

        matchs = driver.find_elements_by_class_name('home-game')
        with open('results.csv', 'w+') as f:
            for match in matchs:
                f.write(match.text)
        driver.close()