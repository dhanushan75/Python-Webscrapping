import os
import selenium
from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
import time

#Install Driver
opts = Options()
opts.BinaryLocation = "/usr/bin/chromium-browser"
opts.headless =True
driver = webdriver.Chrome(executable_path='/usr/bin/chromium-browser',options=opts)

URL1 = 'https://dramacool.vc/365-repeat-the-year-episode-3.html'
driver.get(URL1)
