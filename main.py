# TODO : create a main.py demo
from urllib.request import urlopen
from sitescraper import SiteScrapper
import re

test = SiteScrapper("https://ensai.fr/")
print(test.site_map())
