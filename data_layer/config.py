"""
CONFIGURATION FILE
Central control for entire alpha model system
"""

import os

# =========================
# PROJECT ROOT PATH
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =========================
# DATA PATHS
# =========================
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# Create directories if not exist
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

# =========================
# MARKET CONFIG
# =========================
MARKET = "NSE"
INDEX = "NIFTY200"

# =========================
# STOCK UNIVERSE (INITIAL)
# =========================
# NOTE: Using sample tickers first
# We will replace with full Nifty 200 list in next step

STOCK_UNIVERSE = [
    "RELIANCE.NS",
    "TCS.NS",
    "HDFCBANK.NS",
    "INFY.NS",
    "ICICIBANK.NS",
    "LT.NS",
    "SBIN.NS",
    "BHARTIARTL.NS",
    "ITC.NS",
    "HINDUNILVR.NS"
]

# =========================
# DATA SETTINGS
# =========================
START_DATE = "2018-01-01"
END_DATE = None  # None = latest available

INTERVAL = "1d"  # daily data

# =========================
# FILE FORMAT SETTINGS
# =========================
FILE_FORMAT = "csv"  # future: parquet

# =========================
# LOGGING / DEBUG
# =========================
DEBUG = True