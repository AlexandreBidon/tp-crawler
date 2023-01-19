from urllib.request import urlopen
from urllib import robotparser
from bs4 import BeautifulSoup
import re


class SiteScrapper():
    """
    Given an entry point and a number of pages to return, 
    this class will scrap all website it is allowed to scrap 
    in order to find new pages

    Returns :
    Two lists
    page_found : all the page found in the website that where allowed by robots.txt
    external_site : list of all the other websites. Those sites were not checked by robots.txt
    """

    def __init__(
        self
        ,main_url : str):

        self.main_url = main_url
        self.__initialize_robots(self.main_url)

    def __initialize_robots(self, main_url : str):
        # Check if the robots.txt of the given website allows us to scrap
        self.robotcheck = robotparser.RobotFileParser()
        self.robotcheck.set_url(self.main_url + "/robots.txt")
        self.robotcheck.read()

    def site_map(self):
        return self.robotcheck.site_maps()

    def extract_site_page(self):
        """
        # Return all the pages present in the sitemap of a given website
        Only returns the pages that are allowed by the robots.txt
        """
        
        pass

    def scrap_page(page_url : str):
        """
        # Scrap a given page to find new urls

        Returns : a list of all the url found
        """
        webpage=urlopen(page_url).read().decode('utf-8')
        findPatLink=re.findall('"((http|ftp)s?://.*?)"',webpage)
        return(findPatLink)

        
    