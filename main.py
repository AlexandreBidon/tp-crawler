# TODO : create a main.py demo
from sitescraper import SiteScrapper
from crawler import Crawler

test1 = "https://help.twitter.com"
test2 = "https://ensai.fr"
# test = SiteScrapper(test1)
# website_list, new_list= test.run_scraping()

# print(len(website_list))
# print(new_list)

crawler = Crawler(max_websites=8)

pages_found = crawler.run(test2)

print(pages_found)