import urllib.request

url = "https://uta.pw/shodou/img/28/214.png"
savename = "test1.png"

# urllib.request.urlretrieve(url, savename)
# print("保存しました")

mem = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f:
    f.write(mem)
    print("保存しました")
