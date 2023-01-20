# TODO : create a main.py demo
from sitescraper import SiteScrapper

test1 = "https://help.twitter.com"
test2 = "https://ensai.fr"
test = SiteScrapper(test1)
website_list, new_list= test.run_scraping()

print(len(website_list))
print(new_list)