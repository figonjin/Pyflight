"""
Google Flights Main Page Locators
"""
from selenium.webdriver.common.by import By

class MainLocators:
    """
    Locators for Google Flights page elements.
    """
    # Main search widget
    SEARCH_FLIGHTS = (By.CSS_SELECTOR, "div[role='search']")
    EXPLORE_BUTTON = (
        By.CSS_SELECTOR, "div[role='button'][aria-label][tabindex][jsname][style] + div button")

    # Flight locations selectors
    SOURCE_INPUT = (By.CSS_SELECTOR, "div[jscontroller][jsname][class] input[type='text'][aria-expanded='false']:not([value=''])")
    DESTINATION_INPUT = (By.CSS_SELECTOR, "div[jscontroller][jsname][class] input[type='text'][aria-expanded='false'][value='']")

    # Flight locations dropdown
    NO_LOCATIONS_FOUND_ALERT = (By.CSS_SELECTOR, "div[role='alert']:not([jsname])")

    # Flight dates selectors
    DEPARTURE_RETURN_INPUTS = (By.CSS_SELECTOR, "div[data-state] div[jscontroller] div[data-value] input")


    # Ticket type selections
    TICKET_SELECTION = (By.CSS_SELECTOR, "div[data-allow-empty-dates]:not([data-enable-prices]) > div[jsaction]")

    TICKET_TYPE_FLIGHT_CLASS_BUTTONS = (By.CSS_SELECTOR, f"{TICKET_SELECTION[1]} div[tabindex='0']")
    PASSENGERS_BUTTON = (By.CSS_SELECTOR, f"{TICKET_SELECTION[1]} div[data-max]")

    # Ticket Dropdown element selectors
    TICKET_TYPE_ROUND_TRIP = (By.CSS_SELECTOR, "ul:not([tabindex]) li[data-value='1']")
    TICKET_TYPE_ONE_WAY = (By.CSS_SELECTOR, "ul:not([tabindex]) li[data-value='2']")
    TICKET_TYPE_MULTI_CITY = (By.CSS_SELECTOR, "ul:not([tabindex]) li[data-value='3']")

    # Ticket class element selectors
    TICKET_CLASS_ECONOMY = (By.CSS_SELECTOR, "ul:not([tabindex]) li[data-value='1'][jslog]")
    TICKET_CLASS_PREIMUM_ECONOMY = (By.CSS_SELECTOR, "ul:not([tabindex]) li[data-value='2'][jslog]")
    TICKET_CLASS_BUSINESS = (By.CSS_SELECTOR, "ul:not([tabindex]) li[data-value='3'][jslog]")
    TICKET_CLASS_FIRST = (By.CSS_SELECTOR, "ul:not([tabindex]) li[data-value='4'][jslog]")

    #Passenger dropdown
    PASSENGER_DROPDOWN = (By.CSS_SELECTOR, "div[data-allow-empty-dates]:not([data-enable-prices]) > div[jsaction] div[data-max] ul")
    PASSENGER_CONFIRM_CANCEL_BUTTONS = (By.CSS_SELECTOR, f"{PASSENGER_DROPDOWN[1]} + div button")

    # Dropdown passenger selectors
    ADD_SUBSTRACT_BUTTONS = (By.CSS_SELECTOR, f"{PASSENGER_DROPDOWN[1]} span[data-is-tooltip-wrapper] button")
    PASSENGER_COUNTERS = (By.CSS_SELECTOR, f"{PASSENGER_DROPDOWN[1]} span[aria-atomic] > span:not([class])")

    # SourceDest Dropdown selectors
    DROPDOWN_CONTAINER = (By.CSS_SELECTOR, "ul[role='listbox'][aria-multiselectable='true']")
    DROPDOWN_SUBSECTION_BUTTONS = (By.CSS_SELECTOR, f"{DROPDOWN_CONTAINER[1]} button")
    MAJOR_DESTINATIONS = (By.CSS_SELECTOR, f"{DROPDOWN_CONTAINER[1]} li:not([data-ved])") # check aria-label
    
    AIRPORT_COUNT_PER_DEST = (By.CSS_SELECTOR, f"{MAJOR_DESTINATIONS[1]} div[data-toggle]")
    AIRPORTS = (By.CSS_SELECTOR, f"{DROPDOWN_CONTAINER[1]} li[data-ved]") # check aria-label
    AIRPORT_DISTANCE = (By.CSS_SELECTOR, f"{AIRPORTS[1]} div div[id]") # check text
