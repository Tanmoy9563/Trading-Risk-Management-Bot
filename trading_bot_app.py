# =====================================================
# AI Trading Bot with Risk Management + Arbitrage
# FINAL STABLE VERSION (No External Dependencies)
# =====================================================

import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.graph_objects as go

st.set_page_config(page_title="AI Trading Bot", layout="wide")

st.title("🚀 AI Trading Bot with Risk Control & Arbitrage")

# =====================================================
# CONFIGURATION
# =====================================================

capital = st.sidebar.number_input("Initial Capital ($)", value=10000.0)
risk_per_trade = st.sidebar.slider("Risk per Trade (%)", 0.5, 5.0, 1.0)
max_daily_loss_pct = st.sidebar.slider("Max Daily Loss (%)", 1.0, 10.0, 3.0)
run_bot = st.sidebar.button("Start Bot")

# =====================================================
# RISK MANAGEMENT ENGINE
# =====================================================

class RiskManager:
    def __init__(self, capital, risk_pct, max_daily_loss_pct):
        self.initial_capital = capital
        self.capital = capital
        self.risk_pct = risk_pct / 100
        self.max_daily_loss = capital * (max_daily_loss_pct / 100)
        self.daily_loss = 0

    def can_trade(self):
        return self.daily_loss < self.max_daily_loss

    def calculate_position_size(self, entry, stop_loss):
        risk_amount = self.capital * self.risk_pct
        stop_distance = abs(entry - stop_loss)

        if stop_distance == 0:
            return 0

        return risk_amount / stop_distance

    def update_pnl(self, pnl):
        self.capital += pnl
        if pnl < 0:
            self.daily_loss += abs(pnl)

# =====================================================
# STRATEGY ENGINE (EMA Crossover)
# =====================================================

def generate_market_data():
    dates = pd.date_range(end=pd.Timestamp.today(), periods=120)
    prices = np.cumsum(np.random.randn(120)) + 30000

    df = pd.DataFrame({
        "Close": prices
    }, index=dates)

    return df

def strategy_signal(df):
    df["EMA9"] = df["Close"].ewm(span=9).mean()
    df["EMA21"] = df["Close"].ewm(span=21).mean()

    if df["EMA9"].iloc[-1] > df["EMA21"].iloc[-1]:
        return "BUY"
    elif df["EMA9"].iloc[-1] < df["EMA21"].iloc[-1]:
        return "SELL"
    else:
        return None

# =====================================================
# ARBITRAGE ENGINE (Simulated)
# =====================================================

def check_arbitrage():
    price_exchange_1 = np.random.uniform(30000, 31000)
    price_exchange_2 = np.random.uniform(30000, 31000)

    spread = price_exchange_2 - price_exchange_1

    if abs(spread) > 50:
        return True, spread
    else:
        return False, spread

# =====================================================
# MAIN BOT LOGIC
# =====================================================

if run_bot:

    st.subheader("📊 Bot Running...")

    df = generate_market_data()

    risk = RiskManager(capital, risk_per_trade, max_daily_loss_pct)
    trade_log = []

    for i in range(30):

        if not risk.can_trade():
            st.error("⚠️ Max Daily Loss Reached. Bot Stopped Automatically.")
            break

        signal = strategy_signal(df)

        # Arbitrage Check
        arb, spread = check_arbitrage()

        if arb:
            profit = abs(spread) * 0.01
            risk.update_pnl(profit)
            trade_log.append(["Arbitrage", profit])
            continue

        # Directional Trade
        if signal == "BUY":
            entry = df["Close"].iloc[-1]
            stop_loss = entry * 0.98
            size = risk.calculate_position_size(entry, stop_loss)

            new_price = entry * np.random.uniform(0.97, 1.03)
            pnl = (new_price - entry) * size

            risk.update_pnl(pnl)
            trade_log.append(["Directional Trade", pnl])

        time.sleep(0.05)

    # =====================================================
    # RESULTS
    # =====================================================

    st.success("✅ Bot Execution Completed")

    result_df = pd.DataFrame(trade_log, columns=["Type", "PnL"])

    if len(result_df) > 0:

        total_pnl = result_df["PnL"].sum()
        win_rate = (len(result_df[result_df["PnL"] > 0]) / len(result_df)) * 100

        col1, col2, col3 = st.columns(3)

        col1.metric("Final Capital", f"${round(risk.capital,2)}")
        col2.metric("Total PnL", f"${round(total_pnl,2)}")
        col3.metric("Win Rate (%)", f"{round(win_rate,2)}")

        result_df["Cumulative"] = result_df["PnL"].cumsum()

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            y=result_df["Cumulative"],
            mode="lines",
            name="Equity Curve"
        ))

        fig.update_layout(title="Equity Curve", template="plotly_dark")

        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(result_df)

    else:
        st.warning("No trades executed.")

