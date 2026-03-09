import yfinance as yf
import pandas as pd
import numpy as np
from tqdm import tqdm
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

print("🚀 AI STOCK PROJECT STARTED")

tickers = [
"AAPL","MSFT","GOOGL","AMZN","NVDA","META","TSLA","JPM","V","AMD",
"INTC","NFLX","ADBE","CRM","ORCL","IBM","QCOM","TXN","AVGO","MU",
"BA","LMT","NOC","CAT","GE","GS","BLK","C","BAC","WFC"
]

data = []

print("📊 Downloading data...")

for ticker in tqdm(tickers):

    try:

        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="5y")

        if len(hist) < 300:
            continue

        hist["return"] = hist["Close"].pct_change()

        # volatility
        hist["volatility30"] = hist["return"].rolling(30).std()*np.sqrt(252)

        # moving averages
        hist["ma20"] = hist["Close"].rolling(20).mean()
        hist["ma50"] = hist["Close"].rolling(50).mean()
        hist["ma200"] = hist["Close"].rolling(200).mean()

        hist["price_ma50"] = hist["Close"]/hist["ma50"]
        hist["price_ma200"] = hist["Close"]/hist["ma200"]

        # volume signals
        hist["vol_avg20"] = hist["Volume"].rolling(20).mean()
        hist["vol_ratio"] = hist["Volume"]/hist["vol_avg20"]

        # future return (target)
        hist["future_return"] = hist["Close"].shift(-60)/hist["Close"] - 1

        hist = hist.dropna()

        for i,row in hist.iterrows():

            data.append({

                "ticker": ticker,

                # TIME FEATURES
                "year": i.year,
                "month": i.month,
                "day": i.dayofweek,
                "quarter": (i.month-1)//3 + 1,

                # FUNDAMENTALS
                "pe": info.get("trailingPE"),
                "forward_pe": info.get("forwardPE"),
                "price_book": info.get("priceToBook"),
                "roe": info.get("returnOnEquity"),
                "debt_eq": info.get("debtToEquity"),
                "rev_growth": info.get("revenueGrowth"),
                "profit_margin": info.get("profitMargins"),

                # TECHNICAL
                "volatility": row["volatility30"],
                "ma20": row["ma20"],
                "ma50": row["ma50"],
                "ma200": row["ma200"],
                "price_ma50": row["price_ma50"],
                "price_ma200": row["price_ma200"],
                "vol_ratio": row["vol_ratio"],

                # TARGET
                "target": int(row["future_return"] > 0.15)
            })

    except:
        continue


df = pd.DataFrame(data)

df.to_csv("stock_dataset.csv", index=False)
print("Dataset saved as stock_dataset.csv")
print("Dataset size:", len(df))

features = [
"year","month","day","quarter",
"pe","forward_pe","price_book","roe","debt_eq",
"rev_growth","profit_margin",
"volatility","ma20","ma50","ma200",
"price_ma50","price_ma200","vol_ratio"
]

df = df.dropna(subset=features)

X = df[features]
y = df["target"]

print("🤖 Training AI Model...")

split = int(len(df) * 0.75)

X_train = X.iloc[:split]
X_test = X.iloc[split:]

y_train = y.iloc[:split]
y_test = y.iloc[split:]

pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

model = XGBClassifier(
    n_estimators=400,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=pos_weight,
    random_state=42
)

model.fit(X_train,y_train)

pred = model.predict(X_test)

print("\n📊 MODEL RESULTS")

print("Accuracy:",accuracy_score(y_test,pred))
print(classification_report(y_test,pred))

print("\n🏆 AI STOCK RANKING")

latest = df.groupby("ticker").tail(1)

X_latest = latest[features]

latest = latest.copy()
latest.loc[:, "ai_score"] = model.predict_proba(X_latest)[:,1]

top = latest.sort_values("ai_score",ascending=False).head(10)

print(top[["ticker","ai_score"]])

import joblib

joblib.dump(model, "stock_ai_model.pkl")
print("Model saved as stock_ai_model.pkl")