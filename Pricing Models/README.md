# Bitcoin Trend Prediction using Machine Learning

**On-Chain factors (pulled from CryptoQuant):**
- Exchange Reserve
- Miner Reserve
- Puell Multiple
- Hashrate
- Fee-Reward Ratio
- SOPR
- Active Addresses
- Exchange Netflow
- Funding Rates
- Mean Coin Age
- MVRV Ratio
- Open Interest

**Market factors (pulled from Bloomberg / yfinance API):**
- S&P 500
- Nasdaq
- Dow Jones
- Gold
- Silver
- Copper
- Oil
- Natural Gas
- Dollar close
- EUR:USD
- USD:CNY

**Economic factors (pulled from Bloomberg / linear interpolation):**
- CPI
- Fed Funds Rate
- 10Y Treasury Yield
- GDP (real)
- M2 Money Supply
- Unemployment Rate

**Response variable:**
- *Price direction (classification ML)*

**Decided against:**
- Percent return (USD change): (P_t - P_(t-1)) / P_(t-1)
- Log return (USD change): log(P_t / P_(t-1))

========================================================================

## Feature Engineering
- Correlation matrices
- Boruta

## Model Selection
- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)

- Multilayer Perceptron (MLP)
- Long Short Term Memory Recurrent Neural Network (LSTM)

## Output
- Predicting Bitcoin price direction / movement
