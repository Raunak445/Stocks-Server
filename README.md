# Stocks API Server

This Flask server provides an API endpoint to retrieve stock prices and pagination information.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Raunak445/Stocks-Server
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask server:

    ```bash
    python app.py
    ```

2. The server will start running locally at `http://127.0.0.1:5000/`.

## Endpoints

### GET /stock-prices

This endpoint returns stock prices along with pagination information.

#### Parameters

- `page` (optional): The page number to retrieve. Defaults to `1`.

#### Response

- `data`: An object containing stock tickers and their corresponding prices.
- `totalPages`: Total number of pages available.

Example response:

```json
{
    "data": {
        "INFY": 150.25,
        "RELIANCE": 2500.65,
        "TCS": 3200.45
        // Other stock tickers and prices
    },
    "totalPages": 4
}
