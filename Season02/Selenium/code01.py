from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome("/Users/itaegyeong/Desktop/webcrawling/chromedriver")
browser.get("https://www.instagram.com/accounts/login/")

id_text = browser.find_element_by_name("username")
pw_text = browser.find_element_by_name("password")

id_text.send_keys("test")
pw_text.send_keys("passwordtest")

login_button = browser.find_element_by_tag_name('button').click()

time.sleep(3)
