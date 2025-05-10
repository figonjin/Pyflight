import time

from drivers.driver_factory import create_driver, AllowedBrowsers
from pages.google_flights.main_page import MainPage
from pages.google_flights.flight_details_config import FlightDetails

def main():
    driver = create_driver(AllowedBrowsers.CHROME)

    main_page = MainPage(driver)
    flight_config = FlightDetails(driver)
    main_page.open()
    flight_config.input_flight_source("Paris")
    flight_config.scrape_airports()
    time.sleep(2)

if __name__ == "__main__":
    main()
