# BeautifulSoup and Request

from bs4 import BeautifulSoup
import requests
url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

# BeautifulSoup(page.text, 'html')
soup = BeautifulSoup(page.text, features= "html.parser")
# print(soup.title.text)  // menampikan judul web
print(soup.prettify()) 
# print (soup)


