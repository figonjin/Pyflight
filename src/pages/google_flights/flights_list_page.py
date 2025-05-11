"""
Google Flights List Page Object
"""
import re
import time
import math
from typing import Optional

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .main_locators import MainLocators

class FlightsList:

    def __init__(self, driver: Optional[WebDriver]):
        self.driver = driver
        self.min_action_delay = 0.5
        self.max_action_delay = 0.9
        self.iterator = 0
        self.wait = WebDriverWait(driver, 5)
    
    def safe_find_all(self, locator, visible = False):
        """Always fetch fresh elements, waiting for presence or visibility."""
        retries = 0
        element = None
        while retries < 3:
            try:
                if visible:
                    element = self.wait.until(EC.visibility_of_all_elements_located(locator))
                    break
                # element = self.wait.until(EC.presence_of_all_elements_located(locator))
                element = self.driver.find_elements(locator[0], locator[1])
                break
            except StaleElementReferenceException:
                retries += 1
        if element is None:
            raise StaleElementReferenceException
        else:
            return element

    def expand_all(self):
        """
        Expands all flight options on the Google Flights page.
        """
        button = self.safe_find_all(MainLocators.OTHER_MORE_FLIGHTS_BUTTON, True)
        ActionChains(self.driver).move_to_element(button[0]).click(button[0]).perform()
        self.wait.until(EC.presence_of_element_located(MainLocators.OTHER_FLIGHTS))


    
    def scrape_flights(self):
        """
        Scrapes flight information from the Google Flights page.
        """
        self.expand_all()
        flights_array = {0: {}, 1: {}}

        for i, entry in enumerate(flights_array.values()):
            data = {
                'flights': MainLocators.TOP_FLIGHTS if i == 0 else MainLocators.OTHER_FLIGHTS,
                'duration': MainLocators.TOP_FLIGHT_DURATIONS if i == 0 else MainLocators.OTHER_FLIGHT_DURATIONS,
                'price': MainLocators.TOP_FLIGHT_PRICES if i == 0 else MainLocators.OTHER_FLIGHT_PRICES,
                'times': MainLocators.TOP_FLIGHT_TIMES if i == 0 else MainLocators.OTHER_FLIGHT_TIMES,
            }
            time.sleep(5)
            flights = self.safe_find_all(data['flights'])[0]
            flights = flights.find_elements(By.CSS_SELECTOR, "li")
            prices_list = self.safe_find_all(data['price'])
            for j, _ in enumerate(flights):
                entry[j] = {'times': [], 'price': "", 'duration': ""}
            for j, array in enumerate(entry.values()):
                index = None
                if i == 1:
                    index = lambda x: x if x <= max(0, min(x, math.floor(len(prices_list)/2) - 1)) else None
                else:
                    index = lambda x: x
                validate = index(j*3)
                if validate is not None:
                    array['price'] = self.safe_find_all(data['price'])[index(j*3)].get_attribute("textContent")
                else:
                    array['price'] = "Price Unavailable"
            for j, array in enumerate(entry.values()):
                array['duration'] = self.safe_find_all(data['duration'])[j*4].get_attribute("textContent")               
                array['times'].append(re.sub(r'\s+', ' ', self.safe_find_all(data['times'])[index(j*2)].get_attribute("textContent")).strip())
                array['times'].append(re.sub(r'\s+', ' ', self.safe_find_all(data['times'])[index((j*2)+1)].get_attribute("textContent")).strip())

        flights_array[1].popitem()
        return flights_array