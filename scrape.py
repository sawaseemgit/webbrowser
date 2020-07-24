import sys
import pprint
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
alist = soup.select('.storylink')
subtext = soup.select('.subtext')

alist2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

combinedlist = alist + alist2
combinedsubtext = subtext + subtext2


# print(alist[0].get('id'))
def sort_by_votes(links):
    return sorted(links, key=lambda k: k['points'], reverse=True)


def custom_news(alist, subtext):
    links = []
    for idx, item in enumerate(alist):
        title = alist[idx].getText()
        href = alist[idx].get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                links.append({'title': title, 'link': href, 'points': points})
    print(len(links))
    return sort_by_votes(links)


# custom_news(alist, subtext)
pprint.pprint(custom_news(combinedlist, combinedsubtext))
# for i in alist:
#     print(str(i) + '\n')
