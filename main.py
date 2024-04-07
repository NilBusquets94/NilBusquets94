# Importing the standard libraries
import time
import pandas as pd
import numpy as np
from datetime import datetime
import re
import locale

# Importing Selenium library and relevant classes
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains


# Installing the Selenium Chrome web driver
# No external files need to be downloaded with this method of utilizing Selenium
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Fetching the Wallapop home page
driver.get('https://www.coches.net/segunda-mano/');
time.sleep(1)

# Maximizing the window
driver.maximize_window()  
driver.switch_to.window(driver.current_window_handle)
driver.implicitly_wait(1)

# Accepting page cookies whenever it shows/loads up on the screen
try:
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".banner-actions-container"))).click()
except:
    pass
