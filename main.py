# TODO : create a main.py demo
from sitescraper import SiteScrapper


test = SiteScrapper("https://ensai.fr/")
website_list, empty_list= test.run_scraping()
print(website_list)
