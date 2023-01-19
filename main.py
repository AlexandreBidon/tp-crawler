from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

webpage=urlopen('https://ensai.fr/').read().decode('utf-8')

findPatLink=re.findall('"((http|ftp)s?://.*?)"',webpage)
print(findPatLink)
