#!python3
#download.py

#中一英単語download

import requests, os, bs4, csv
url = 'https://eigo-duke.com/tango/chu1.html'
os.makedirs('English', exist_ok=True)
print('ページをダウンロード中 {}...'.format(url))
res = requests.get(url)
#errorチェック
res.raise_for_status()
# print(res.content)
soup = bs4.BeautifulSoup(res.content, 'lxml')
word_elem = soup.find('table', class_='table')

word_set = soup.select('.table tr')

words = []
if word_set == []:
    print('英単語が見つかりませんでした')
else:
    for i in range(len(word_set)-1):
        if word_set[i].select('.jap') == []:
            continue
        else:
            jp_word = word_set[i].select('.jap')[0].text
            en_word = word_set[i].select('.eng')[0].text
            words.append([en_word, jp_word])
    print('英単語ダウンロード完了')

print(words)
os.makedirs('words', exist_ok=True)
file = open('words/word2.csv', 'w')    #既存でないファイル名を作成してください

w = csv.writer(file)
w.writerows(words)

file.close()
