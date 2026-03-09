
# AI-Stock-Predictor

AI-Stock-Predictor is a machine learning project that analyzes financial data and predicts potential stock outperformers using fundamental indicators, technical signals, and time-series features.

The system automatically downloads market data, engineers features, trains a machine learning model, and ranks stocks based on predicted future performance.

---

# Project Overview

This project builds an end-to-end AI pipeline for stock analysis:

1. Download historical stock data
2. Generate financial and technical indicators
3. Build a large dataset for training
4. Train a machine learning model
5. Evaluate prediction performance
6. Rank stocks based on AI prediction score

The goal is to identify stocks that may outperform in the near future.

---

# Features Used

## Fundamental Features

* PE Ratio
* Forward PE
* Price to Book
* Return on Equity (ROE)
* Debt to Equity
* Revenue Growth
* Profit Margin

## Technical Features

* 20 Day Moving Average
* 50 Day Moving Average
* 200 Day Moving Average
* Price / Moving Average Ratios
* Volatility
* Volume Ratio

## Time Features

* Year
* Month
* Day of Week
* Quarter

These features help the model learn both **company fundamentals** and **market behavior**.

---

# Dataset

* Data Source: Yahoo Finance
* Library Used: yfinance
* Historical Period: 5 Years
* Stocks Used: 30 major US companies
* Dataset Size: ~30,000 samples

---

# Machine Learning Model

The project uses **XGBoost**, a powerful gradient boosting algorithm for structured data.

Key characteristics:

* Handles non-linear relationships well
* Works effectively on financial datasets
* Provides strong performance on tabular data

---

# Model Results

Example output:

Accuracy ≈ 75%

Classification Summary:

Class 0 → Normal stock performance
Class 1 → Potential high-return stocks

The model focuses on **ranking stocks by probability of future outperformance**.

---

# Example Output

🚀 AI STOCK PROJECT STARTED
📊 Downloading data...
100%|██████████████████████████████████████| 30/30 [00:20<00:00,  1.46it/s]
Dataset saved as stock_dataset.csv
Dataset size: 29910
🤖 Training AI Model...

📊 MODEL RESULTS
Accuracy: 0.7557766367137355
              precision    recall  f1-score   support

           0       0.76      0.98      0.85      4563
           1       0.74      0.13      0.23      1669

    accuracy                           0.76      6232
   macro avg       0.75      0.56      0.54      6232
weighted avg       0.75      0.76      0.69      6232


🏆 AI STOCK RANKING
      ticker  ai_score
19939     MU  0.972788
17945    TXN  0.136641
11963   NFLX  0.111263
13957    CRM  0.046349
14954   ORCL  0.022761
20936     BA  0.022534
2990   GOOGL  0.015089
15951    IBM  0.012887
9969     AMD  0.011505
24924     GE  0.010569
Model saved as stock_ai_model.pkl


```

These represent stocks the model predicts may have stronger future performance.

---

# Installation

Clone the repository:

```
git clone https://github.com/umamanipraharshitha/ai-stock-predictor.git
cd ai-stock-predictor
```

Install dependencies:

```
pip install yfinance pandas numpy scikit-learn xgboost tqdm
```

Run the project:

```
python e.py
```

---

# Project Structure

```
AI-Stock-Predictor
│
├── e.py            # Complete AI pipeline
├── README.md       # Project documentation
```

---

# Future Improvements

* Add technical indicators such as RSI and MACD
* Expand dataset to more stocks
* Add backtesting system for trading strategies
* Build a dashboard to visualize predictions

---

# Disclaimer

This project is for **educational and research purposes only**.
It should not be considered financial advice.

