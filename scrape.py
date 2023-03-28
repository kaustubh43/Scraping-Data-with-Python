import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')  # Analogous to a web browser without a window
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find(id='score_35325693'))
