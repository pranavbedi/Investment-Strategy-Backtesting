import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for S&P 500
data = yf.download('^GSPC', start='2014-01-01', end='2024-01-01')

# Calculate daily returns
data['Daily Return'] = data['Adj Close'].pct_change()

# Initialize variables for your strategy
initial_balance = 1000  # Set an initial balance
cash = initial_balance
shares = 0
portfolio_values = [initial_balance]  # Start with the initial balance
investment_log = []
total_investment_your_strategy = initial_balance

# Initialize variables for simple $10 a day strategy
simple_cash = initial_balance
simple_shares = 0
simple_portfolio_values = [initial_balance]  # Start with the initial balance
total_investment_simple_strategy = initial_balance

# Backtest your strategy
for i in range(1, len(data)):
    if data['Daily Return'].iloc[i] >= -0.005:
        # Market went green or down less than 0.5%
        cash -= 10
        total_investment_your_strategy += 10
        shares += 10 / data['Adj Close'].iloc[i]
        investment_log.append((data.index[i], 'Buy $10', data['Adj Close'].iloc[i], shares, cash))
    else:
        # Market went red
        cash -= 20
        total_investment_your_strategy += 20
        shares += 20 / data['Adj Close'].iloc[i]
        investment_log.append((data.index[i], 'Buy $20', data['Adj Close'].iloc[i], shares, cash))
    
    # Calculate the portfolio value
    portfolio_value = shares * data['Adj Close'].iloc[i] + cash
    portfolio_values.append(portfolio_value)
    
    # Simple $10 a day strategy
    simple_cash -= 10
    total_investment_simple_strategy += 10
    simple_shares += 10 / data['Adj Close'].iloc[i]
    simple_portfolio_value = simple_shares * data['Adj Close'].iloc[i] + simple_cash
    simple_portfolio_values.append(simple_portfolio_value)

# Convert the investment log to DataFrame for analysis
log_df = pd.DataFrame(investment_log, columns=['Date', 'Action', 'Price', 'Shares', 'Cash'])
data['Your Strategy Value'] = portfolio_values
data['Simple Strategy Value'] = simple_portfolio_values

# Plot the portfolio values over time
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Your Strategy Value'], label='Your Strategy Value', color='blue')
plt.plot(data.index, data['Simple Strategy Value'], label='Simple $10/day Strategy', color='green')
plt.title('Portfolio Value: Your Strategy vs. Simple $10/day Strategy')
plt.xlabel('Date')
plt.ylabel('Value ($)')
plt.legend()
plt.grid(True)
plt.show()

# Performance metrics
final_balance = portfolio_values[-1]
simple_final_balance = simple_portfolio_values[-1]
initial_sp500 = data['Adj Close'].iloc[0]
final_sp500 = data['Adj Close'].iloc[-1]
sp500_return = (final_sp500 - initial_sp500) / initial_sp500 * 100
portfolio_return = (final_balance - total_investment_your_strategy) / total_investment_your_strategy * 100
simple_strategy_return = (simple_final_balance - total_investment_simple_strategy) / total_investment_simple_strategy * 100
investment_years = (data.index[-1] - data.index[0]).days / 365.25  # Total investment period in years
cagr_portfolio = ((final_balance / initial_balance) ** (1 / investment_years) - 1) * 100
cagr_simple_strategy = ((simple_final_balance / initial_balance) ** (1 / investment_years) - 1) * 100
cagr_sp500 = ((final_sp500 / initial_sp500) ** (1 / investment_years) - 1) * 100

print(f'Total Investment (Your Strategy): ${total_investment_your_strategy:.2f}')
print(f'Total Investment (Simple Strategy): ${total_investment_simple_strategy:.2f}')
print(f'Final Portfolio Value (Your Strategy): ${final_balance:.2f}')
print(f'Final Portfolio Value (Simple Strategy): ${simple_final_balance:.2f}')
print(f'Portfolio Total Returns (Your Strategy): {portfolio_return:.2f}%')
print(f'Simple Strategy Total Returns: {simple_strategy_return:.2f}%')
print(f'S&P 500 Total Returns: {sp500_return:.2f}%')
print(f'Portfolio CAGR (Your Strategy): {cagr_portfolio:.2f}%')
print(f'Simple Strategy CAGR: {cagr_simple_strategy:.2f}%')
print(f'S&P 500 CAGR: {cagr_sp500:.2f}%')

# Optional: Display the log dataframe for a glimpse of the transactions
print(log_df.head())
