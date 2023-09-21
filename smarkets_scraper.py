import requests

from selenium import webdriver
from selenium.webdriver.common.by import By


class SmarketsScraper:
    def __init__(self):

        self.BaseURL = "https://smarkets.com/"
        self.PLURL = "https://smarkets.com/listing/sport/football/england-premier-league"


    def getMatchData(self):
        driver = webdriver.Firefox(executable_path="C:\Program Files\gekkodriver\geckodriver.exe")

        driver.get(self.PLURL)
        driver.implicitly_wait(3)

        event_list = driver.find_element(by=By.CLASS_NAME,value="event-list")
        events = event_list.find_elements(by=By.CLASS_NAME,value="event-tile")
        for event in events:
            print()

