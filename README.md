# Investment Strategy Backtesting

This repository contains a Python script to backtest a custom investment strategy and compare it with a simple daily investment strategy in the S&P 500.

## Purpose

The purpose of this project is to simulate and compare the performance of two different investment strategies over a 10-year period using historical data of the S&P 500:
1. **Custom Strategy:** This strategy invests $10 daily if the market goes up or drops by less than 0.5%. If the market drops by 0.5% or more, it invests $20.
2. **Simple Strategy:** This strategy consistently invests $10 daily regardless of market conditions.

By backtesting these strategies, we aim to analyze their performance, total returns, and growth over time to determine which strategy yields better results.


## Data Source

The historical data for the S&P 500 index is obtained using the `yfinance` library.

## How to Use

### Requirements

Ensure you have the following Python libraries installed:

```bash
pip install pandas yfinance matplotlib
```

### Running the Script

Run the `backtest.py` script to execute the backtest.

### Results

The script will output a plot comparing the portfolio values of both strategies over time. Below is a placeholder for the graph generated by the script:

![Graph of Portfolio Values](/graph.png)

## Current Issues and Errors

### Issue 1: Discrepancy in Total Investment
- The total investment for the custom strategy is higher than expected, which might be due to the logic of investing $10 or $20 daily based on market conditions.
- **Action Needed:** Verify and ensure the logic accurately tracks the total amount invested based on market conditions.

### Issue 2: Negative Total Returns with High Positive CAGR
- The total returns for both strategies are negative, but the CAGR shows high positive values. This indicates an inconsistency in the return calculations.
- **Action Needed:** Reevaluate the return and CAGR calculations to ensure they are based on accurate initial and final portfolio values and the correct investment period.

### Issue 3: Realistic Initial Balance
- Ensure that the initial balance and daily investments are set to realistic values to reflect a typical investment scenario.
- **Action Needed:** Set a realistic initial balance and confirm that daily investment logic aligns with the strategy.

## Ideas:
- [ ] Include Fees (Currently Assuming Wealthsimple)
- [ ] Compare Against other intervals of investment with same amount (instead of $10 daily consider $50 every monday)
- [ ] Verify that there isnt any weekend trading

## Contribution

Feel free to fork this repository and submit pull requests for improvements or bug fixes. For significant changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
