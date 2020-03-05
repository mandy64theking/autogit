from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import sys
url = "https://github.com/login"
username = "ENTER USERNAME"
password = "ENTER PASSWORD"
options = webdriver.ChromeOptions() #Use FirefoxOptions() if you use firefox driver
options.add_argument('--headless')
driver = webdriver.Chrome(options=options) #replace with Chrom with Firefox

driver.implicitly_wait(30)
driver.get(url)
driver.find_element_by_name("login").send_keys(username)

driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("commit").click()
driver.get("https://github.com/new")
driver.find_element_by_id("repository_name").send_keys(sys.argv[1])
#bleh

if sys.argv[2] == "private":
    driver.find_element_by_id(
        "repository_visibility_private").click()
else:
    driver.find_element_by_id(
        "repository_visibility_public").click()

driver.find_element_by_xpath(
    "/html/body/div[4]/main/div/form/div[3]/button").submit()
link=driver.find_element_by_id("empty-setup-clone-url").get_attribute("value")
print("A Github git repository has been created on "+str(link))
driver.get("https://github.com/logout")
driver.find_element_by_xpath("/html/body/div[4]/main/div/form/input[3]").submit()
driver.close()