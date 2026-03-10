# ML Portfolio Allocation

A machine learning-based portfolio optimization system that predicts which assets are likely to perform better and allocates funds accordingly. This approach supports informed investment decisions across multiple asset classes including stocks (Nifty & IPOs) and minerals.

---

## 💡 Idea

- Predict the performance of assets using historical and financial data.  
- Rank assets based on model predictions.  
- Allocate funds to top-ranked assets according to a fixed allocation strategy:  
  - Nifty Stocks → 40%  
  - IPOs → 30%  
  - Minerals → 20%  

---

## 🔄 Pipeline

1. **Data Collection**  
   - Download historical data for Nifty stocks, IPOs, and minerals.  
   - For stocks and IPOs, focus on balance sheet-based features.

2. **Feature Engineering**  
   - Extract financial ratios from balance sheets (e.g., PE ratio, ROE, debt-equity ratio).  
   - Include technical indicators if needed for trends.

3. **ML Model Training**  
   - Train machine learning models such as Random Forest or XGBoost to predict asset performance.  

4. **Asset Ranking**  
   - Rank assets based on predicted returns.  

5. **Portfolio Allocation**  
   - Allocate funds to top assets according to fixed weights:  
     - Top 2 Nifty Stocks → 40%  
     - Top 2 IPOs → 30%  
     - Top 2 Minerals → 20%  

---

## 📈 Example Result

| Asset      | Allocation |
|------------|------------|
| Stock A    | 40%        |
| Stock B    | 30%        |
| Mineral X  | 20%        |
| IPO Y      | 10%        |

> Allocation percentages are based on predicted performance and fixed strategy.

---

## 🛠 Technologies

- **Python** – Data processing and ML  
- **Pandas & NumPy** – Data handling  
- **Scikit-learn** – Random Forest / XGBoost models  
- **yFinance / Custom APIs** – Historical stock & IPO data  

---

## ⚡ How it works

- Focus on **both company stocks and commodities** simultaneously.  
- Extract ratios and metrics from balance sheets to feed into ML models.  
- Rank assets and assign allocations based on predictions.  
- Portfolio allocation is **dynamic based on model output** but follows fixed proportion strategy.

---

## 🚀 Future Improvements

- Include **real-time price updates** for dynamic rebalancing.  
- Add **crypto or ETFs** as alternative asset classes.  
- Backtesting with historical data for **performance evaluation**.  
- Experiment with advanced ML models (LightGBM, Neural Networks) for improved prediction accuracy.

---

## ⚠ Disclaimer

This project is for **educational and research purposes only**.  
It is **not financial advice**. Investing in financial markets carries risk.
