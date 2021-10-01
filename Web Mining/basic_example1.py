import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=mobile+phone"
page = requests.get(url)
soup = BeautifulSoup(page.text,'lxml')

links = soup.find_all('a')
for link in links:
    print(link.text, link.attrs.get('href'))
