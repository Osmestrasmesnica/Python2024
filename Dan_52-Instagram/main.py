from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

load_dotenv()

instagram_path = "https://www.instagram.com/"
follow_profile = "tuitamo.ma"

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
driver.get(instagram_path)

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# Wait for the username input field and enter username
username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")))
username_input.send_keys(INSTAGRAM_USERNAME)

# Wait for the password input field and enter password
pass_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")))
pass_input.send_keys(INSTAGRAM_PASSWORD)
pass_input.send_keys(Keys.ENTER)

# Wait for the "Save Login Info" button and click
logininfo_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div._ac8f')))
logininfo_btn.click()

# Wait for the "Turn on Notifications" button and click
notific_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button._a9_1")))
notific_btn.click()

time.sleep(3)
driver.get(f"https://www.instagram.com/{follow_profile}/")

time.sleep(3)
follow_btn = driver.find_element(By.CLASS_NAME, "_acan")
follow_btn.click()