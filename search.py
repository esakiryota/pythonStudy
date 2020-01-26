#! python3
# search.py
import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=ワンパンマン')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select('.r a')
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))
