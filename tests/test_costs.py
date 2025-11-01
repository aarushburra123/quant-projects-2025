import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import pandas as pd

from costs import compute_turnover, apply_costs

def test_zero_turnover():
    # Test identical weights produce zero turnover
    w_now = pd.DataFrame({'A': [0.5], 'B': [0.5]})
    w_prev = pd.DataFrame({'A': [0.5], 'B': [0.5]})
    turnover = compute_turnover(w_now, w_prev)
    assert turnover.iloc[0] == 0.0

def test_full_turnover():
    # Test complete portfolio flip produces 100% turnover
    w_now = pd.DataFrame({'A': [1.0], 'B': [0.0]})
    w_prev = pd.DataFrame({'A': [0.0], 'B': [1.0]})
    turnover = compute_turnover(w_now, w_prev)
    assert turnover.iloc[0] == 1.0

def test_zero_costs():
    # Test zero basis points produces zero costs
    gross_returns = pd.Series([0.1, 0.05, -0.02])
    w = pd.DataFrame(index=gross_returns.index)
    _, _, net = apply_costs(gross_returns, w, bps_per_turn=0.0)
    pd.testing.assert_series_equal(gross_returns, net)
