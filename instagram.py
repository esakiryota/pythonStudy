#!python3
#download.py

import requests, os, bs4
url = 'https://www.instagram.com/natsukoakahani/?hl=ja'
os.makedirs('insta', exist_ok=True)
print('ページをダウンロード中 {}...'.format(url))
res = requests.get(url)
#errorチェック
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
img_elem = soup.select('.FyNDV img')
if img_elem == []:
    print('画像が見つかりませんでした')
else:
    for i in range(30):
        img_url = 'http:' + img_elem[i].get('src')
        print('画像をダウンロード中 {}...'.format(img_url))
        img_res = requests.get(img_url)
        img_res.raise_for_status()
        image_file = open(os.path.join('insta', os.path.basename(img_url)), 'wb')
        for chunk in img_res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
    print('完了')
