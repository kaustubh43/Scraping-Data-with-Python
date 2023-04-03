import requests
from bs4 import BeautifulSoup
from pprint import pprint


def create_link_subtext(hn_link):
    res = requests.get(hn_link)  # Analogous to a web browser without a window
    soup = BeautifulSoup(res.text, 'html.parser')  # Soup object
    links_func = soup.select('.titleline')
    subtext_func = soup.select('.subtext')
    return links_func, subtext_func


def sort_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


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
    return sort_by_votes(hn)


# Home page follows a particular pattern, end of link contains the page number
HOME_PAGE = 'https://news.ycombinator.com/?p='
n = int(input('How many pages do you want to scrape from Hacker News: '))
links, subtext = [], []

# Getting all links and subtext in one place and appending to lists
for i in range(n):
    temp = create_link_subtext(HOME_PAGE + str(i+1))
    links += temp[0]
    subtext += temp[1]

# Sending to scrape
x = create_custom_hn(links, subtext)
pprint(x)
pprint(f'{len(x)} links were scraped')
