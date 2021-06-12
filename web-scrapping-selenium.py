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
#opts.BinaryLocation = "/usr/bin/chromium-browser"

#Below line to add extension privacy pass which has been packed as crx file
opts.add_extension('./2.0.7_0.crx')

#Remove this comment if you dont want see the UI pop up also removing helps in masking from anti bot programs
#opts.headless =True
chromedriverPath = './chromedriver'
driver = webdriver.Chrome(executable_path=chromedriverPath,options=opts)

if(driver == None):
    print('driver not initialised.....')
else:
    print('driver initialised.....')

URL1 = 'https://dramacool.vc/365-repeat-the-year-episode-3.html'
URL = 'https://dramacool.vc/drama-detail/365-one-year-against-destiny'
driver.get(URL1)

button = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[4]/ul/li[4]/a')[0]
button.click()

#list_of_download_elements = driver.find_element_by_name("download")
#print(list_of_download_elements)
