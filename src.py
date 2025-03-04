import requests
import pandas as pd
import time
from openpyxl import Workbook

# API URL for CoinCap
API_URL = "https://api.coincap.io/v2/assets"

# Approximate USD to INR conversion rate (can be updated dynamically)
USD_TO_INR = 83.0  # Adjust as needed


def fetch_crypto_data():
    try:
        response = requests.get(API_URL, timeout=10)  # Set timeout
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)
        return response.json()["data"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


def analyze_data(data):
    df = pd.DataFrame(data, columns=["id", "symbol", "priceUsd", "marketCapUsd", "volumeUsd24Hr", "changePercent24Hr"])

    # Convert columns to numeric
    df[["priceUsd", "marketCapUsd", "volumeUsd24Hr", "changePercent24Hr"]] = df[
        ["priceUsd", "marketCapUsd", "volumeUsd24Hr", "changePercent24Hr"]].apply(pd.to_numeric)

    # Convert prices to INR
    df["priceInr"] = df["priceUsd"] * USD_TO_INR

    # Identify top 5 cryptocurrencies by market cap
    top_5 = df.nlargest(5, "marketCapUsd")[["id", "marketCapUsd"]]

    # Calculate average price of top 50 in USD and INR
    avg_price_usd = df["priceUsd"].mean()
    avg_price_inr = avg_price_usd * USD_TO_INR

    # Find highest and lowest 24-hour price change percentage
    highest_change = df.loc[df["changePercent24Hr"].idxmax()]
    lowest_change = df.loc[df["changePercent24Hr"].idxmin()]

    return df, top_5, avg_price_usd, avg_price_inr, highest_change, lowest_change


def save_to_excel(df):
    with pd.ExcelWriter("crypto_data.xlsx", engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Live Crypto Data", index=False)
    print("Data saved to crypto_data.xlsx")


def main():
    while True:
        data = fetch_crypto_data()
        if data:
            df, top_5, avg_price_usd, avg_price_inr, highest_change, lowest_change = analyze_data(data)
            print(f"Top 5 Cryptos by Market Cap:\n{top_5}\n")
            print(f"Average Price: {avg_price_usd:.2f} USD ({avg_price_inr:.2f} INR)")
            print(f"Highest 24h Change: {highest_change['id']} ({highest_change['changePercent24Hr']:.2f}%)")
            print(f"Lowest 24h Change: {lowest_change['id']} ({lowest_change['changePercent24Hr']:.2f}%)")
            save_to_excel(df)
        time.sleep(300)  # Update every 5 minutes


if __name__ == "__main__":
    main()
