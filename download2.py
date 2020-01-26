#!python3
#download.py
import requests, sys, webbrowser, bs4, os

print('Googling...')
os.makedirs('画像', exist_ok=True)
url = 'http://google.com/search?q=ワンパンマン'
res = requests.get('http://google.com/search?q=ワンパンマン')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")
res = requests.get(url)
img_elem = soup.select('a')
len(img_elem)
img_url = img_elem[5].get('href')
print(img_url)
img_res = requests.get('http://www.google.com' + img_url)
print(img_res)
