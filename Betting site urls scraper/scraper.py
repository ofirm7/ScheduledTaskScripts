from concurrent.futures import ThreadPoolExecutor

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures
import csv
import hashlib
import uuid
import os
import json
from twocaptcha import TwoCaptcha
import logging
import requests
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import os
from PIL import ImageGrab, Image
from tkinter import Tk


# ? loading website
BASE_URL = "https://sports.bet9ja.com/competition/soccer/international/uefanationsleaguewomen/1-11463-3952843?s=new&_gl=1*asaox2*_gcl_au*MjA1ODkwMDc3MC4xNjk2MDEzMDA2"

options = Options()
# options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
options.add_argument('start-maximized')
driver = webdriver.Chrome(service=Service(
    executable_path='./chromedriver-win64/chromedriver-win64/chromedriver.exe'), options=options)
action=ActionChains(driver)
driver.get(BASE_URL)
time.sleep(5)

# clicking soccer 
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//div[text()='Soccer']")))
soccer=driver.find_elements(By.XPATH,"//div[text()='Soccer']")[0]
action.move_to_element(soccer).click().perform()
time.sleep(3)


# clicking showmore
showMore=driver.find_element(By.ID,"left_prematch_sport-1_soccer_buttonmore-toggle")
showMore = driver.find_element(By.ID, "left_prematch_sport-1_soccer_labelmore-toggle")
parent_element = showMore.find_element(By.XPATH, '..')
parent_element.click()

# # clicking on accordian items
container=WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME,"accordion-item.accordion-item--open")))
accordian_items=container.find_elements(By.CLASS_NAME,"accordion-item")
print(accordian_items[-1].get_attribute("innerText"))
with open("urls.txt",'a+') as f:
    for item in accordian_items:
        try:
           item.click()
        except:
           action.move_to_element(item).click().perform()
            
        links=item.find_elements(By.CLASS_NAME,'menu-list__item')
        
        for link in links:
            try:
                link.click()
                print(driver.current_url)
                f.write(driver.current_url)
            except:
                try:
                   action.move_to_element(link).click().perform()
                   print(driver.current_url)
                   f.write(driver.current_url)
                except:
                   continue
                
                
