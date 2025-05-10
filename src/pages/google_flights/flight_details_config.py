import re
from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .main_locators import MainLocators


class FlightDetails:

    def __init__(self, driver: Optional[WebDriver]):
        self.driver = driver
        self.min_action_delay = 0.5
        self.max_action_delay = 0.9
        self.iterator = 0
        self.wait = WebDriverWait(driver, 10)

    def input_flight_source(self, source: str):
        flight_source_field = self.wait.until(EC.visibility_of_element_located(MainLocators.SOURCE_INPUT))
        flight_source_field.click()
        flight_source_field.clear()
        for char in source:
            ActionChains(self.driver).send_keys_to_element(flight_source_field, char).perform()

    def input_flight_destination(self, dest: str):
        flight_destination_field = self.wait.until(EC.visibility_of_element_located(MainLocators.DESTINATION_INPUT))
        flight_destination_field.click()
        flight_destination_field.clear()
        for char in dest:
            ActionChains(self.driver).send_keys_to_element(flight_destination_field, char).perform()

    def scrape_airports(self):
        airport_array = {}

        major_destinations = [dest.accessible_name for dest in self.wait.until(EC.visibility_of_all_elements_located(MainLocators.MAJOR_DESTINATIONS))]
        for destination in major_destinations:
            airport_array[destination] = []

        airport_subsection_buttons = self.wait.until(EC.visibility_of_all_elements_located(MainLocators.DROPDOWN_SUBSECTION_BUTTONS))
        ActionChains(self.driver).move_to_element(self.wait.until(EC.visibility_of_all_elements_located(MainLocators.DROPDOWN_SUBSECTION_BUTTONS))[-1]).perform()
        for i, _ in enumerate(airport_subsection_buttons):
            if i == 0:
                continue
            buttons = self.wait.until(EC.visibility_of_all_elements_located(MainLocators.DROPDOWN_SUBSECTION_BUTTONS))
            buttons[i].click()

        ActionChains(self.driver).move_to_element(self.wait.until(EC.visibility_of_all_elements_located(MainLocators.AIRPORTS))[-1]).perform()
        airports = [airport.accessible_name for airport in self.wait.until(EC.visibility_of_all_elements_located(MainLocators.AIRPORTS))]
        airports_counts = dict((self.process_airport_count(ap) for ap in self.driver.find_elements(*MainLocators.AIRPORT_COUNT_PER_DEST)))

        for key, value in airports_counts.items():
            airport_array[key] = ["" for i in range(value)]

        for destination, array in airport_array.items():
            if not destination in airports_counts:
                continue
            replacer = self.replace_range(airports)
            airport_array[destination] = replacer(array)
        
        return airport_array

    def find_number(self, text: str):
        """
        Find the first number in a string.
        
        Args:
            text (str): The string to search.
        Returns:
            int: The first number found in the string, or None if no number is found.
        """
        result = re.search(r"Showing (\d+) nearby", text)
        return int(result.group(1)) if result else None
    
    def process_airport_count(self, element: WebElement):
        parent = element.find_element(By.XPATH, "..").accessible_name
        airport_count = self.find_number(element.get_attribute("textContent"))
        return (parent, airport_count)

    def replace_range(self, source: list):

        def _replacer(target: list):
            result = source[self.iterator:self.iterator + len(target)]
            self.iterator += len(target)
            return result

        return _replacer

