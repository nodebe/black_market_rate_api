from bs4 import BeautifulSoup as bs
import requests

# This is to format the string received to dictionary
bm = 'black_market'
cbn = 'cbn'
bdc = 'bdc'
moneygram = 'moneygram'
westernunion = 'westernunion'
fx = 'fx'

def get_current_rates():
    url = 'https://nairatoday.com/liverates.html'
    soup = bs(requests.get(url).text, 'html.parser')

    # This is the required rates
    needed = ['black_market', 'cbn']
    needed_rates = {}

    # Getting the current exchanges from the script tag
    script = soup.find('script').text

    # Formating the response to dictionary
    current_rates = eval(script.split('=')[1].strip(' ;'))

    # Accessing only needed exchanges and storing in needed_rates
    for key, value in current_rates.items():
        if key in needed:
            needed_rates[key] = value[0]

    return needed_rates
