# TODO : create a main.py demo
from sitescraper import SiteScrapper


test = SiteScrapper("https://ensai.fr/")
website_list = test.site_map()
print(len(website_list))
