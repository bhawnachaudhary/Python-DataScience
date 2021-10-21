from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())


webpage1 = "https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation"
driver.get(webpage)