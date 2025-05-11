import random
from typing import Optional

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .main_locators import MainLocators


class PassengerTicketConfig:
    def __init__(self, driver: Optional[WebDriver]):
        self.driver = driver
        self.min_action_delay = 0.5
        self.max_action_delay = 0.9
        self.wait = WebDriverWait(driver, 10)

    @property
    def ticket_type_flight_class_buttons(self):
        """
        Returns the ticket type and flight class buttons.
        """
        ticket_type, flight_class = self.driver.find_elements(*MainLocators.TICKET_TYPE_FLIGHT_CLASS_BUTTONS)
        return (ticket_type, flight_class) if ticket_type and flight_class else (None, None)

    @property
    def adult_passenger_amount_buttons(self):
        """
        Returns the adult passenger amount buttons.
        """
        elements = self.driver.find_elements(*MainLocators.ADD_SUBSTRACT_BUTTONS)
        buttons = [elements[0], elements[1]]
        return buttons

    @property
    def child_passenger_amount_buttons(self):
        """
        Returns the child passenger amount buttons.
        """
        elements = self.driver.find_elements(*MainLocators.ADD_SUBSTRACT_BUTTONS)
        buttons = [elements[2], elements[3]]
        return buttons

    @property
    def infant_lap_passenger_amount_buttons(self):
        """
        Returns the infant lap passenger amount buttons.
        """
        elements = self.driver.find_elements(*MainLocators.ADD_SUBSTRACT_BUTTONS)
        buttons = [elements[4], elements[5]]
        return buttons

    @property
    def infant_seat_passenger_amount_buttons(self):
        """
        Returns the infant seat passenger amount buttons.
        """
        elements = self.driver.find_elements(*MainLocators.ADD_SUBSTRACT_BUTTONS)
        buttons = [elements[6], elements[7]]
        return buttons

    @property
    def passenger_amount_indicators(self):
        """
        Returns the passenger amount indicators.
        """
        elements = self.driver.find_elements(*MainLocators.PASSENGER_COUNTERS)
        buttons = [elements[0], elements[1], elements[2], elements[3]]
        return buttons
    
    @property
    def passenger_confirm_cancel_buttons(self):
        """
        Returns the passenger confirm and cancel buttons.
        """
        elements = self.driver.find_elements(*MainLocators.PASSENGER_CONFIRM_CANCEL_BUTTONS)
        buttons = [elements[0], elements[1]]
        return buttons

    def click_ticket_type(self):
        """
        Clicks the ticket type button on the Google Flights page.
        """
        ticket_type_button = self.ticket_type_flight_class_buttons[0]
        button = self.wait.until(EC.element_to_be_clickable(ticket_type_button))
        ActionChains(self.driver).pause(random.uniform(self.min_action_delay, self.max_action_delay)).click(button).perform()
        self.wait.until(EC.visibility_of_element_located(MainLocators.TICKET_TYPE_ROUND_TRIP))

    def click_passenger_selection(self):
        """
        Clicks the passenger selection button on the Google Flights page.
        """
        button = self.wait.until(EC.element_to_be_clickable(MainLocators.PASSENGERS_BUTTON))
        ActionChains(self.driver).pause(random.uniform(self.min_action_delay, self.max_action_delay)).click(button).perform()
        self.wait.until(EC.visibility_of_element_located(MainLocators.PASSENGER_DROPDOWN))

    def click_flight_class(self):
        """
        Clicks the flight class button on the Google Flights page.
        """
        flight_class_button = self.ticket_type_flight_class_buttons[1]
        ActionChains(self.driver).pause(random.uniform(self.min_action_delay, self.max_action_delay)).click(flight_class_button).perform()
        self.wait.until(EC.visibility_of_element_located(MainLocators.TICKET_CLASS_ECONOMY))

    def select_ticket_type(self, ticket_type: int):
        """
        Selects the ticket type on the Google Flights page.
        :param ticket_type: The ticket type to select (0: Round Trip, 1: One Way, 2: Multi City).
        """
        self.click_ticket_type()
        match ticket_type:
            case 0:
                button = self.wait.until(EC.element_to_be_clickable(MainLocators.TICKET_TYPE_ROUND_TRIP))
            case 1:
                button = self.wait.until(EC.element_to_be_clickable(MainLocators.TICKET_TYPE_ONE_WAY))
            case 2:
                button = self.wait.until(EC.element_to_be_clickable(MainLocators.TICKET_TYPE_MULTI_CITY))

        ActionChains(self.driver).pause(random.uniform(self.min_action_delay, self.max_action_delay)).click(button).perform()
        self.wait.until(EC.invisibility_of_element_located(MainLocators.TICKET_TYPE_ROUND_TRIP))

    def select_flight_class(self, ticket_class: int):
        """
        Selects the ticket class on the Google Flights page.
        :param ticket_class (int)
        """
        self.click_flight_class()
        match ticket_class:
            case 0:
                button = self.wait.until(EC.element_to_be_clickable(MainLocators.TICKET_CLASS_ECONOMY))
            case 1:
                button = self.wait.until(EC.element_to_be_clickable(MainLocators.TICKET_CLASS_PREIMUM_ECONOMY))
            case 2:
                button = self.wait.until(EC.element_to_be_clickable(MainLocators.TICKET_CLASS_BUSINESS))
            case 3:
                button = self.wait.until(EC.element_to_be_clickable(MainLocators.TICKET_CLASS_FIRST))

        ActionChains(self.driver).pause(random.uniform(self.min_action_delay, self.max_action_delay)).click(button).perform()
        self.wait.until(EC.invisibility_of_element_located(MainLocators.TICKET_CLASS_ECONOMY))
        

    def adjust_passenger_amount(self, passenger_type: int, amount: int):
        """
        Adjusts the amount of passengers for the given passenger type.
        :param passenger_type: The type of passenger (0: Adult, 1: Child, 2: Infant Lap, 3: Infant Seat).
        :param amount: The amount of passengers to set.
        """
        self.click_passenger_selection()
        amount = amount - 1 if passenger_type == 0 else amount
        match passenger_type:
            case 0:
                buttons = self.adult_passenger_amount_buttons
            case 1:
                buttons = self.child_passenger_amount_buttons
            case 2:
                buttons = self.infant_seat_passenger_amount_buttons
            case 3:
                buttons = self.infant_lap_passenger_amount_buttons
        button = buttons[0 if amount < 0 else 1]
        button = self.wait.until(EC.element_to_be_clickable(button))
        for _i in range(amount):
            ActionChains(self.driver).pause(random.uniform(0.1, 0.2)).click(button).perform()
        confirm_button = self.wait.until(EC.element_to_be_clickable(self.passenger_confirm_cancel_buttons[0]))
        ActionChains(self.driver).pause(random.uniform(self.min_action_delay, self.max_action_delay)).click(confirm_button).perform()
