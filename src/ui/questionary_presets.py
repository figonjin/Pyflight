import questionary

class MainFlow:

    def __init__(self):
        self.source: str
        self.destination: str
        self.flight_class: str
        self.passenger_amount_adult: int
        self.passenger_amount_child: int
        self.passenger_amount_infant_lap: int
        self.passenger_amount_infant_seat: int
        self.departure_date: str
        self.return_date: str


    def program_start(self):
        return questionary.select(
            "What would you like to do?",
            choices=["Find a Flight", "Explore Flights", "Quit"]
            ).ask()
    
    # def flight_source(self, default_source: str):
    #     start_from_default = questionary.confirm(
    #         f"Would you like your flight to start from {default_source}?"
    #     ).ask()

    #     if start_from_default:
    #         self.source = default_source
    #         return
    #     else:
            