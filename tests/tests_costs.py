import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from costs import calculate_transaction_cost

def test_zero_cost():
    assert calculate_transaction_cost(1000, 0.0) == 0.0

def test_basic_cost():
    cost = calculate_transaction_cost(1000, 0.01)
    assert cost == 10.0
