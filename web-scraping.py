import requests
from bs4 import BeautifulSoup
import cloudscraper

URL = 'https://dramacool.vc/drama-detail/365-one-year-against-destiny'
URL1 = 'https://dramacool.vc/365-repeat-the-year-episode-3.html'
page = requests.get(URL1)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('li', class_="download")
print(results)

url2 = results[0].find('a')['href']
print(url2)

scraper = cloudscraper.create_scraper()
print(scraper.get(url2).text)

#page2 = requests.get(url2)
#soup2 = BeautifulSoup(page2.content, 'html.parser')
#print('soup2 : ', soup2)
#results2 = soup2.find_all('div', class_="download")

#print(results2)


#url2 = results.get_text()
#print('lines in results : ', url2)
#if('href' in str(url2)):
    #print(url2)
