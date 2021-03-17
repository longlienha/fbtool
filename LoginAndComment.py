from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver


def loginFB(user = "longlienha20@gmail.com", password="l0nglienha",url="https://m.facebook.com/"):
    
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)

    # open fb
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)
    sleep(5)
    #login
    txtUser = browser.find_element_by_id("m_login_email")
    txtUser.send_keys(user)

    txtPass = browser.find_element_by_id("m_login_password")
    txtPass.send_keys(password)

    txtPass.send_keys(Keys.ENTER)
    sleep(5)
    return browser

def getPage(url, browser):
    browser.get(url)
    return browser


