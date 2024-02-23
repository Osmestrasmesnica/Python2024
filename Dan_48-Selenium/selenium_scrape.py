from selenium import webdriver
from selenium.webdriver.common.by import By

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrom_options)

driver.get("https://www.python.org/")

events_date = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for time in events_date:
    print(time.text)

for name in events_name:
    print(name.text)


    
# create dict
events = {}

for n in range(len(events_date)):
    events[n] = {
        "date": events_date[n].text,
        "name": events_name[n].text
    }

# events = [{"date": date.text, "name": name.text} for date, name in zip(events_date, events_name)]


print(events)


driver.quit()