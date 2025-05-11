"""
Google Flights Scraper
"""

from drivers.driver_factory import create_driver, AllowedBrowsers
from pages.google_flights.main_page import MainPage
from pages.google_flights.flight_details_config import FlightDetails
from pages.google_flights.passenger_ticket_config import PassengerTicketConfig
from pages.google_flights.flights_list_page import FlightsList


def main():
    """
    Main function to run the Google Flights scraper.
    """
    driver = create_driver(AllowedBrowsers.CHROME)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})
    main_page = MainPage(driver)
    flight_config = FlightDetails(driver)
    passenger_config = PassengerTicketConfig(driver)
    flights_list = FlightsList(driver)

    main_page.open()
    passenger_config.select_ticket_type(0)
    passenger_config.adjust_passenger_amount(0, 4)
    passenger_config.select_flight_class(0)
    flight_config.input_flight_source("Madrid")
    flight_config.select_airport("Madrid")
    flight_config.input_flight_destination("Paris")
    flight_config.select_airport("Paris")
    flight_config.input_departure_arrival_date('06-01')
    flight_config.input_departure_arrival_date('07-01', False)
    flight_config.click_search()
    entries = flights_list.scrape_flights()
    for group, flights_in_group in entries.items():
        print(f"\nGroup {group}:")
        for index, flight in flights_in_group.items():
            times = f"{flight['times'][0]} → {flight['times'][1]}"
            print(f"  Flight {index}:")
            print(f"    Time: {times}")
            print(f"    Duration: {flight['duration']}")
            print(f"    Price: {flight['price']}")

if __name__ == "__main__":
    main()
