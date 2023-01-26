import utils
from sitescraper import SiteScrapper

class Crawler():

    def __init__(self, max_websites : int):
        self.max_websites = max_websites

    def run(self, entrypoint_url : str):
        self.already_visited = []
        self.to_visit = [entrypoint_url]
        self.pages_found = []
        for website_url in self.to_visit:
            website_url = utils.url_to_main(website_url)
            print("crawl " + website_url)
            new_pages, new_sites = SiteScrapper(website_url).run_scraping()
            print("Found " + str(len(new_pages)) + " new pages")
            self.already_visited.append(website_url)
            self.pages_found += new_pages
            self.to_visit += [ x for x in new_sites if x not in self.to_visit ]
            print("visited : " + str(len(new_pages)))
            if len(self.pages_found) >= self.max_websites:
                print("stop")
                break
        return(self.pages_found)