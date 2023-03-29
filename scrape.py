import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')  # Analogous to a web browser without a window
soup = BeautifulSoup(res.text, 'html.parser')  # Soup object
links = soup.select('.titleline')
votes = soup.select('.score')
print(votes[0].get('id'))

