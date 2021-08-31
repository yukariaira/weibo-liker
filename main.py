#for weibo account liking friend circle

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
import os


#creates a browser that can have memory / store previous information
#treats the item as one whole newly installed / incongito, need to log in once to retain info

chrome_options = Options()
dir_path = os.getcwd()
chrome_options.add_argument(f'user-data-dir={dir_path}/storedatahere')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
#alt - chrome_options.add_argument("user-data-dir=C:\environments\selenium") #creates a new cookie/cache in the session
#old - chrome_options.add_argument("--user-data-dir=chrome-data") #creates a new cookie/cache in the session)
driver = webdriver.Chrome("A:\\Coding stuffs\\documents\\chromedriver.exe",options=chrome_options)#makes the driver use the data in the options



#-------------start trying here-------------------------
try:

    driver.get('https://weibo.com/') #gets friend circle page

    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "woo-like-count")) #wait until posts loaded(inside plc_main element)
    )

    targets = driver.find_elements_by_xpath('//span[(@class="woo-like-count")]')
    #old - targets = driver.find_elements_by_xpath('//a[contains(@action-type,"fl_like") and contains(@class,"S_txt2")]')


    for target in targets:
        target.click()
        time.sleep(randint(30,60)) #pauses for random 30-60secs

    print('likepost - done')
    driver.quit()

except:
    print('likepost - nope')
    


