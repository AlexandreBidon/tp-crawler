# TODO : create a main.py demo
from sitescraper import SiteScrapper
from crawler import Crawler
import utils

test1 = "https://help.twitter.com"
test2 = "https://ensai.fr"

crawler = Crawler(max_websites=100)

pages_found = crawler.run(test2)

utils.list_to_txt(url_list= pages_found, filename= "results/test.txt")