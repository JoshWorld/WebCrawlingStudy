from selenium import webdriver

browser = webdriver.Chrome("/Users/itaegyeong/Desktop/webcrawling/Season02/Selenium/chromedriver")
browser.get("https://www.instagram.com/accounts/login/")

id_text = browser.find_element_by_name("username")
pw_text = browser.find_element_by_name("password")

button = browser.find_element_by_tag_name("button")

id_text.send_keys("test_id")
pw_text.send_keys("testpassword")
button.click()

