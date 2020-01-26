#!python3
#selenium.py

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
email_elem = browser.find_element_by_id('identifierId')
email_elem.send_keys('esaki1217@gmail.com')
click_elem = browser.find_element_by_id('identifierNext')
click_elem.click()
