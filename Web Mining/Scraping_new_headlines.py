import sys
from selenium import webdriver
from webdriver_manager import driver
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

webpage = "https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation"
driver.get(webpage)

target = driver.find_element_by_css_selector('div.lisingNews')  # single
news = target.find_element_by_css_selector('div.newsItm')   # multi

# loop through all the news
data = []
for item in news:
    try:
        title = item.find_element_by_css_selector('h2.newsHdng').text
    except:
        title = ""
    try:
        posted_by = item.find_element_by_css_selector('span.posted-by').text
    except:
        posted_by = ""
    try:
        content = item.find_element_by_css_selector('p.newsCont').text
    except:
        content = ""

    data.append({
        'title':title,
        'posted_by':posted_by,
        'content':content
    })

if len(data) > 0:
    pd.DataFrame(data).to_csv('todays_headlines.csv')
else:
    print("No news headlines found!!")
driver.close()

#     print(title)
#     print(posted_by)
#     print()

# print(len(news),'news found')
# driver.close()