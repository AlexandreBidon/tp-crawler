# TODO : create a main.py demo
from urllib.request import urlopen
from sitescraper import SiteScrapper
import re
#test = SiteScrapper("https://ensai.fr")
#print(test.site_map())

def scrap_page(page_url : str):
        """
        # Scrap a given page to find new urls

        Returns : a list of all the url found
        """
        url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
        url_test = '"((http|ftp)s?://.*?)"'
        webpage=urlopen(page_url).read().decode('utf-8')
        findPatLink=re.findall(url_extract_pattern,webpage)
        return(findPatLink)


test = scrap_page("https://ensai.fr/page-sitemap.xml")
print(test)