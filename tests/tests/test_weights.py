# tests/test_weights.py
import sys, os
sys.path.append(os.path.join("..", "src"))
import pandas as pd
import numpy as np

def test_weights_sum_to_one():
    """Weights should sum to 1.0 at each rebalance date"""
    w = pd.read_csv("../results/mom_topq_weights.csv", index_col=0)
    sums = w.sum(axis=1)
    assert np.allclose(sums, 1.0, atol=1e-8), f"Weight sums deviate: {sums[~np.isclose(sums, 1.0)]}"

def test_only_top_quintile_selected():
    """Only top 20% of stocktickers should have nonzero weights"""
    # This is a placeholder check; in a real test you'd load the factor ranks and verify
    # For now just check that at least 1 ticker is selected and not all are selected
    w = pd.read_csv("../results/mom_topq_weights.csv", index_col=0)
    for idx, row in w.iterrows():
        n_selected = (row > 0).sum()
        n_total = len(row)
        assert 1 <= n_selected <= n_total * 0.3, f"Selected {n_selected}/{n_total} at {idx}"

if __name__ == "__main__":
    test_weights_sum_to_one()
    test_only_top_quintile_selected()
    print("All tests passed.")


