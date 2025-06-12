BITCOIN LINEAR FACTOR PRICING MODEL

Factors:

- Exchange Holdings (BTC)
Total amount of Bitcoin held in wallets associated with a centralized exchange
High exchange holdings may indicate more BTC available for selling (bearish market), while low exchange holdings indicates the opposite

- Miner Holdings / Reserves (BTC)
Total BTC held by miners
Decreases in miner holdings indicates a bearish market, while accumulation of miner holdings indicates a bullish market

- Puell Multiple
Puell Multiple = (Daily BTC issued in USD) / (365-day moving average of BTC issued in USD)
High Puell multiple suggests possible overvaluation of BTC, while low Puell multiple represents undervaluation


Response variable:

- Percent return (USD change): (P_t - P_(t-1)) / P_(t-1)
- Log return (USD change): log(P_t / P_(t-1))


Regression equation: R_(t+1) = alpha + B_1 * F_1,t + B_2 * F_2,t + B_3 * F_3,t + epsilon_t

