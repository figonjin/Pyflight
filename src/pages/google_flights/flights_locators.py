"""
Google Flights Main Page Locators
"""
from selenium.webdriver.common.by import By
from enum import Enum, auto

class PASSENGER_TYPES(Enum):
    ADULT = auto()
    CHILD = auto()
    SEAT_INFANT = auto()
    LAP_INFANT = auto()

class FlightsLocators:
    """
    Locators for Google Flights page elements.
    """
    # Main search widget
    SEARCH_FLIGHTS = (By.CSS_SELECTOR, "div[role='search']")
    EXPLORE_BUTTON = (
        By.CSS_SELECTOR, "button[aria-label='Explore destinations']")

    # Flight locations selectors
    SOURCE_INPUT = (By.CSS_SELECTOR, "input[aria-label='Where from?']")
    DESTINATION_INPUT = (By.CSS_SELECTOR, "input[aria-label='Where to?']")

    # Flight locations dropdown
    NO_LOCATIONS_FOUND_ALERT = (By.CSS_SELECTOR, "div[role='alert']:not([jsname])")

    # Flight dates selectors
    DEPARTURE_INPUT = (By.CSS_SELECTOR, "div[data-state] input[aria-label='Departure']")
    RETURN_INPUT = (By.CSS_SELECTOR, "div[data-state] input[aria-label='Return']")

    TICKET_TYPE = (By.CSS_SELECTOR, "span[aria-label='Change ticket type.'] + span")
    TICKET_TYPE_DROPDOWN = (By.CSS_SELECTOR, "div[data-menu-uid] ul[aria-label='Select your ticket type.']:not([tabindex])")

    FLIGHT_CLASS = (By.CSS_SELECTOR, "span[aria-label='Change seating class.'] + span")
    FLIGHT_CLASS_DROPDOWN = (By.CSS_SELECTOR, "div[data-menu-uid] ul[aria-label='Select your preferred seating class.']:not([tabindex])")

    PASSENGER = (By.CSS_SELECTOR, "button[aria-label*='passenger']")
    PASSENGER_DROPDOWN = (By.CSS_SELECTOR, "div[aria-label='Number of passengers']")

    # Dropdown element selectors
    FIRST_ELEMENT = (By.CSS_SELECTOR, "li[data-value='1']")
    SECOND_ELEMENT = (By.CSS_SELECTOR, "li[data-value='2']")
    THIRD_ELEMENT = (By.CSS_SELECTOR, "li[data-value='3']")

    # Dropdown passenger selectors
    ADD_ADULT = (By.CSS_SELECTOR, "button[aria-label='Add adult']")
    REMOVE_ADULT = (By.CSS_SELECTOR, "button[aria-label='Remove adult']")
    ADD_CHILD = (By.CSS_SELECTOR, "button[aria-label='Add child']")
    REMOVE_CHILD = (By.CSS_SELECTOR, "button[aria-label='Remove child']")
    ADD_INFANT_SEAT = (By.CSS_SELECTOR, "button[aria-label='Add infant in seat']")
    REMOVE_INFANT_SEAT = (By.CSS_SELECTOR, "button[aria-label='Remove infant in seat']")
    ADD_INFANT_LAP = (By.CSS_SELECTOR, "button[aria-label='Add infant on lap']")
    REMOVE_INFANT_LAP = (By.CSS_SELECTOR, "button[aria-label='Remove infant on lap']")

    # Passenger count
    ADULT_COUNT = (
        By.CSS_SELECTOR,
        "div[aria-label='Number of adult passengers'] span[aria-atomic] > span"
        )
    CHILD_COUNT = (
        By.CSS_SELECTOR,
        "div[aria-label='Number of children aged 2 to 11'] span[aria-atomic] > span"
        )
    INFANT_SEAT_COUNT = (
        By.CSS_SELECTOR,
        "div[aria-label='Number of infants in their own seat'] span[aria-atomic] > span"
        )
    INFANT_LAP_COUNT = (
        By.CSS_SELECTOR,
        "div[aria-label='Number of infants on lap'] span[aria-atomic] > span"
        )
