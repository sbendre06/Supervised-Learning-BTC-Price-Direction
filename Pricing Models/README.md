BITCOIN PRICING MODELS

Factors (pulled from CryptoQuant): 
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


Response variable:
- Percent return (USD change): (P_t - P_(t-1)) / P_(t-1)
- Log return (USD change): log(P_t / P_(t-1))


Regression attempts:
1. Linear Regression: R_(t+1) = alpha + B_1 * F_1,t + B_2 * F_2,t + B_3 * F_3,t + epsilon_t
2. Ridge Regression (supposed to address multicollinearity)
3. Correlation Matrix for visualization
4. Random Forest regression for factor importance

