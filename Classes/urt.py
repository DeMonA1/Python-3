import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        with open("parser.txt", 'w') as f:
            for tag in sp.find_all('a'):
                url = tag.get('href')
                if url is None:
                    continue
                if 'html' in url:
                    f.write(url + '\n')    
                    print("\n" + url)
news = "https://oz.by"
Scraper(news).scrape()

