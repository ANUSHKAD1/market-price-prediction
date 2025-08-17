import requests
import sqlite3
from datetime import datetime

API_KEY = "579b464db66ec23bdd00000171f04671ff624c5858b2534935fb7bc8"
DB_FILE = "market_prices.db"

def fetch_market_prices():
    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    params = {
        "api-key": API_KEY,
        "format": "json",
        "limit": 50,
        "filters[arrival_date]": datetime.now().strftime("%d/%m/%Y")
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        records = response.json().get("records", [])
        print(f"Fetched {len(records)} records.")
        return records
    else:
        print(f"API error: {response.status_code}")
        return []

def store_in_db(records):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS prices (
                    commodity TEXT,
                    variety TEXT,
                    market TEXT,
                    modal_price TEXT,
                    arrival_date TEXT
                )''')
    for r in records:
        c.execute("INSERT INTO prices VALUES (?, ?, ?, ?, ?)", (
            r.get("commodity"),
            r.get("variety"),
            r.get("market"),
            r.get("modal_price"),
            r.get("arrival_date")
        ))
    conn.commit()
    conn.close()
    print("Data stored successfully.")

if __name__ == "__main__":
    data = fetch_market_prices()
    if data:
        store_in_db(data)
    else:
        print("No data to store.")
