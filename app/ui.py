import streamlit as st

def render_ui():
    st.set_page_config(layout="wide",page_title="Trade_Simulator")
    st.title("GoQuant Trade Simulator")

    col1, col2= st.columns([2,2])

    with col1:
        st.header("Input Parameters")
        exchange = st.selectbox("Exchange", ["OKX"])
        asset = st.selectbox("Spot Asset", ["BTC-USDT-SWAP"])
        order_type = st.selectbox("Order Type", ["Market"])
        quantity = st.number_input("Quantity (USD)", value=100.0)
        volatility = st.slider("Market Volatility", min_value=0.0, max_value=1.0, value=0.3)
        fee_tier = st.selectbox("Fee Tier", ["Tier 1", "Tier 2", "Tier 3"])

    with col2:
        st.header("Simulation Output")
        st.info("Waiting for order book data...")
        st.metric("Expected Slippage", "0.00%")
        st.metric("Expected Fees", "$0.00")
        st.metric("Market Impact", "$0.00")
        st.metric("Net Cost", "$0.00")
        st.metric("Maker/Taker Probability", "50/50")
        st.metric("Internal Latency", "0 ms")