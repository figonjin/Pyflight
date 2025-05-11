import time

from drivers.driver_factory import create_driver, AllowedBrowsers
from pages.google_flights.main_page import MainPage
from pages.google_flights.flight_details_config import FlightDetails
from pages.google_flights.passenger_ticket_config import PassengerTicketConfig
from pages.google_flights.flights_list_page import FlightsList


def main():
    driver = create_driver(AllowedBrowsers.CHROME)

    main_page = MainPage(driver)
    flight_config = FlightDetails(driver)
    passenger_config = PassengerTicketConfig(driver)
    flights_list = FlightsList(driver)

    main_page.open()
    passenger_config.select_ticket_type(0)
    passenger_config.adjust_passenger_amount(0, 4)
    passenger_config.select_flight_class(0)
    flight_config.input_flight_source("Adolfo Suarez Madrid-Barajas Airport")
    flight_config.select_airport("Adolfo Suarez Madrid-Barajas Airport")
    flight_config.input_flight_destination("Pari")
    flight_config.select_airport("Paris")
    flight_config.input_departure_arrival_date('06-01')
    flight_config.input_departure_arrival_date('07-01', False)
    flight_config.click_search()
    flights_list.expand_all()
    time.sleep(500)
    main_page.open()

if __name__ == "__main__":
    main()
