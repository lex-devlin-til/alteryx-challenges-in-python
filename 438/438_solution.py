# Solution to Alteryx Challenge 438 in python

# Importing libraries and data
import pandas as pd
import numpy as np

df = pd.read_csv('438/currency_data.csv')

# Challenge Prompt
"""
A client requested assistance with retrieving the history of a customer’s end-of-day currency balances from a given dataset. The goal is to display these daily balances in an output table, with the oldest balances on the left and the most recent on the right.

Your challenge is to find a solution that ensures the daily balances are always displayed in the correct chronological order, from the oldest (left) to the most recent (right).
"""
# Sort by Order column
df = df.sort_values(by=['Order'])

df_melted = df.melt(
    id_vars = ['Subgroup Name', 'Order', 'Currency'],
    var_name = 'day',
    value_name = 'currency_balance'
)

df_sorted = df_melted.sort_values(by=['day', 'Order'])

df_pivoted = df_sorted.pivot(
    index = ['Subgroup Name', 'Order', 'Currency'],
    columns = 'day',
    values = 'currency_balance'
)

print(df_pivoted)