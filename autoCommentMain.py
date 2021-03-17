from LoginAndComment import *
from commentHelper import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

linkFile = "listUrlPage.txt"
listPage = getPageFromFile(linkFile)

browser = loginFB()
browser = getPage(listPage[3].urlPage,browser)
comments = browser.find_elements_by_class_name("_15kq._77li")
print(len(comments))
while listPage[3].indexPost > len(comments):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(0.5)
    comments = browser.find_elements_by_class_name('_15kq._77li')
print(len(comments))
sleep(5)
indexPost = 0
while indexPost != listPage[3].indexPost:
    comments = browser.find_elements_by_class_name('_15kq._77li')
    comments[indexPost].click()
    sleep(5)
    if browser.find_elements_by_css_selector("#composerInput") == []:
        backPage = browser.find_element_by_css_selector("#MBackNavBar")
        backPage.click()
        sleep(5)
    else:
        textComment = browser.find_element_by_css_selector("#composerInput")
        textComment.send_keys("huulong")
        sleep(2)
        backPage = browser.find_element_by_css_selector("#MBackNavBar")
        backPage.click()
        sleep(2)

    indexPost = indexPost + 1


# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)

# # open fb
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.get("https://m.facebook.com/")
# sleep(5)
# #login
# txtUser = browser.find_element_by_id("m_login_email")
# txtUser.send_keys("longlienha20@gmail.com")

# txtPass = browser.find_element_by_id("m_login_password")
# txtPass.send_keys("l0nglienha")

# txtPass.send_keys(Keys.ENTER)
# sleep(5)

# for page in listPage:
#     browser.get(page.urlPage)
#     comments = browser.find_elements_by_class_name('_15kq._77li')
#     while page.indexPost > len(comments):
#         browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#         sleep(0.5)
#         comments = browser.find_elements_by_class_name('_15kq._77li')
#     print(len(comments))
#     sleep(5)
#     comments[1].click()
    
#     sleep(5)
#     if browser.find_elements_by_css_selector("#composerInput") == []:
#         backPage = browser.find_element_by_css_selector("#MBackNavBar")
#         backPage.click()
#     else:
#         textComment = browser.find_element_by_css_selector("#composerInput")
#         textComment.click()
#         sleep(30)
    
# sleep(30)
# browser.close()

