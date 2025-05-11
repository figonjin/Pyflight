Sure! Here's a clean and professional version of your README in proper Markdown formatting:

---

# Pyflight

**Pyflight** is a Python-based automation tool for fetching flight ticket information from **Google Flights**. It leverages **Selenium WebDriver** to interact with the website and enables users to search flights, configure travel preferences, and scrape flight details.

---

## ✈️ Features

* **Automated Flight Search**: Specify source, destination, departure, and return dates.
* **Passenger Configuration**: Set the number of adults, children, infants, and choose ticket types and flight classes.
* **Flight Data Scraping**: Extract details such as departure/arrival times, durations, and ticket prices.
* **Consent Handling**: Automatically bypass Google’s consent form.
* **Browser Support**: Fully supports **Chrome**; **Firefox** support is partially implemented.

---

## 📁 Project Structure

```
pyflight/
├── chrome_pyflight/          # Chrome user data (ignored by .gitignore)
├── firefox_pyflight/         # Firefox user data (ignored by .gitignore)
├── src/
│   ├── drivers/
│   │   └── driver_factory.py         # Factory for creating WebDriver instances
│   ├── main.py                       # Entry point for the application
│   └── pages/
│       ├── consent_form/
│       │   ├── consent_locators.py   # Locators for Google's consent elements
│       │   └── consent_page.py       # Page object for handling the consent form
│       └── google_flights/
│           ├── explore_locators.py         # Locators for the Explore page
│           ├── flight_details_config.py    # Configures flight details
│           ├── flights_list_page.py        # Scrapes the flights list
│           ├── main_locators.py            # Main Google Flights page locators
│           ├── main_page.py                # Page object for the main page
│           ├── passenger_ticket_config.py  # Configures passengers and tickets
│           └── search_locators.py          # Search page locators
│
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Ignored files/directories
```

---

## ⚙️ Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd pyflight
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download WebDriver**:

   * Download the appropriate WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/chromium.org/driver/)).
   * Make sure it is available in your system’s `PATH`.

---

## 🚀 Usage

Run the main script:

```bash
python src/main.py
```

This will:

1. Open Google Flights in a browser.
2. Handle the Google consent form.
3. Configure passenger count, ticket type, and flight class.
4. Enter source and destination airports.
5. Input departure and return dates.
6. Scrape and display flight details.

---

## 🛠️ Configuration

* **Browser Selection**: Change the `create_driver()` function in `driver_factory.py` to switch between Chrome and Firefox.
* **Interaction Delays**: Modify `min_action_delay` and `max_action_delay` in the page objects for more human-like interactions.

---

## ⚠️ Known Issues

* Firefox support is currently **incomplete** and commented out.
* Google Flights UI changes may break some element locators over time.
* Occasional random index errors, timeouts and others due to Google's DOM manipulation during runtime
* If the search result doesn't find any flights due to user settings, the program will crash
---

## 🤝 Potential Improvements

* Add a UI to actualy allow a user to interact with the program
* Add handling for other browsers
* Add options to scrape return tickets, allow the user to explore, etc.
* General structure cleanup
* Refactoring, refactoring, refactoring
* Actual error handling