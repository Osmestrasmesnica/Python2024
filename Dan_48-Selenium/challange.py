from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

dummy_site = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(dummy_site)

SECRET_EMAIL = "secret-email@example.com"
SECRET_FIRST_NAME = "Example"
SECRET_LAST_NAME = "Elpmaex"

# insert first name
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys(SECRET_FIRST_NAME)

# insert last name
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys(SECRET_LAST_NAME)

# insert email address
email = driver.find_element(By.NAME, "email")
email.send_keys(SECRET_EMAIL)

# click Signup button
signup_btn = driver.find_element(By.CSS_SELECTOR, "button.btn")
signup_btn.click()

driver.quit()
