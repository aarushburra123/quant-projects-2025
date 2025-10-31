# quant-projects-2025
Title: quant-projects-2025

About: Public portfolio of quant projects: factor backtester, options pricer, microstructure simulator. 

# Topics: quant, quantitative-finance, backtesting, options, yfinance.

## Install:

python 3.10+

pip install yfinance pandas numpy matplotlib​

## Quickstart:

jupyter notebook notebooks/00_setup.ipynb

Runs and writes results/spy_close.png

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

## Tests

- [tests/tests_weights.py](tests/tests_weights.py) — unit tests for weight constraints (sum to 1, top-quintile selection)


## Repo structure:

src/ — library code

notebooks/ — analysis

tests/ — unit tests (pytest-ready)

data/ — ignored datasets

results/ — generated plots/files​

## Roadmap:

Milestone 1: SPY plot (done today)

Milestone 2: Factor returns backtest with Sharpe/DD/CAGR

Milestone 3: Black–Scholes with Greeks and stress tests
