from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url='http://radiofrance-podcast.net/podcast09/rss_10212.xml'

uClient = ureq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("guid")

filename = "latac.csv"
f = open(filename, "w")


for container in containers:
	print(container.text)
	f.write(container.text + "\n")