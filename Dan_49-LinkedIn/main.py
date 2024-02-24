from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

#TODO 1 - Setup resume for LinkedIn

# Python Remote Easy Apply European Union
pre_defined_job = "https://www.linkedin.com/jobs/search/?currentJobId=3829860321&f_AL=true&f_WT=2&geoId=91000000&keywords=python%20developer%20&location=European%20Union&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"

# Python Remote Easy Apply Serbia
pre_defined_job2 = "https://www.linkedin.com/jobs/search/?currentJobId=3820001764&f_AL=true&f_WT=2&geoId=101855366&keywords=python%20developer%20&location=Serbia&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(pre_defined_job2)

#! Ako se pojavljuje Cookies ili Login page
# # Click Reject Cookies Button
# try:
#     time.sleep(2)
#     reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
#     reject_button.click()
# except Exception as e:
#     print(e)

# Click Sign in Button
time.sleep(4)
try:
    sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
    sign_in_button.click()
except Exception as e:
    print(e)

# Sign in
time.sleep(5)
try:
    email_field = driver.find_element(by=By.ID, value="username")
    email_field.send_keys(EMAIL)
    password_field = driver.find_element(by=By.ID, value="password")
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.ENTER)
    time.sleep(5)
except Exception as e:
    print(e)

time.sleep(5)
list_of_jobs = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container")
for job in list_of_jobs:
    job.click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button").click()
    print("Dodato u SAVE posao za: " + job.text)
    time.sleep(2)