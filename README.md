# Simple web scraper

This repository contains the code for a web scraping project developed as part of the GoIT web course homework.

## Features

- Scrapes quotes from a specified website.
- Saves the scraped quotes into a json file.

## Main Files

- `quotes.py`: Contains the `get_quotes` function for scraping quotes from a website.
- `load_data.py`: Contains the `load_data` function for loading data from a JSON file.
- `main.py`: Main script to run the application, which prints quotes and loaded data.
- `models.py`: Defines the `QuoteModel` class for representing quotes.

## Setup

### Requirements

- python = "^3.12"
- scrapy = "^2.11.2"
- pymongo = "^4.8.0"

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Danyil-SY/goit-web-hw-09.git
    cd goit-web-hw-09
    ```

2. Install Poetry if you haven't already:

    ```bash
    pip install poetry
    ```

3. Install the project dependencies:

    ```bash
    poetry install
    ```

## Usage

1. Run the scraper:

    ```bash
    python main.py
    ```

2. The scraped quotes will be saved in a `quotes.json` and `authors.json` files in the project directory.
