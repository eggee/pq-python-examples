#simple webgui selenium automation example

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('http://10.213.253.35')
driver.find_element_by_id("l_usrnm").clear()
driver.find_element_by_id("l_usrnm").send_keys("ADTRAN")
driver.find_element_by_id("l_pswrd").clear()
driver.find_element_by_id("l_pswrd").send_keys("BOSCO")
driver.find_element_by_id("loginbutton").click()
time.sleep(10)
driver.find_element_by_id("overlay_ok").click()
time.sleep(10)

output = driver.find_element_by_id("ProductTitle")
print output.text

driver.close()
