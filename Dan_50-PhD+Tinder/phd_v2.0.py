from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
driver.get("https://osmestrasmesnica.github.io/wlqmapapp/")

# Click on the import link
import_hover = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul/li[2]/a").click()

# Click on the import excel link
import_excel_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/nav/div/div/ul/li[2]/ul/li[2]/a"))
)
import_excel_link.click()

# Wait for the file dialog window to appear
time.sleep(2)

# Click TAB six times to navigate to the file name input field
for _ in range(6):
    pyautogui.press('tab')

# Type the file name "PhD_BAZA (10).xlsx"
time.sleep(2)
pyautogui.write("PhD_BAZA (10).xlsx")

# Click TAB four times to navigate to the file name input field again
for _ in range(4):
    pyautogui.press('tab')

# Type the file name "PhD_BAZA (10).xlsx" again
pyautogui.write("PhD_BAZA (10).xlsx")
time.sleep(2)

# Press ENTER to confirm the file selection
pyautogui.press('enter')

# Select the option with value "UTM_10x10"
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='UTM_10x10']"))
)
select_element.click()

add_taxa_btn = driver.find_element(By.CSS_SELECTOR, ".togetherTaxa")
export_btn = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul/li[3]/a")
export_png_btn = driver.find_element(By.XPATH, "//*[@id='png']")

time.sleep(2)


# Loop through orchids and perform actions
select_orchid = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.dataToShow select option"))
)
for orchid in select_orchid:
    orchid.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".togetherTaxa"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/nav/div/div/ul/li[3]/a"))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='png']"))
    ).click()
