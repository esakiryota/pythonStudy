#!python3
#autotweet.py

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# account = input('account:')
# password = input('password:')
account = 'AKpDbERJm5hZzUm'
password = 'esaki1217'
browser = webdriver.Chrome()
browser.get('https://twitter.com/login')
account_elem = browser.find_element_by_class_name('js-username-field')
account_elem.send_keys(account)
password_elem = browser.find_element_by_class_name('js-password-field')
password_elem.send_keys(password)
password_elem.submit()
browser.get('https://twitter.com/compose/tweet')
time.sleep(5)
content = browser.find_element_by_css_selector('div.public-DraftStyleDefault-block > span > br')
print(content)
content.send_keys(Keys.SHIFT, "python自動ツイート完了")
tweet = browser.find_element_by_css_selector('div.css-18t94o4.css-1dbjc4n.r-urgr8i')
tweet.click()
time.sleep(3)
