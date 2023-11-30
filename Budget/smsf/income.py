# Full code for the updated amortization table calculation

import pandas as pd
import openpyxl
import datetime

# Function to create amortization table
def create_amortization_table(initial_investment, annual_withdrawal, inflation_rate, return_rate, years):
    balance = initial_investment
    records = []

    for year in range(1, years + 1):
        # Record the start balance and withdrawal for the year
        start_balance = balance
        withdrawal = annual_withdrawal

        # Calculate the end balance after withdrawal and investment return
        balance -= withdrawal
        balance *= (1 + return_rate)

        # Increase the withdrawal for the next year
        annual_withdrawal *= (1 + inflation_rate)

        # Record the year's details
        records.append({
            "Year": year,
            "Starting Balance": start_balance,
            "Withdrawal": withdrawal,
            "Ending Balance": balance
        })

    return pd.DataFrame(records)

# Parameters for the amortization table
starting_investment = 2_500_000  # Starting investment: $2.5M
year_1_drawdown = 128_000        # Year 1 drawdown: $128,000
annual_inflation = 0.02         # Annual Inflation: 2.0% Which is the annual drawdown increase
annual_investment_income = 0.054 # Annual Investment income: 5.4%
years_duration = 30              # Duration of 30 years

# Creating the amortization table with the parameters
amortization_table = create_amortization_table(
    initial_investment=starting_investment,
    annual_withdrawal=year_1_drawdown,
    inflation_rate=annual_inflation,
    return_rate=annual_investment_income,
    years=years_duration
)

# Displaying the full amortization table
amortization_table_full = amortization_table
amortization_table_full.head(30)  # Displaying all 30 years

# Current timestamp in the format Year-Month-Day_Hour-Minute-Second
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Filename with timestamp
filename = f"amortization_table_{timestamp}.xlsx"

# Outputting the data to an Excel spreadsheet
amortization_table_full.to_excel(filename, index=False)
