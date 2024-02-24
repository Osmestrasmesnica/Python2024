from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
driver.get("https://osmestrasmesnica.github.io/wlqmapapp/")
time.sleep(2)

# Click on the import link
import_hover = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul/li[2]/a").click()
time.sleep(2)

# Click on the import excel link
import_excel_link = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul/li[2]/ul/li[2]/a")
import_excel_link.click()

time.sleep(2)

# Wait for the file dialog window to appear
time.sleep(2)

# Click TAB six times to navigate to the file name input field
for _ in range(6):
    pyautogui.press('tab')

# Type the file name "PhD_BAZA (10).xlsx"
pyautogui.write("PhD_BAZA (10).xlsx")

# Click TAB four times to navigate to the file name input field again
for _ in range(4):
    pyautogui.press('tab')

time.sleep(2)

# Type the file name "PhD_BAZA (10).xlsx" again
pyautogui.write("PhD_BAZA (10).xlsx")

# Press ENTER to confirm the file selection
pyautogui.press('enter')

time.sleep(2)

# Select the option with value "UTM_10x10"
select_element = driver.find_element(By.CSS_SELECTOR, "option[value='UTM_10x10']")
select_element.click()

# Find and click on elements
add_taxa_btn = driver.find_element(By.CSS_SELECTOR, ".togetherTaxa")
export_btn = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul/li[3]/a")
export_png_btn = driver.find_element(By.XPATH, "//*[@id='png']")

time.sleep(2)

# Loop through orchids and perform actions
select_orchid = driver.find_elements(By.CSS_SELECTOR, "div.dataToShow select option")
for orchid in select_orchid:
    orchid.click()
    time.sleep(1)
    add_taxa_btn.click()
    time.sleep(1)
    export_btn.click()
    time.sleep(1)
    export_png_btn.click()
    time.sleep(1)
