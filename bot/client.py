import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    client = Client(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET")
    )

    # 🔥 FORCE DEMO FUTURES ENDPOINT
    client.FUTURES_URL = "https://demo-fapi.binance.com"

    return client