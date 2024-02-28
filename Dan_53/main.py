from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

# Define headers for HTTP requests
headers = {
    "User-Agent": "Defined"
}

# URL of the Zillow Clone page
zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"

# Fetch the HTML content of the page
response = requests.get(zillow_clone_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extract property links
links = soup.find_all("a", class_="property-card-link")
link_list = [link.get("href") for link in links]

# Extract property prices
prices = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
prices_list = [price.getText().split("/")[0] if "/" in price.getText() else price.getText().split("+")[0] for price in prices]

# Extract property addresses
addresses = soup.find_all("address", {"data-test": "property-card-addr"})
address_list = [address.getText(strip=True) for address in addresses]

# Selenium WebDriver setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# URL of the Google Form
google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSc291fiWejdptcd2fM9uiB31f9lO6I2CldH6R7O4E2mJLWZLA/viewform?usp=sf_link"
driver.get(google_form_url)

# Find form elements
form_address = driver.find_element(By.CSS_SELECTOR, "div.Xb9hP input[type=text]")
form_price = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
form_link = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")

# Iterate over each property and submit the form
for i in range(len(address_list)):
    # Populate form fields
    form_address.send_keys(address_list[i])
    form_price.send_keys(prices_list[i])
    form_link.send_keys(link_list[i])
    
    # Submit the form
    form_btn = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
    form_btn.click()
    
    # Wait for the submission to complete
    driver.implicitly_wait(2)
    
    # Navigate to the new form page
    new_form_btn = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    new_form_btn.click()

# # Close the browser
driver.quit()
