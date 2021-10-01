from selenium import webdriver
from webdriver_manager import driver
import webdriver_manager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
