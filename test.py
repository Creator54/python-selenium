import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
urls = [
        'https://drive.google.com/drive/folders/1zttrYkknLimLgipb6EgC-TkkP74nJyky?usp=share_link',
        ]
clicked = False

def down(url='https://drive.google.com/drive/folders/1hm5dPwJI3y2AAK6YNmJ__zGVW-3Kivj2'):
    #global clicked
    driver.get(url)
    time.sleep(2)
    #if not clicked:
    #    driver.find_element(By.XPATH,"//div[@class='c-Po a-d-c']").click()
    #    clicked = True

    #allData = driver.find_elements(By.XPATH,"//div[@class='akerZd']")
    #folders = driver.find_elements(By.XPATH,"//span[text()='—']")
    ##allData - folders = files

    #for i in range(len(allData)-len(folders)-1,len(allData)):
    #    if(len(driver.window_handles) != 1):
    #        driver.switch_to.window(driver.window_handles[0])
    #    allData[i].click() #download all files

    ##now recurse to folders
    ##driver.switch_to.window(driver.window_handles[0])
    ##for x in folders:
    ##    x.click()
    ##    down(driver.current_url)

    stuff = driver.find_elements(By.XPATH, "//div[@aria-label='Download']")
    for x in stuff:
        x.click()
    input("Press enter")
for x in urls:
    down(x)
