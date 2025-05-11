"""
FlightDetails class for Google Flights
"""
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
    """
    Page object for the Google Flights flight details page.
    """
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

    def safe_input(self, text: str, destination: bool = True):
        """
        Safely inputs text into a flight search field.
        Args:
            text (str): The text to input.
            destination (bool): Whether the input is for the destination field.
        """
        selector = "div[jscontroller][jsname][class] input[type='text'][aria-expanded='false'][value]"
        if destination:
            selector = selector[:-1] + "='']"
        js_script = f'''
        let input = document.querySelector("{selector}");
        input.value = "{text}";
        input.dispatchEvent(new Event('input', {{bubbles: true}}));
        input.dispatchEvent(new Event('change', {{bubbles: true}}));
        return input;
        '''
        self.driver.execute_script(js_script)

    def input_flight_source(self, source: str):
        """
        Safely inputs text into the flight source field.
        Args:
            source (str): The source airport or city.
        """
        self.safe_input(source, False)
        time.sleep(1)        

    def input_flight_destination(self, dest: str):
        """
        Safely inputs text into the flight destination field.
        Args:
            dest (str): The destination airport or city.
        """
        self.safe_input(dest)
        time.sleep(1)

    def select_airport(self, airport: str):
        """
        Selects an airport from the dropdown list.
        Args:
            airport (str): The airport to select.
        """
        all_airports = self.scrape_airports()
        for destinations, airports in all_airports.items():
            if normalize(airport) in normalize(destinations):
                time.sleep(0.1)
                elements = self.safe_find_all(MainLocators.MAJOR_DESTINATIONS, True)
                self.actions.click(elements[0]).perform()
                time.sleep(0.5)
                return
            if any(airport in item for item in airports):
                elements = self.safe_find_all(MainLocators.AIRPORTS, True)
                for element in elements:
                    selection = element.find_element(By.CSS_SELECTOR, "div[class][jsname]")
                    if airport in selection.text:
                        self.actions.move_to_element(selection).pause(1).click(selection).perform()
                        time.sleep(0.5)
                        return


    def scrape_airports(self):
        """
        Scrapes the airport data from the dropdown menu.
        Returns:
            dict: A dictionary with major destinations as keys and lists of airports as values.
        """
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
    
    def input_departure_arrival_date(self, date_string: str, departure: bool = True):
        """
        Inputs a date into either departure or arrival field using JavaScript.
        
        Args:
            date_string (str): Date in the format expected by the site (e.g., "MM/DD/YYYY")
            departure (bool): Whether this is for departure (True) or return (False)
        """
        index = 0 if departure else 1
        fields = self.wait.until(EC.presence_of_all_elements_located(MainLocators.DEPARTURE_RETURN_INPUTS))
        field = fields[index]
        
        self.actions.click(field).perform()
        time.sleep(0.5)
        
        js_script = f"""
        arguments[0].value = '{date_string}';
        arguments[0].dispatchEvent(new Event('input', {{bubbles: true}}));
        arguments[0].dispatchEvent(new Event('change', {{bubbles: true}}));
        """
        self.driver.execute_script(js_script, field)
        time.sleep(1)
        field.send_keys(Keys.ENTER)
        buttons = self.safe_find_all(MainLocators.DONE_BUTTON, False)
        self.actions.click(buttons[-1]).perform()
        time.sleep(0.5)
    
    def click_search(self):
        """
        Clicks the search button on the Google Flights page.
        """
        button = self.safe_find_all(MainLocators.SEARCH_BUTTON)[0]
        self.actions.click(button).perform()

    def process_airport_count(self, element: WebElement):
        """
        Process the airport count from the element.
        Args:
            element (WebElement): The WebElement containing the airport count.
        Returns:
            tuple: A tuple containing the parent element's accessible name and the airport count.
        """
        parent = element.find_element(By.XPATH, "..").accessible_name
        airport_count = find_number(element.get_attribute("textContent"))
        return (parent, airport_count)

    def replace_range(self, source: list):
        """
        Replace a range of elements in a list with another list.
        Args:
            source (list): The source list to replace elements from.
        Returns:
            function: A function that takes a target list and returns the replaced elements.
        """
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

def normalize(text: str):
    """
    Normalize the text by removing accents and replacing typographic dashes with a standard hyphen.
    Args:
        text (str): The string to normalize.
    Returns:
        str: The normalized string 
    """
    # Normalize accents
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    # Replace typographic dashes with a standard hyphen
    text = re.sub(r"[–—−]", "-", text)
    return text.lower()
