from selenium.webdriver.common.by import By

class SearchLocators:
    DEPARTING_FLIGHTS_CONTAINER = (By.CSS_SELECTOR, 'h3[class][tabindex] + div + ul')
    FLIGHTS = (By.CSS_SELECTOR, f'{DEPARTING_FLIGHTS_CONTAINER[1]} li')
    FLIGHT_DETAILS_BUTTON = (By.CSS_SELECTOR, f'{FLIGHTS[1]} div[data-ved]:not([class]) button')
    FLIGHT_PRICES = (By.CSS_SELECTOR, f'{FLIGHTS[1]} div span[data-gs]') # Hacky. Requires using %3 on the result, checking every third result, + remainder for the last element

