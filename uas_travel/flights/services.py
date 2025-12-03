import os
from pathlib import Path
from amadeus import Client, ResponseError
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / '.env'

load_dotenv(ENV_FILE)

API_KEY = os.getenv('AMADEUS_API_KEY')
API_SECRET = os.getenv('AMADEUS_API_SECRET')

if not API_KEY or not API_SECRET:
    print(f"--- DEBUG INFO ---")
    print(f"Mencari .env di: {ENV_FILE}")
    print(f"File ditemukan?: {ENV_FILE.exists()}")
    print(f"API Key status: {'OK' if API_KEY else 'MISSING'}")
    print(f"------------------")
    raise ValueError("API Key atau Secret tidak ditemukan di file .env")

# Client Initialization
amadeus = Client(
    client_id=API_KEY,
    client_secret=API_SECRET
)

def search_flight_offers(origin, destination, departure_date, return_date=None):
    try:
        kwargs = {
            'originLocationCode': origin,
            'destinationLocationCode': destination,
            'departureDate': departure_date,
            'adults': 1, 
            'currencyCode': 'IDR',
            'max': 10
        }
        
        if return_date:
            kwargs['returnDate'] = return_date

        response = amadeus.shopping.flight_offers_search.get(**kwargs)
        return response.data

    except ResponseError as error:
        print(f"Amadeus API Error: {error}")
        return None