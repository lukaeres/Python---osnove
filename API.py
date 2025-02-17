import requests

#  API ključ koji sam uzeo nakon kreiranja racuna na CMC developer forum
API_KEY = "3623765e-0884-4fa9-9c01-05cb55785e2c"
URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

# Parametri za API zahtjev
params = {
    "start": 1,   # Počinje od prve kriptovalute
    "limit": 10,   # Dohvaća samo top 10
    "convert": "USD"  # Konverzija u USD
}

# Zaglavlje
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": API_KEY
}

# Slanje zahtjeva CoinMarketCap API-ju
response = requests.get(URL, headers=headers, params=params)


if response.status_code == 200:     #trazimo jednakonst sa 200 jer je to oznaka za uspjesnu autorizaciju
    data = response.json()  # Parsiranje JSON odgovora
    cryptos = data["data"]  # Lista top 10 kriptovaluta
    
    # Ispis rezultata
    for crypto in cryptos:
        name = crypto["name"]
        price = crypto["quote"]["USD"]["price"]
        print(f"{name}: ${price:.2f}")
else:
    print("Greška pri dohvaćanju podataka!", response.status_code)
