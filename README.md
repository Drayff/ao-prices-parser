# Albion Online Item Prices Fetcher
![GitHub](https://img.shields.io/github/license/Drayff/ao-prices-parser)

A tool to fetch and display item prices for the Albion Online game.

## Features

- Fetches item prices from the Albion Online API.
- Displays minimum and maximum sell and buy prices for each item.
- Supports specifying a game location for price retrieval.

## Installation

1. Clone the repository: `git clone https://github.com/Drayff/ao-prices-parser.git`.
2. Navigate to the project directory: `cd ao-prices-parser`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Specify the city for the price parse in `config.ini`.

## Usage

1. Run the `python process_items_file.py` script to create an "items.txt" file with the item id, or create the "items.txt" file yourself and enter the parsing IDs you need.
2. Run the script: `python fetch_prices.py` to start items parcer.

## Contributions

Contributions are welcome!
