# Rate Scraper

This is an endpoint built on python's fastAPI to return the black market rates of Nigeria

## Installation

You'll need a virtual environment to install necessary requirements

```bash
virtualenv venv
```

Activate virtual environment

```bash
source venv/bin/activate
```

Install necessary requirements

```bash
pip install -r requirements.txt
```

## Usage
Run the application

```bash
uvicorn main:app
```

Use a GET request to call `http://127.0.0.1:8000/get_rates`

## Expected Response

Response is a json data

{
    "data": {
        "black_market": 740.0,
        "cbn": 440.0
    }
}


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
