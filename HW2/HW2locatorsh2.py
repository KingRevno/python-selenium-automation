from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

driver.find_element(By.XPATH, "//input[@id='ap_email']")

driver.find_element(By.ID, 'continue')

driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(),'Conditions of Use')]")

driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(),'Privacy Notice')]")

# Need Help
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()

driver.find_element(By.ID, 'auth-fpp-link-bottom')

driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

driver.quit()


