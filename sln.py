from selenium import webdriver
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.facebook.com/profile.php?id=100014957612928")

# btn = driver.find_element_by_xpath('//*[@id="mount_0_0_ia"]/div/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/a/div/div[1]/div/span/span')
# btn.click()
# username = driver.find_element_by_xpath('//*[@id="email"]')

# password = driver.find_element_by_xpath('//*[@id="pass"]')

# button = driver.find_element_by_xpath('//*[@id="mount_0_0_fs"]/div/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/a/div/div[1]/div/span/span')
# button.click()

submit   = driver.find_element_by_name("login")
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")



username.send_keys('9140083568')
password.send_keys('shivvamm04')

submit.click()

# search = driver.find_element_by_xpath('//*[@id="mount_0_0_Sl"]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/label/input')
# search.send_keys('pravin singh')

# comment = driver.find_element_by_xpath('//*[@id="mount_0_0_ou"]/div/div[1]/div/div[3]/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[11]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div[2]/form/div/div/div[1]/p')
# comment.send_keys('hii')
# driver.get("https://youtube.com")

# time.sleep(30)
# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys('selenium')
# button = driver.find_element_by_id('')

# searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
# searchbutton.click()