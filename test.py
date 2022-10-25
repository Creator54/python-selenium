from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://google.com')

search = browser.find_element(By.NAME, 'q')
search.send_keys('seleniumhq' + Keys.RETURN)
