import os
import selenium
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
import time

#For Chrome browser
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())

opts = Options()
opts.BinaryLocation = "/usr/bin/chromium-browser"
#Remove this comment if you dont want see the UI pop up
#opts.headless =True
chromedriverPath = '/home/admin1/Documents/webscraping/Python-Webscrapping/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriverPath,options=opts)

if(driver == None):
    print('driver not initialised.....')
else:
    print('driver initialised.....')

URL1 = 'https://dramacool.vc/365-repeat-the-year-episode-3.html'
URL = 'https://dramacool.vc/drama-detail/365-one-year-against-destiny'
testurl = 'https://www.google.com/'
driver.get(URL1)

print(driver)
