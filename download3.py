#!python3
#download.py

import requests, os, bs4
url = 'https://pixta.jp/free-items'
os.makedirs('pixta', exist_ok=True)
i = 0
while i < 2:
    #ページをダウンロード
    print('ページをダウンロード中 {}...'.format(url))
    res = requests.get(url)
    #errorチェック
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    #コミック画像のurlを見つける
    comic_elem = soup.select('img')
    len(comic_elem)
    i += 1
    if comic_elem == []:
        print('画像が見つかりませんでした。')
    else:
        for j in range(30):
            comic_url = comic_elem[j].get('src')
            #画像をダウンロードする
            print('画像をダウンロード中 {}...'.format(comic_url))
            res = requests.get(comic_url)
            #errorチェック
            res.raise_for_status()
            #画像を./xkcdに保存する
            image_file = open(os.path.join('pixta', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()
    #
    # prev_link = soup.select('a[rel="prev"]')[0]
    # url = 'http://xkcd.com' + prev_link.get('href')

print('完了')
