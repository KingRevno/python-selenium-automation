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

# Open Amazon
driver.get('https://www.amazon.com/')
# Click Orders
driver.find_element(By.XPATH, "//span[normalize-space()='& Orders']").click()
# Verify Sign in Page by check Sign In Header and Email Input Field is visible

# header
driver.find_element(By.XPATH, "//h1[normalize-space()='Sign in']")
# Email Input Field
driver.find_element(By.XPATH, "//input[@id='ap_email']")


print('Test case passed!')

driver.quit()
