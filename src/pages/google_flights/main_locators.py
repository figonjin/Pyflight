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
    SEARCH_BUTTON = (By.CSS_SELECTOR, f"{SEARCH_FLIGHTS[1]} button[aria-label][jslog]:not([tabindex])")

    # Flight locations selectors
    SOURCE_INPUT = (By.CSS_SELECTOR, "div[jscontroller][jsname][class] input[type='text'][aria-expanded='false']:not([value=''])")
    DESTINATION_INPUT = (By.CSS_SELECTOR, "div[jscontroller][jsname][class] input[type='text'][aria-expanded='false'][value='']")

    # Flight locations dropdown
    NO_LOCATIONS_FOUND_ALERT = (By.CSS_SELECTOR, "div[role='alert']:not([jsname])")

    # Flight dates selectors
    DEPARTURE_RETURN_INPUTS = (By.CSS_SELECTOR, "div[data-state] div[jscontroller] input")


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

    # Dates selectors
    DATES_GRID = (By.CSS_SELECTOR, "div[role='grid']")
    DATES_ROWGROUPS = (By.CSS_SELECTOR, "div[role='grid'] div[role='rowgroup']")
    AVAILABLE_MONTHS = (By.CSS_SELECTOR, f"{DATES_ROWGROUPS[1]} > div[class]:not([jsname]):not([aria-hidden])")
    DAY_ROWS = (By.CSS_SELECTOR, f"{DATES_ROWGROUPS[1]} > div[jsname]")
    AVAILABLE_DAYS = (By.CSS_SELECTOR, f"{DAY_ROWS[1]} div[aria-hidden='false']")
    DAY_LABELS = (By.CSS_SELECTOR, f"{AVAILABLE_DAYS[1]} div > div:not([data-gs])")
    DAY_PRICES = (By.CSS_SELECTOR, f"{AVAILABLE_DAYS[1]} div > div[data-gs]")
    DONE_BUTTON = (By.CSS_SELECTOR, "div[tabindex='-1'][jsslot][role='dialog'][jsowner]:not([data-ved]) button[tabindex='-1'][aria-label]") # last element

    # Flights
    TOP_FLIGHTS = (By.CSS_SELECTOR, "div h3 + div + ul")
    OTHER_FLIGHTS = (By.CSS_SELECTOR, "div h3 + ul") # target element 0
    TOP_MORE_FLIGHTS_BUTTON = (By.CSS_SELECTOR, "div h3 + div + ul li[data-ved]")
    OTHER_MORE_FLIGHTS_BUTTON = (By.CSS_SELECTOR, "div h3 + ul li[data-ved]")

    #Flight details
    TOP_FLIGHT_TIMES = (By.CSS_SELECTOR, f"{TOP_FLIGHTS[1]} li span[jsslot] > span[aria-label] > span[aria-label][role='text']")
    TOP_FLIGHT_DURATIONS = (By.CSS_SELECTOR, f"{TOP_FLIGHTS[1]} li div[class] > div[class][aria-label]:not([tabindex])") # Every 4 elements (n + 4)
    TOP_FLIGHT_PRICES = (By.CSS_SELECTOR, f"{TOP_FLIGHTS[1]} li span[data-gs][aria-label][role='text']")
    OTHER_FLIGHT_TIMES = (By.CSS_SELECTOR, f"{OTHER_FLIGHTS[1]} li span[jsslot] > span[aria-label] > span[aria-label][role='text']")
    OTHER_FLIGHT_DURATIONS = (By.CSS_SELECTOR, f"{OTHER_FLIGHTS[1]} li div[class] > div[class][aria-label]:not([tabindex])") # Every 4 elements (n + 4)
    OTHER_FLIGHT_PRICES = (By.CSS_SELECTOR, f"{OTHER_FLIGHTS[1]} li span[data-gs][aria-label][role='text']")