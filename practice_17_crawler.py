import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
title = soup.find_all(class_= 'story-heading')

all_title = []
for t in title:	
	x = t.get_text().replace("\n", " ").strip()
	all_title.append(x)


with open('news_headline.csv', 'w') as open_file:
	open_file.write(str(all_title))