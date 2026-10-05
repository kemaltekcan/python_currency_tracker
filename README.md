# 🪙 Python Currency & Forex Tracker (CLI)

A modular, object-oriented Command Line Interface (CLI) application built with Python 3.12 that fetches real-time foreign exchange (Forex) rates via REST API and handles cross-currency conversions.

Designed following **Separation of Concerns** and **SOLID** principles to demonstrate clean code standards and scalable software design.

---

## 🏗 Architecture & Modules

The application is structured into four distinct modules to enforce high cohesion and low coupling:

* **`api_client.py` (`CurrencyAPI`)**: Handles network requests to the ExchangeRate-API endpoint, network timeout configs, and error handling.
* **`converter.py` (`CurrencyConverter`)**: Encapsulates business logic, including USD-base cross-currency calculation models (e.g., JPY/TRY).
* **`ui.py` (`TerminalUI`)**: Manages CLI outputs, dynamic dashboard rendering, and user input workflows.
* **`main.py`**: Acts as the entry point and orchestrates interactions between the core modules.

---

## 🚀 Key Features

* **Live Exchange Rates**: Real-time USD, EUR, GBP, and JPY tracking mapped to TRY.
* **Cross-Currency Converter**: Accurate cross-rate conversion logic utilizing USD-base calculations.
* **Robust Error Handling**: Graceful exception catches for network timeouts and invalid currency inputs.
* **Modular Design**: Easy to extend for GUI/Web integrations or new external API endpoints.

---

## 🛠 Tech Stack

* **Language**: Python 3.12
* **Libraries**: `requests`
* **API**: ExchangeRate-API (USD-base)

---

## 📦 Installation & Running

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kemaltekcan/python_currency_tracker.git](https://github.com/kemaltekcan/python_currency_tracker.git)
   cd python_currency_tracker