# Live Crypto Tracker 

This project fetches live cryptocurrency data using a public API and updates an Excel sheet in real-time. The data includes cryptocurrency names, symbols, prices, market cap, trading volume, and price changes.

## Features  
✅ Fetches top 50 cryptocurrencies by market capitalization  
✅ Displays live data including price, market cap, and 24h trading volume  
✅ Performs basic analysis (top 5 by market cap, average price, highest/lowest 24h price change)  
✅ Auto-updates in Excel every 5 minutes  

## 📂 Project Structure  
📁 Live-Crypto-Tracker
├── 📄 crypto_tracker.py # Python script to fetch live data
├── 📄 live_crypto.xlsx # Excel sheet with live updates
├── 📄 analysis_report.pdf # Summary of insights
├── 📄 README.md # Project documentation


## 🛠️ Setup Instructions  
1️⃣ **Clone the Repository**  
   ```bash
   git clone https://github.com/Rohit-0112/Live-Crypto-Tracker.git
   cd Live-Crypto-Tracker
pip install requests pandas openpyxl
python crypto_tracker.py

