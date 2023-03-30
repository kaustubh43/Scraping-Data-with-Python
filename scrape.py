import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')  # Analogous to a web browser without a window
soup = BeautifulSoup(res.text, 'html.parser')  # Soup object
links = soup.select('.titleline')
subtext = soup.select('.subtext')


def create_custom_hn(link, vote):
    hn = []
    for idx, item in enumerate(link):
        title = link[idx].getText()
        a_tags = link[idx].find("a")  # Finds all the <a> tags within which the links reside
        href = a_tags.get('href')  # Extract the link from the a tag
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn


x = create_custom_hn(links, subtext)
pprint.pprint(x)
