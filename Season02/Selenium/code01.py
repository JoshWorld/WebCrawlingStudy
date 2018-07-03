
from selenium import webdriver

browser = webdriver.Chrome("/Users/itaegyeong/Desktop/2018spring/webcrawling/Season02/Selenium/chromedriver")
browser.get("http://naver.com")

id_text = browser.find_element_by_css_selector('#id')
pw_text = browser.find_element_by_css_selector('#pw')

button = browser.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span/input')

id_text.send_keys("test_id")
pw_text.send_keys("testpassword")
button.click()

