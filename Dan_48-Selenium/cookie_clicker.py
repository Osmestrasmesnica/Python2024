from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# # Add implicit wait to allow elements to load
# driver.implicitly_wait(10)  # Adjust the timeout as needed

cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")
cps = driver.find_element(By.ID, "cps")

cursor = driver.find_element(By.ID, "buyCursor")
grandma = driver.find_element(By.ID, "buyGrandma")
factory = driver.find_element(By.ID, "buyFactory")
mine = driver.find_element(By.ID, "buyMine")
shipment = driver.find_element(By.ID, "buyShipment")
alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
portal = driver.find_element(By.ID, "buyPortal")
time_machine = driver.find_element(By.ID, "buyTime machine")
# elder_pledge = driver.find_element(By.ID, "buyElder Pledge")

list_of_upgrades = driver.find_elements(By.CSS_SELECTOR, "div#store b")
price_list = []

for item in list_of_upgrades:
    try:
        price = item.text.split(" - ")[1].replace(",", "")
        price_list.append(int(price))
    except IndexError:
        print(f"{item.text} does not exist")

time_out = time.time() + 60  # 1 minute from now
check_upgrades = time.time() + 5  # Check every 5 seconds

while True:
    cookie.click()

    if time.time() > time_out:
        print(f"This is my cookies per second amount: {cps.text}")
        break

    if time.time() > check_upgrades:
        money_value = int(money.text.replace(",", ""))
        print(f"Current money: {money_value}")
        for i in range(len(price_list) - 1, -1, -1):
            print(f"Price: {price_list[i]}, Money: {money_value}")
            if price_list[i] < money_value:
                list_of_upgrades[i].click()
                time.sleep(1)
        check_upgrades = time.time() + 5  # Update the check time

# driver.quit()


#! SREDITI OVO DA SE NASTAVI POSLE KUPOVINE