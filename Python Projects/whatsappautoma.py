from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome()
import time

driver.get("https://web.whatsapp.com/")

input("Scan QR Code and press any key to continue")


RM = driver.find_element_by_css_selector('span[title="Links"]')
RM.click()

testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

#time.sleep(5)
for i in range(5):
    testinput.send_keys("Hello......")
    testinput.send_keys(Keys.RETURN)
