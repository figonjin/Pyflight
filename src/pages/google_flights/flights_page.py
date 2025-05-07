import random

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.consent_form.consent_page import ConsentPage
from .flights_locators import FlightsLocators, PASSENGER_TYPES
from .explore_locators import ExploreLocators

class FlightsPage:
    """
    Google Flights Page Object
    """
    URL = "https://www.google.com/travel/flights/"
    TITLE = "Google Flights"

    def __init__(self, driver: (WebDriver| None)):
        self.driver = driver
        self.passengers = 1
        self.passenger_cap = 9
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        self.handle_consent()

    def handle_consent(self):
        if self.driver.title == ConsentPage.TITLE:
            consent_page = ConsentPage(self.driver)
            consent_page.click_reject()
            self.wait.until(EC.title_contains(self.TITLE))

    def click_explore(self):
        button = self.wait.until(EC.element_to_be_clickable(FlightsLocators.EXPLORE_BUTTON))
        ActionChains(self.driver).pause(random.uniform(1, 3)).click(button).perform()
        button.click()
        self.wait.until(EC.visibility_of_element_located(ExploreLocators.MAP_TAG))
    
    def click_ticket_type(self):
        button = self.wait.until(EC.element_to_be_clickable(FlightsLocators.TICKET_TYPE))
        ActionChains(self.driver).pause(random.uniform(1, 3)).click(button).perform()
        self.wait.until(EC.visibility_of_element_located(FlightsLocators.TICKET_TYPE_DROPDOWN))

    def click_passenger(self):
        button = self.wait.until(EC.element_to_be_clickable(FlightsLocators.PASSENGER))
        ActionChains(self.driver).pause(random.uniform(1, 3)).click(button).perform()
        self.wait.until(EC.visibility_of_element_located(FlightsLocators.PASSENGER_DROPDOWN))
    
    def click_flight_class(self):
        button = self.wait.until(EC.element_to_be_clickable(FlightsLocators.FLIGHT_CLASS))
        ActionChains(self.driver).pause(random.uniform(1, 3)).click(button).perform()
        self.wait.until(EC.visibility_of_element_located(FlightsLocators.FLIGHT_CLASS_DROPDOWN))

    def select_element_in_dropdown(self, element: int):
        match element:
            case 1:
                button = self.wait.until(EC.element_to_be_clickable(FlightsLocators.FIRST_ELEMENT))
                ActionChains(self.driver).pause(random.uniform(1, 3)).click(button).perform()
            case 2:
                button = self.wait.until(EC.element_to_be_clickable(FlightsLocators.SECOND_ELEMENT))
                ActionChains(self.driver).pause(random.uniform(1, 3)).click(button).perform()
            case 3:
                button = self.wait.until(EC.element_to_be_clickable(FlightsLocators.THIRD_ELEMENT))
                ActionChains(self.driver).pause(random.uniform(1, 3)).click(button).perform()
    
    # def adjust_passenger_amount(self, passenger_type: PASSENGER_TYPES, amount: int):
    #     match passenger_type:
    #         case PASSENGER_TYPES.ADULT:
