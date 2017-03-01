from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

#note: sleeps were used here for simplicity of understanding and showcase
#ideally would not use those - need to poll for your values

url = "https://10.255.64.112"

driver = webdriver.Chrome()
# driver = webdriver.Chrome()


#go to url
driver.get(url)
#username
# driver.find_element_by_xpath("//div[@class='login-form-group']//input[@name='username']").send_keys("TEST")
# time.sleep(2)
driver.find_element_by_id("input_0").clear()
driver.find_element_by_id("input_0").send_keys("ADMIN")
#password
driver.find_element_by_id("input_1").clear()
driver.find_element_by_id("input_1").send_keys("PASSWORD")
driver.find_element_by_xpath("//button[@type='submit']").click()

#waiting for settings element to both exist and be visible
# time.sleep(5)
try:
    element_present = EC.presence_of_element_located((By.XPATH, "//md-menu[@class='md-primary md-menu ng-scope']"))
    WebDriverWait(driver, 30).until(element_present)
except TimeoutException:
    raise AssertionError("Timeout waiting for MOSAIC page to load")

#click on settings
driver.find_element_by_xpath("//md-menu/button[@aria-label='User Settings']").click()
time.sleep(1)
driver.find_element_by_xpath("//md-menu-item/button[@aria-label='About']").click()
client_version = driver.find_element_by_xpath("//md-list-item/div[contains(text(), 'Client Version')]/parent::md-list-item/div[@class='md-secondary']").text

print "here is your client version: {0}".format(client_version)

driver.close()
