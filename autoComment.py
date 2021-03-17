from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

#button = '#mount_0_0_yr > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.l9j0dhe7.dp1hu0rb.cbu4d94t.j83agx80 > div.j83agx80.cbu4d94t > div > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.qmfd67dx.hpfvmrgz.gile2uim.buofh1pr.g5gj957u.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5 > div:nth-child(2) > div:nth-child(2) > div:nth-child(8) > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div.cwj9ozl2.tvmbv18p > div.ecm0bbzt.hv4rvrfc.e5nlhep0.dati1w0a.j83agx80.btwxx1t3.lzcic4wl > div.g3eujd1d.ni8dbmo4.stjgntxs.rz4wbd8a > div > div > div > div > form > div > div > div._5rpb > div > div > div > div'
# block alert save password
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# open fb
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("https://m.facebook.com/")

#login
txtUser = browser.find_element_by_id("m_login_email")
txtUser.send_keys("longlienha20@gmail.com")

txtPass = browser.find_element_by_id("m_login_password")
txtPass.send_keys("l0nglienha")

txtPass.send_keys(Keys.ENTER)
sleep(5)

# open group
browser.get("https://m.facebook.com/groups/stylemobiles/")
sleep(5)
# find elements comment
comment = browser.find_elements_by_class_name('_15kq._77li')
postIndex = 100
while postIndex > len(comment):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    comment = browser.find_elements_by_class_name('_15kq._77li')

# comment[100].click()
print(type(comment))
sleep(5)



