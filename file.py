import os

# print(os.path.join('usr', 'bin', 'spam'))
# print(os.getcwd())
# hello_file = open('/Users/esakiryota/Desktop/scraping/hello.txt')
# hello_content = hello_file.read()
# print(hello_content)
# write_file = open('/Users/esakiryota/Desktop/scraping/hello.txt', 'a')
# read_file = open('/Users/esakiryota/Desktop/scraping/hello.txt')
# write_file.write('hello world')
# read_content = read_file.read()
# print(read_content)

import shelve
shelf_file = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats
print(type(shelf_file))
print(shelf_file['cats'])
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()
