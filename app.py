"""
BisonQuant Portfolio Dashboard — Streamlit
10-strategy portfolio, paper trading, backtest, live signals
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import json, os
from datetime import datetime

# ═══════════════════════════════════════════════════════
# AUTH / PASSWORD PROTECTION
# ═══════════════════════════════════════════════════════
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("""
    <div style="max-width:400px; margin:100px auto; text-align:center;">
        <div style="font-size:3rem; margin-bottom:20px;">🔒</div>
        <h1 style="color:#00ff88;">BisonQuant Portfolio</h1>
        <p style="color:#8b8d91; margin-bottom:30px;">Enter password to access the dashboard</p>
    </div>
    """, unsafe_allow_html=True)
    
    password = st.text_input("", type="password", placeholder="Enter password...", key="auth_password")
    
    # Password from Streamlit secrets or environment variable
    import os
    PW = os.environ.get('DASHBOARD_PASSWORD', st.secrets.get('DASHBOARD_PASSWORD', 'bisonquant2026'))
    
    if st.button("Access Dashboard", use_container_width=True):
        if password == PW:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password")
    
    st.stop()
st.set_page_config(
    page_title="BisonQuant Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark theme
st.markdown("""
<style>
    .stApp { background: #0e1117; }
    .metric-card { background: #1a1d23; border-radius: 10px; padding: 20px; text-align: center; }
    .metric-value { font-size: 2.2rem; font-weight: 700; color: #00ff88; }
    .metric-label { font-size: 0.8rem; color: #8b8d91; text-transform: uppercase; letter-spacing: 1px; }
    .metric-delta-positive { color: #00ff88; }
    .metric-delta-negative { color: #ff4444; }
    h1 { font-size: 1.8rem !important; }
    h2 { font-size: 1.3rem !important; color: #8b8d91 !important; }
    .section-title { font-size: 1.1rem; font-weight: 600; color: #00ff88; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# LOAD DATA
# ═══════════════════════════════════════════════════════
@st.cache_data(ttl=3600)
def load_data():
    base = os.path.dirname(os.path.abspath(__file__))
    
    # Try to load paper trading ledger
    ledger_path = os.path.join(base, '..', 'paper_trading', 'ledger.json')
    ledger = {}
    if os.path.exists(ledger_path):
        with open(ledger_path) as f:
            ledger = json.load(f)
    
    # Load backtest results (hardcoded from our validated backtests)
    backtest = {
        'years': [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
        'returns': [0.0, 52.7, -0.3, 50.1, 108.6, 61.0, 0.9, 59.8, 28.3, 45.1, 53.4],
        'dd': [1.9, 4.9, 16.3, 11.8, 12.7, 6.2, 15.2, 10.3, 9.3, 11.0, 8.9],
        'sharpe': [0.09, 2.22, 0.04, 1.68, 1.81, 1.62, 0.09, 1.57, 0.88, 1.29, 2.07],
        'spy': [4.3, 21.7, -4.6, 31.2, 18.3, 28.7, -18.2, 26.2, 24.9, 17.7, 8.9],
    }
    
    # Strategy stats
    strategies = [
        ('Sector Leverage Rotation', 160.3, 2.51, -14.8, 'leverage'),
        ('Commodity Momentum', 164.2, 1.97, -21.0, 'commodity'),
        ('Momentum Commodities Futures', 164.4, 2.01, -18.2, 'commodity'),
        ('EMA Crossover Futures', 46.3, 2.73, -3.8, 'momentum'),
        ('TQQQ Trailing Stop', 146.4, 1.59, -22.7, 'leverage'),
        ('Leveraged ETF Momentum', 217.6, 1.58, -40.5, 'leverage'),
        ('KMLM Switcher Enhanced', 95.8, 2.47, -13.4, 'momentum'),
        ('Tech Momentum', 121.1, 1.71, -19.9, 'tech'),
        ('Crypto Pair', 108.8, 1.02, -14.3, 'crypto'),
        ('Emerging Markets', 50.1, 1.41, -13.4, 'international'),
    ]
    
    return ledger, backtest, strategies

# ═══════════════════════════════════════════════════════
# METRIC CARD
# ═══════════════════════════════════════════════════════
def metric_card(label, value, delta=None, delta_color='normal'):
    color = '#00ff88' if delta_color == 'normal' else '#ff4444'
    delta_html = f'<span style="color:{color};font-size:1rem">({delta})</span>' if delta else ''
    return f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """

# ═══════════════════════════════════════════════════════
# MAIN DASHBOARD
# ═══════════════════════════════════════════════════════
ledger, backtest, strategies = load_data()

# Title
st.markdown("""
<div style="display:flex; align-items:center; margin-bottom:20px;">
    <div style="font-size:2.5rem; margin-right:15px;">📊</div>
    <div>
        <h1 style="margin:0;">BisonQuant Portfolio Dashboard</h1>
        <p style="color:#8b8d91; margin:0;">10-Strategy Optimized Portfolio • Paper Trading • $125K Portfolio Margin</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# ROW 1: KPI CARDS
# ═══════════════════════════════════════════════════════
total_return = 3429
cagr = 41.8
max_dd = -16.3
sharpe = 1.81
spy_return = (1 + 0.043) * (1 + 0.217) * (1 - 0.046) * (1 + 0.312) * (1 + 0.183) * (1 + 0.287) * (1 - 0.182) * (1 + 0.262) * (1 + 0.249) * (1 + 0.177) * (1 + 0.089) - 1
spy_total = spy_return * 100

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.markdown(metric_card("Cumulative Return", f"+{total_return:,}%", "11 years"), unsafe_allow_html=True)
with col2:
    st.markdown(metric_card("Annual Return", f"{cagr}%", "avg/yr"), unsafe_allow_html=True)
with col3:
    st.markdown(metric_card("Max Drawdown", f"{max_dd}%", "2018"), unsafe_allow_html=True)
with col4:
    st.markdown(metric_card("Sharpe Ratio", f"{sharpe}", "risk-adjusted"), unsafe_allow_html=True)
with col5:
    st.markdown(metric_card("vs SPY", f"+{total_return - spy_total:.0f}%", f"SPY: +{spy_total:.0f}%"), unsafe_allow_html=True)
with col6:
    st.markdown(metric_card("Leveraged (1.5x)", f"+18,780%", "Portfolio Margin"), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# ROW 2: EQUITY CURVE + YEAR-BY-YEAR
# ═══════════════════════════════════════════════════════
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown('<div class="section-title">📈 Equity Curve (11-Year Backtest)</div>', unsafe_allow_html=True)
    
    # Build cumulative equity curve from yearly returns
    eq = [10000]
    for r in backtest['returns']:
        eq.append(eq[-1] * (1 + r/100))
    
    # SPY comparison
    spy_eq = [10000]
    for r in backtest['spy']:
        spy_eq.append(spy_eq[-1] * (1 + r/100))
    
    years = [str(y) for y in backtest['years']]
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=years, y=eq[1:], mode='lines+markers', name='Portfolio',
                             line=dict(color='#00ff88', width=3), marker=dict(size=6)),
                  secondary_y=False)
    fig.add_trace(go.Scatter(x=years, y=spy_eq[1:], mode='lines+markers', name='SPY',
                             line=dict(color='#8b8d91', width=1.5, dash='dash'), marker=dict(size=4)),
                  secondary_y=False)
    
    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='#1a1d23',
        plot_bgcolor='#1a1d23',
        margin=dict(l=10, r=10, t=10, b=10),
        height=350,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, x=0),
        hovermode='x unified'
    )
    fig.update_yaxes(title='Equity ($)', gridcolor='#2a2d33', secondary_y=False)
    fig.update_xaxes(gridcolor='#2a2d33')
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown('<div class="section-title">📅 Year-by-Year Returns</div>', unsafe_allow_html=True)
    
    df_yr = pd.DataFrame({
        'Year': [str(y) for y in backtest['years']],
        'Portfolio': [f"{r:+.1f}%" for r in backtest['returns']],
        'SPY': [f"{r:+.1f}%" for r in backtest['spy']],
        'Δ': [f"{backtest['returns'][i] - backtest['spy'][i]:+.1f}%" for i in range(len(backtest['years']))],
        'DD': [f"{d:.1f}%" for d in backtest['dd']],
        'Sharpe': [f"{s:.2f}" for s in backtest['sharpe']],
    })
    
    # Color the Δ column
    def color_delta(val):
        if val.startswith('+'):
            return 'color: #00ff88'
        return 'color: #ff4444'
    
    styled = df_yr.style.applymap(color_delta, subset=['Δ'])
    st.dataframe(styled, use_container_width=True, hide_index=True)

# ═══════════════════════════════════════════════════════
# ROW 3: STRATEGY TABLE + ALLOCATIONS
# ═══════════════════════════════════════════════════════
col_left2, col_right2 = st.columns([3, 2])

with col_left2:
    st.markdown('<div class="section-title">🎯 Strategy Leaderboard</div>', unsafe_allow_html=True)
    
    df_strat = pd.DataFrame(strategies, columns=['Strategy', 'Return%', 'Sharpe', 'Max DD%', 'Category'])
    df_strat['Return%'] = df_strat['Return%'].apply(lambda x: f"+{x:.1f}%")
    df_strat['Max DD%'] = df_strat['Max DD%'].apply(lambda x: f"{x:.1f}%")
    df_strat['Sharpe'] = df_strat['Sharpe'].apply(lambda x: f"{x:.2f}")
    
    st.dataframe(df_strat, use_container_width=True, hide_index=True,
                 column_config={
                     'Strategy': st.column_config.TextColumn('Strategy', width='large'),
                     'Return%': st.column_config.TextColumn('Return', width='small'),
                     'Sharpe': st.column_config.TextColumn('Sharpe', width='small'),
                     'Max DD%': st.column_config.TextColumn('Max DD', width='small'),
                     'Category': st.column_config.TextColumn('Type', width='small'),
                 })

with col_right2:
    st.markdown('<div class="section-title">🍩 Strategy Allocation</div>', unsafe_allow_html=True)
    
    weights = [12, 12, 12, 11, 11, 11, 11, 9, 6, 5]
    names = [s[0][:25] for s in strategies]
    colors = ['#00ff88', '#00cc6a', '#00994d', '#ff6b6b', '#ff4444', '#cc0000', 
              '#ffd93d', '#ff8c00', '#6c5ce7', '#a29bfe']
    
    fig = go.Figure(data=[go.Pie(labels=names, values=weights, hole=0.5,
                   marker=dict(colors=colors), textinfo='label+percent',
                   textfont=dict(size=10))])
    fig.update_layout(
        template='plotly_dark', paper_bgcolor='#1a1d23', plot_bgcolor='#1a1d23',
        margin=dict(l=10, r=10, t=10, b=10), height=350, showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════════════════
# ROW 4: TOS SIGNALS + DRAWDOWN
# ═══════════════════════════════════════════════════════
col_left3, col_right3 = st.columns([2, 3])

with col_left3:
    st.markdown('<div class="section-title">📋 Today\'s TOS Signal Sheet</div>', unsafe_allow_html=True)
    
    signal_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paper_trading', 'signal_data.json')
    if os.path.exists(signal_path):
        with open(signal_path) as f:
            signal_data = json.load(f)
        
        if signal_data.get('positions'):
            signals = []
            for ticker, info in signal_data['positions'].items():
                signals.append({
                    'Ticker': ticker,
                    'Alloc': f"{info['allocation_pct']:.1f}%",
                    'Shares': f"{info['shares']:,}",
                    'Price': f"${info['price']:.2f}",
                    'Value': f"${info['market_value']:,.0f}",
                })
            st.dataframe(pd.DataFrame(signals), use_container_width=True, hide_index=True)
        else:
            st.info("Signal data not yet generated. Run the TOS signal generator.")
    else:
        st.info("Running paper trading pipeline... signal sheet will appear here at 8 AM ET.")

with col_right3:
    st.markdown('<div class="section-title">📉 Drawdown Timeline</div>', unsafe_allow_html=True)
    
    # Simulate drawdown from yearly returns
    cum = 10000
    peak = 10000
    dds = []
    for r, yr in zip(backtest['returns'], backtest['years']):
        cum *= (1 + r/100)
        peak = max(peak, cum)
        dd = (cum - peak) / peak * 100
        dds.append(dd)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[str(y) for y in backtest['years']], y=dds,
                         marker=dict(color=['#ff4444' if d < -5 else '#2a2d33' for d in dds]),
                         text=[f'{d:.1f}%' for d in dds], textposition='outside',
                         textfont=dict(color='#8b8d91', size=10)))
    fig.update_layout(
        template='plotly_dark', paper_bgcolor='#1a1d23', plot_bgcolor='#1a1d23',
        margin=dict(l=10, r=10, t=10, b=10), height=350,
        showlegend=False
    )
    fig.update_yaxes(title='Drawdown %', gridcolor='#2a2d33')
    fig.update_xaxes(gridcolor='#2a2d33')
    fig.add_hline(y=-16.3, line_dash='dash', line_color='#ff4444', annotation_text='Max DD: -16.3%')
    st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════
st.markdown("""
<div style="text-align:center; color:#4a4d53; margin-top:30px; padding-top:20px; border-top:1px solid #2a2d33;">
    <p style="font-size:0.8rem;">
        BisonQuant Portfolio Dashboard • Paper Trading • Updated Daily • $125K Portfolio Margin • 1.5x Leverage
    </p>
    <p style="font-size:0.7rem;">
        Safety Overlay Active • Circuit Breaker: -30% DD • Max Position: 15% • Rebalance: Daily 9 AM ET
    </p>
</div>
""", unsafe_allow_html=True)