from urllib.request import urlopen
from urllib import robotparser
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import utils

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
        self.__initialize_robots()
        self.internal_page = []
        self.new_site = []

    def run_scraping(self, remove_picture = True):
        self.internal_page = self.site_map()
        self.new_site = self.scrap_new_link()
        if remove_picture:
            self.remove_picture()
        return self.internal_page, self.new_site

    def __initialize_robots(self):
        # Check if the robots.txt of the given website allows us to scrap
        self.robotcheck = robotparser.RobotFileParser()
        self.robotcheck.set_url(self.main_url + "/robots.txt")
        self.robotcheck.read()

    def site_map(self):
        pages_list = []
        site_map = self.robotcheck.site_maps()
        if site_map is not None:
            for site_map in site_map:
                pages_list.append(self.scrap_page(site_map))
            pages_list = set(utils.flatten(pages_list))
            return(pages_list)
        else :
            # No site-map so we return nothing
            return([])

    def scrap_page(self,page_url : str):
        """
        # Scrap a given page to find new urls

        Returns : a list of all the url found
        """
        try:
            webpage= urlopen(page_url).read().decode('utf-8')
            url_extract_pattern = 'https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)'
            # url_test = '"((http|ftp)s?://.*?)"'
            findPatLink=re.findall(
                url_extract_pattern
                ,webpage)
            return(findPatLink)
        except Exception as e:
            return([])
    
    def remove_picture(self):
        """
        Remove all pages finishing with .png or .jpg
        """
        self.internal_page = [val for val in self.internal_page if not val.endswith(".png")]
        self.internal_page = [val for val in self.internal_page if not val.endswith(".jpg")]

    def scrap_new_link(self):
        """
        Return the main url of all the new websites found in the current main url explored
        """
        if self.robotcheck.can_fetch('*',self.main_url):
            website_list = self.scrap_page(self.main_url)
            website_list = [ x for x in website_list if self.main_url not in x ]
            parsed_list = []
            for website in website_list:
                domain = urlparse(website)
                parsed_list.append(domain.scheme +"://" + domain.netloc)
            parsed_list = set(parsed_list)
            return(parsed_list)
        else :
            # Not allowed to scrap the website, returns nothing
            return([])
