import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
import matchdata as md


class SmarketsScraper:
    def __init__(self):
        self.BaseURL = "https://smarkets.com/"
        self.PLURL = "https://smarkets.com/listing/sport/football/england-premier-league"

    def get_match_data(self):
        match_data_list = list()
        driver = webdriver.Firefox(executable_path="C:\Program Files\gekkodriver\geckodriver.exe")

        driver.get(self.PLURL)
        driver.implicitly_wait(3)

        events = driver.find_elements(by=By.CLASS_NAME, value="event-tile")


        list_count = 0
        list_length = len(events)

        while list_count < list_length:

            driver.execute_script("window.scrollTo(0, " + str(list_count*150) + ")")
            events[list_count].click()
            driver.implicitly_wait(.1)

            time = driver.find_element(by=By.CLASS_NAME, value="event-date").text
            driver.back()
            driver.implicitly_wait(.1)

            events = driver.find_elements(by=By.CLASS_NAME, value="event-tile")
            match_data_list.append(md.MatchData(events[list_count].text,time))
            list_count += 1

        return match_data_list

