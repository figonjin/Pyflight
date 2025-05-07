import time

from drivers.driver_factory import create_driver, AllowedBrowsers
from pages.google_flights.flights_page import FlightsPage


def main():
    driver = create_driver(AllowedBrowsers.CHROME)

    flights_page = FlightsPage(driver)
    flights_page.open()
    flights_page.click_ticket_dropdown()
    time.sleep(10)

if __name__ == "__main__":
    main()
