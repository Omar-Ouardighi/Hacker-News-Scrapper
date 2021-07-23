import requests
from bs4 import BeautifulSoup
import csv

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

csv_file = open('hn_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Link', 'Votes'])


def create_costum_hn(links,subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                
                csv_writer.writerow([title, href, points])


create_costum_hn(links,subtext)

csv_file.close()
