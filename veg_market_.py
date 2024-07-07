import requests
import pandas as pd
import json
from datetime import datetime, timedelta

# Define your state code and date range
state_code = "tamil nadu"
start_date = datetime(2024, 5, 1)
end_date = datetime(2024, 6, 30)

# Initialize an empty list to store the data
data_list = []


def get_data(data_str):
    url = f"https://vegetablemarketprice.com/api/dataapi/market/TamilNadu/daywisedata?date={date_str}"

    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": "JSESSIONID=7DCA83AF88D74F763774905CD5EA0D43; _ga=GA1.1.579592366.1719805178; __gads=ID=d417311b4ca58bd6:T=1719805164:RT=1719805164:S=ALNI_MZBDVVGHlSQqR5k0P8vj4Ymc9foyA; __gpi=UID=00000e6d610639a0:T=1719805164:RT=1719805164:S=ALNI_MbOlZIJQSQMot2btmDNHhDbbUpTNw; __eoi=ID=5fb93107935acbae:T=1719805164:RT=1719805164:S=AA-Afjbak2cMxgawT7R_UvUzAL3n; _ga_2RYZG7Y4NC=GS1.1.1719805178.1.1.1719805217.0.0.0; FCNEC=%5B%5B%22AKsRol-OtelDtdCW5TTRX5DbcCTw22YeR7qeIawMoDe0pq8Ub6oK3fFXUeH0X7oqPSXfmcdd2HxA2Y7INCAKWHjyvMmu2YDvGQWNtlmZ702PZ6WqWITxix-3mZbovWDBeVg44JknSd9CzIx7g6NDK3Ks4_CbT5hW0Q%3D%3D%22%5D%5D",
        "Referer": "https://vegetablemarketprice.com/market/TamilNadu/today",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        js_data = response.json()
        for item in js_data.get("data", []):
            data_list.append({
                "date": date_str,
                "state_name": "TamilNadu",
                "vegetable_name": item.get("vegetablename"),
                "wholesale_price": item.get("price"),
                "retail_price": item.get("retailprice"),
                "shoping_mall_price": item.get("shopingmallprice"),
                "unit": item.get("units"),
                "image":"https://vegetablemarketprice.com/"+item.get("table").get("chart_symbol")
            })
# Iterate through the date range and fetch data
while start_date <= end_date:
    date_str = start_date.strftime("%Y-%m-%d")
    start_date += timedelta(days=1)
    get_data(date_str)

# Convert the list of dictionaries to a DataFrame and save it as a CSV file
df = pd.DataFrame(data_list)
df.to_csv("vegetable_market_data.csv", index=False)
print("Data saved to vegetable_market_data.csv")
  
  
