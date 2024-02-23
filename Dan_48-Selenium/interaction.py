from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrom_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# a[title = "Special:Statistics"]

number_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(number_of_articles.text)

# kliktanje linka
number_of_articles.click()

# kucanje teksta
search = driver.find_element(By.NAME, "search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()