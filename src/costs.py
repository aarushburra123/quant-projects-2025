
import pandas as pd

def compute_turnover(w_now: pd.DataFrame, w_prev: pd.DataFrame) -> pd.Series:
    """
    Turnover at each rebalance date for long-only equal-weight style:
    0.5 * sum(|w_t - w_{t-1}|) across tickers.
    """
    w_now = w_now.fillna(0.0)
    w_prev = w_prev.fillna(0.0)
    return 0.5 * (w_now.sub(w_prev).abs().sum(axis=1))

def apply_costs(gross_returns: pd.Series, w: pd.DataFrame, bps_per_turn: float):
    """
    Given the gross monthly returns and monthly weights w (shown by rebalance dates),
    find turnover, costs = turnover * bps_per_turn, and net returns = gross - costs.
    bps_per_turn is a decimal (e.g. 0.0025 for 25 bps).
    Returns (gross_aligned, costs_aligned, net_returns) with matching indices.
    """
    w = w.reindex(gross_returns.index).fillna(0.0)
    w_prev = w.shift(1).fillna(0.0)
    turnover = compute_turnover(w, w_prev)
    costs = turnover * bps_per_turn
    net = (gross_returns - costs).dropna()
    return gross_returns.reindex(net.index), costs.reindex(net.index), net


