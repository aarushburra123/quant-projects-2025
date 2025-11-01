# quant-projects-2025
# Title: quant-projects-2025

# About: Public portfolio of quant projects: factor backtester, options pricer, microstructure simulator. 

# Topics: quant, quantitative-finance, backtesting, options, yfinance.

## Install:
- python 3.10+
- pip install yfinance pandas numpy matplotlib​
- pip install -r requirements.txt

## Quickstart:
- jupyter notebook notebooks/00_setup.ipynb
- jupyter notebook notebooks/01_spy_plot.ipynb
- jupyter notebook notebooks/02_factor_backtest.ipynb

## Projects
- [notebooks/00_setup.ipynb](notebooks/00_setup.ipynb) — environment setup
- [notebooks/01_spy_plot.ipynb](notebooks/01_spy_plot.ipynb) — SPY monthly returns analysis, Sharpe, [png](results/spy_plot.png)
- [notebooks/02_factor_backtest.ipynb](notebooks/02_factor_backtest.ipynb) — momentum (12–1), top-quintile EW, gross vs net with transaction costs (25 bps), [gross vs net PNG](results/mom_top_quintile_gross_vs_net.png)

## Data Artifacts

- [results/mom_topq_gross_monthly.csv](results/mom_topq_gross_monthly.csv) — gross monthly returns
- [results/mom_topq_net_monthly.csv](results/mom_topq_net_monthly.csv) — net monthly returns after costs
- [results/mom_topq_costs.csv](results/mom_topq_costs.csv) — monthly transaction costs
- [results/mom_topq_weights.csv](results/mom_topq_weights.csv) — portfolio weights at each rebalance

## Methods
- Universe: 10 large-cap US equities
- Factor: 12–1 momentum (past 12-month return excluding most recent month)
- Rebalance: monthly, end-of-month
- Portfolio: long-only, top quintile equal-weight
- Costs: 25 bps per unit turnover
- Data: Yahoo Finance adjusted close, 2018–present

## Features
- **Transaction Cost Modeling**: Basis points calculation with turnover
- **Factor Backtesting**: Momentum strategy with gross/net returns
- **Risk Metrics**: Sharpe ratio, maximum drawdown, CAGR calculation
- **Market Data Pipeline**: yfinance integration with error handling

## Tests
- [tests/tests_weights.py](tests/tests_weights.py) — unit tests for weight constraints (sum to 1, top-quintile selection)
- [tests/test_costs.py](tests/test_costs.py) — unit tests for transaction cost functions

## Testing
- pytest tests/ -v

## Expected Output Files
- `results/spy_plot.png` - SPY price and monthly returns analysis
- `results/mom_top_quintile_gross_vs_net.png` - Momentum factor backtest
- `results/metrics.csv` - Performance metrics (Sharpe, MaxDD, CAGR)

## Repository Structure
- `src/` - Core library (transaction costs, factor logic)
- `notebooks/` - Jupyter analysis notebooks
- `tests/` - Unit tests for src/ modules
- `results/` - Generated plots and performance data


## Roadmap:

- Milestone 1: SPY plot (done today)

- Milestone 2: Factor returns backtest with Sharpe/DD/CAGR

- Milestone 3: Black–Scholes with Greeks and stress tests
