from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

import time

# div sa slikom
# div role="img" class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox

# ili

# dugme za selektovanje
# <button type="button" class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgi($g-ds-background-nope):a" draggable="false"><span class="Pos(r) Z(1) Expand"><span class="D(b) Expand" style="transform: scale(1); filter: none;"><svg focusable="false" aria-hidden="true" role="presentation" viewBox="0 0 24 24" width="24px" height="24px" class="Scale(.5) Expand"><path d="m15.44 12 4.768 4.708c1.056.977 1.056 2.441 0 3.499-.813 1.057-2.438 1.057-3.413 0L12 15.52l-4.713 4.605c-.975 1.058-2.438 1.058-3.495 0-1.056-.813-1.056-2.44 0-3.417L8.47 12 3.874 7.271c-1.138-.976-1.138-2.44 0-3.417a1.973 1.973 0 0 1 3.25 0L12 8.421l4.713-4.567c.975-1.139 2.438-1.139 3.413 0 1.057.814 1.057 2.44 0 3.417L15.44 12Z" fill="var(--fill--background-nope, none)"></path></svg><span class="Hidden">Ne</span></span></span></button>



# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
driver.get("https://tinder.com/")

base_window = driver.window_handles[0]
print(driver.title)

login_btn = driver.find_element(By.XPATH, """//*[@id="c-1398387530"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]""").click()
time.sleep(3)
google_btn = driver.find_element(By.XPATH, "//*[@id='c-393658329']")
google_btn.click()

time.sleep(3)
new_window = driver.window_handles[1]
new_window2 = driver.window_handles[1]
new_window3 = driver.window_handles[1]
new_window4 = driver.window_handles[1]
new_window5 = driver.window_handles[1]

driver.switch_to.window(new_window)
print(driver.title)

# time.sleep(3)
email_input = driver.find_element(By.CSS_SELECTOR, "input[type = 'email']")
email_input.send_keys("wlq.advisors@gmail.com")
email_input.send_keys(Keys.ENTER)


#! SVE OVO JE ZA SADA DOBRO ALI GOOGLE MALKO SMARA PA MORAS DA NADJES WORK AROUND  
#! IMAS NA OVOM STACKOWERFLOW...
#! https://stackoverflow.com/questions/59515561/this-browser-or-app-may-not-be-secure-error-while-attempting-to-login-in-to-gm
#info ovo ispod je iz koda sa kursa jer nisam dosao do toga

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(3)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    time.sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()