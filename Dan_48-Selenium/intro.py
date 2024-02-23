from selenium import webdriver
from selenium.webdriver.common.by import By

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={USER_AGENT}")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options) # initial of object driver Chrome, sluzi za komunikaciju seleniuma i najnovije verzije webbrowsera

# Za otvaranje stranice
driver.get("https://www.amazon.de/dp/B0CNH77WY4?tag=camelwebde-21&linkCode=ogi&th=1&psc=1&language=de_DE")

price_euro = driver.find_element(By.CLASS_NAME, 'a-price-whole') #! koristiti XPath ako ne mozes da nadjes element
price_cents = driver.find_element(By.CLASS_NAME, 'a-price-fraction')
print(f"Cena izabranog artikla je: {price_euro.text}.{price_cents.text}")


# # Za zatvaranje stranice odnosno taba (jednog taba/trenutnog taba)
# driver.close()

# Za zatvaranje celog prozora sa svim tabovima
driver.quit()