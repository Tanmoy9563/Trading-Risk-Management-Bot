

# 🚀 AI Trading Bot with Risk Management & Arbitrage

## 📖 Overview

This project is a **simulated AI Trading Bot built using Streamlit** that demonstrates:

* Dynamic Risk Management
* EMA-based Trend Strategy
* Simulated Arbitrage Detection
* Capital Preservation Logic
* Equity Curve Visualization
* Interactive Dashboard


---

# 🏗 System Architecture

The bot is built using modular architecture:

```
1. UI Layer (Streamlit)
2. Risk Management Engine
3. Strategy Engine (EMA Crossover)
4. Arbitrage Engine
5. Execution Engine
6. Performance Dashboard
```

Each module is logically separated for scalability and maintainability.

---

# 🛡 Risk Management Engine

This is the core of the system.

## Features:

### ✅ Fixed Percentage Risk Per Trade

Position size is calculated using:

```
Position Size = Risk Amount / Stop Loss Distance
```

Example:

* Capital = $10,000
* Risk per trade = 1%
* Risk amount = $100

The bot adjusts position size dynamically to ensure only 1% is at risk.

---

### ✅ Daily Loss Protection (Auto Shutdown)

If total daily loss exceeds user-defined percentage:

```
Bot automatically stops trading.
```

Example:

* Capital = $10,000
* Max Daily Loss = 3%
* If loss reaches $300 → bot stops execution

This prevents catastrophic drawdowns.

---

# 📈 Strategy Engine – EMA Crossover

The bot uses:

* EMA(9)
* EMA(21)

### Trading Logic:

* If EMA9 > EMA21 → BUY
* If EMA9 < EMA21 → SELL

This is a classical trend-following approach widely used in algorithmic trading.

---

# 🔄 Arbitrage Engine (Simulated)

The bot simulates price differences between two exchanges.

Logic:

```
If price difference > threshold → execute arbitrage trade
```

Arbitrage trades are prioritized before directional trades.

This demonstrates knowledge of:

* Cross-exchange arbitrage
* Spread-based execution
* Low-risk opportunity capture

---

# 🔁 Execution Flow

```
User inputs capital & risk settings
        ↓
Generate simulated market data
        ↓
For 30 iterations:
    Check daily risk limits
    Check arbitrage opportunity
    If available → execute
    Else → apply EMA strategy
    Update capital
        ↓
Display results
```

---

# 📊 Performance Metrics Displayed

* Final Capital
* Total PnL
* Win Rate
* Equity Curve (Cumulative PnL)
* Trade Log

These metrics help evaluate:

* Strategy consistency
* Risk exposure
* Capital growth trajectory

---

# 🧪 Example Run

### Example Input:

* Initial Capital: $10,000
* Risk per Trade: 1%
* Max Daily Loss: 3%

### Possible Output:

| Metric        | Value   |
| ------------- | ------- |
| Final Capital | $10,420 |
| Total PnL     | $420    |
| Win Rate      | 63%     |

Equity curve visually shows cumulative performance.

---

# 💻 How to Run This Application

## Step 1 – Install Python

Python version required:

```
Python 3.9 or higher
Recommended: Python 3.11
```

Check version:

```bash
python --version
```

---

## Step 2 – Install Dependencies

Install required libraries:

```bash
pip install streamlit pandas numpy plotly
```

---

## Step 3 – Run Application

Navigate to project folder and run:

```bash
streamlit run trading_bot_app.py
```


---

# 📦 Dependencies

| Package   | Purpose                  |
| --------- | ------------------------ |
| streamlit | Web UI framework         |
| pandas    | Data manipulation        |
| numpy     | Numerical operations     |
| plotly    | Interactive equity chart |

No external API dependency is required.

---

# 🌍 Cross-System Compatibility

This application runs on:

* Windows
* macOS
* Linux

Since it uses:

* Pure Python
* No system-specific libraries
* No GPU requirement
* No external API dependency

It is fully portable across systems.

---



# 🧠 Key Takeaways

This project demonstrates:

* Understanding of quantitative trading concepts
* Risk management fundamentals
* Algorithmic execution logic
* Modular software architecture
* Data visualization for performance tracking

---




