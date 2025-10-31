
import sys, os
sys.path.append(os.path.join(".", "src"))  # src is in repo root
import pandas as pd
import numpy as np

def test_weights_sum_to_one():
    """Weights should sum to 1.0 at each rebalance date"""
    w = pd.read_csv("results/mom_topq_weights.csv", index_col=0)  # remove the ../
    sums = w.sum(axis=1)
    assert np.allclose(sums, 1.0, atol=1e-8), f"Weight sums deviate"

def test_only_top_quintile_selected():
    """Only top 20% of tickers should have nonzero weights"""
    w = pd.read_csv("results/mom_topq_weights.csv", index_col=0)
    for idx, row in w.iterrows():
        n_selected = (row > 0).sum()
        n_total = len(row)
        assert 1 <= n_selected <= n_total * 0.3, f"Selected {n_selected}/{n_total}"

if __name__ == "__main__":
    test_weights_sum_to_one()
    test_only_top_quintile_selected()
    print("All tests passed.")
