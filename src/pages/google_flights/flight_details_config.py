import re
import time
from typing import Optional
import unicodedata

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
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
        self.wait = WebDriverWait(driver, 1)
        self.actions = ActionChains(self.driver)

    def safe_find_all(self, locator, visible = False):
        """Always fetch fresh elements, waiting for presence or visibility."""
        if visible:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def safe_input(self, field: WebElement, text: str):
        if len(text) > 5:
            text_initial = text[0:4] + text[-1]
            text_inner = reversed(text[4:-1])
            for char in text_initial:
                self.actions.send_keys_to_element(field, char).perform()
                time.sleep(0.000001)
            for char in text_inner:
                self.actions.send_keys_to_element(field, char).perform()
        else:
            for char in text:
                self.actions.send_keys_to_element(field, char).perform()

    def input_flight_source(self, source: str):
        flight_source_field = self.safe_find_all(MainLocators.SOURCE_INPUT, True)[0]
        self.actions.click(flight_source_field).pause(0.0005).send_keys(Keys.DELETE).perform()
        flight_source_field.clear()

        self.safe_input(flight_source_field, source)
        time.sleep(0.1)
        

    def input_flight_destination(self, dest: str):
        flight_destination_field = self.safe_find_all(MainLocators.DESTINATION_INPUT, True)[0]
        self.actions.click(flight_destination_field).pause(0.0005).send_keys(Keys.DELETE).perform()
        flight_destination_field.clear()

        self.safe_input(flight_destination_field, dest)
        time.sleep(0.1)

    def select_airport(self, airport: str):
        all_airports = self.scrape_airports()
        for destinations, airports in all_airports.items():
            if any(airport in item for item in airports):
                elements = self.safe_find_all(MainLocators.AIRPORTS, True)
                for element in elements:
                    selection = element.find_element(By.CSS_SELECTOR, "div[class][jsname]")
                    if airport in selection.text:
                        self.actions.move_to_element(selection).pause(1).click(selection).perform()
                        return
            elif normalize(airport) in normalize(destinations):
                elements = self.safe_find_all(MainLocators.MAJOR_DESTINATIONS, True)
                self.actions.click(elements[0]).perform()


    def scrape_ticket_prices(self):
        ticket_prices = {}

    def scrape_airports(self):
        airport_array = {}
        major_destinations = [e.accessible_name for e in self.safe_find_all(MainLocators.MAJOR_DESTINATIONS, True)]
        for destination in major_destinations:
            airport_array[destination] = []

        try:
            airport_subsection_buttons = self.safe_find_all(MainLocators.DROPDOWN_SUBSECTION_BUTTONS)
        except TimeoutException:
            return airport_array
        for i, _ in enumerate(airport_subsection_buttons):
            buttons = self.safe_find_all(MainLocators.DROPDOWN_SUBSECTION_BUTTONS, True)
            expanded = buttons[i].get_attribute('aria-expanded')
            if not expanded == "true":
                self.actions.move_to_element(self.safe_find_all(MainLocators.DROPDOWN_SUBSECTION_BUTTONS, True)[i]).perform()
                self.actions.click(self.driver.find_elements(*MainLocators.DROPDOWN_SUBSECTION_BUTTONS)[i]).perform()

        self.actions.move_to_element(self.wait.until(EC.visibility_of_all_elements_located(MainLocators.AIRPORTS))[-1]).perform()
        airports = [airport.accessible_name for airport in self.wait.until(EC.visibility_of_all_elements_located(MainLocators.AIRPORTS))]
        airports_counts = dict((self.process_airport_count(ap) for ap in self.driver.find_elements(*MainLocators.AIRPORT_COUNT_PER_DEST)))
        for key, value in airports_counts.items():
            airport_array[key] = ["" for i in range(value)]

        for destination, array in airport_array.items():
            if not destination in airports_counts:
                continue
            replacer = self.replace_range(airports)
            airport_array[destination] = replacer(array)
        
        self.actions.send_keys(Keys.HOME).perform()
        return airport_array
    
    def input_departure_arrival_date(self, date: str, departure: bool = True):
        fields = self.wait.until(EC.presence_of_all_elements_located(MainLocators.DEPARTURE_RETURN_INPUTS))
        field = fields[0] if departure else fields[1]
        self.actions.click(field).perform()
        for char in date:
            self.actions.send_keys_to_element(field, char).perform()
        self.actions.send_keys_to_element(field, Keys.ENTER).perform()
        buttons = self.safe_find_all(MainLocators.DONE_BUTTON, False)
        self.actions.click(buttons[-1]).perform()
    
    def click_search(self):
        button = self.safe_find_all(MainLocators.SEARCH_BUTTON)[0]
        self.actions.click(button).perform()

    def process_airport_count(self, element: WebElement):
        parent = element.find_element(By.XPATH, "..").accessible_name
        airport_count = find_number(element.get_attribute("textContent"))
        return (parent, airport_count)

    def replace_range(self, source: list):

        def _replacer(target: list):
            result = source[self.iterator:self.iterator + len(target)]
            self.iterator += len(target)
            return result
        self.iterator = 0
        return _replacer

def find_number(text: str):
    """
    Find the first number in a string.
    
    Args:
        text (str): The string to search.
    Returns:
        int: The first number found in the string, or None if no number is found.
    """
    result = re.search(r"Showing (\d+) nearby", text)
    return int(result.group(1)) if result else None

def normalize(text):
    # Normalize accents
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    # Replace typographic dashes with a standard hyphen
    text = re.sub(r"[–—−]", "-", text)
    return text.lower()
