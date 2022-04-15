# %% Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import datetime as dt
from pandas.tseries.offsets import Day, MonthEnd

# %% Datasets
d_rates = pd.read_csv('rates.csv')
d_transactions = pd.read_csv('transactions.csv')
d_user = pd.read_csv('users.csv')

# %% Data cleaning
d_rates.dtypes
d_user.dtypes
d_transactions.dtypes

d_user['createdat'] = pd.to_datetime(d_user['createdat'])
d_transactions['createdat'] = pd.to_datetime(d_user['createdat'])

d_user['createdat'] = d_user['createdat'].apply(lambda row: np.datetime64(row, 'D'))
d_transactions['createdat'] = d_transactions['createdat'].apply(lambda row: np.datetime64(row, 'D'))

# %% Rates conversion
d_rates.columns = ['currency', 'quote_currency', 'price']
especies = d_rates.currency.unique()
len_rates = len(d_rates)

# Conversion values to USD
quotes = []
btc, eth = float(42670), float(3236.38)

for i, v in d_rates.iterrows():
    if (v.values[0] == 'UST'):
        if v.values[1] == 'USDT':
            val = float(v.values[2])
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'BTC':
            val = float(v.values[2] * btc)
            quotes.append([v.values[0], v.values[1], v.values[2], val])

    elif v.values[0] == 'SAND':
        if v.values[1] == 'BTC':
            val = v.values[2] * btc
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'USDT':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

    elif v.values[0] == 'USDC':
        quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

    elif v.values[0] == 'UNI':
        if v.values[1] == 'BTC':
            val = v.values[2] * btc
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'USDT':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

    elif v.values[0] == 'ADA':
        if v.values[1] == 'ETH':
            val = v.values[2] * eth
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'BTC':
            val = v.values[2] * btc
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'USDT':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])
        elif v.values[1] == 'USDC':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

    elif v.values[0] == 'LUNA':
        if v.values[1] == 'ETH':
            val = v.values[2] * eth
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'BTC':
            val = v.values[2] * btc
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'USDT':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])
        elif v.values[1] == 'UST':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

    elif v.values[0] == 'SOL':
        if v.values[1] == 'ETH':
            val = v.values[2] * eth
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'BTC':
            val = v.values[2] * btc
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'USDT':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])
        elif v.values[1] == 'USDC':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

    elif v.values[0] == 'ETH':
        if v.values[1] == 'USDC':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])
        elif v.values[1] == 'BTC':
            val = v.values[2] * btc
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'USDT':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])
        elif v.values[1] == 'UST':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])
        elif v.values[1] == 'DAI':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

    elif v.values[0] == 'SLP':
        if v.values[1] == 'ETH':
            val = v.values[2] * eth
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'USDT':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

    elif (v.values[0] == 'DOT') or (v.values[0] == 'AXS') or (v.values[0] == 'MANA') or (v.values[0] == 'ALGO'):
        if v.values[1] == 'ETH':
            val = v.values[2] * eth
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'BTC':
            val = v.values[2] * btc
            quotes.append([v.values[0], v.values[1], v.values[2], val])
        elif v.values[1] == 'USDT':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

    elif v.values[0] == 'USDT':
        if v.values[1] == 'DAI':
            quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

    else:
        quotes.append([v.values[0], v.values[1], v.values[2], v.values[2]])

new_rates = pd.DataFrame(quotes, columns=['currency', 'quote_curr', 'base_price', 'usd_price'])

# Convert transaction amounts
t_test = d_transactions[['id', 'user_id', 'amount', 'currency', 'createdat']]
t_rates = new_rates[['currency', 'usd_price']]
new_row = {'currency': 'MONEY', 'usd_price': 1/200}
t_rates.append(new_row, ignore_index=True)

t_test.set_index('currency', inplace=True)
t_rates.set_index('currency', inplace=True)

pd.merge(t_test, t_rates, left_index=True, right_index=True)
pd.concat([t_test, t_rates], axis=1)


# %% Exploratory data for Users Dataset
# User distribution by gender
n_users = d_user['gender'].value_counts().values
n_users_rel = [x/len(d_user) for x in n_users]
dist_users = ((n_users[0]/len(d_user), 'Male'), (n_users[1]/len(d_user), 'Female'))
plt.bar(('Male', 'Female'), n_users_rel, color='yellowgreen', edgecolor='b')

# %% User acquisition temporality
u_per_day = d_user.groupby("createdat")['gender'].count().reset_index()
u_stats = u_per_day.describe()
fig = plt.figure(figsize=(10,8))
plt.bar(u_per_day['createdat'], u_per_day['gender'])
plt.ylim(0,700)


# %% Exploratory data for transactions Dataset
t_per_month = d_transactions.groupby("createdat")['amount'].sum().reset_index()
t_stats = t_per_month.describe()

# Operated volume per date
fig = plt.figure(figsize=(10,8))
plt.bar(t_per_month['createdat'], t_per_month['amount'])

# %% Transacted volume 25D moving average
t_per_month.rolling(25, min_periods=10).mean().plot()

# Stationality in volume?


# %% LTV / Churning
u_grouped = d_transactions.groupby(['user_id', 'createdat'])['amount'].mean().reset_index()
u_grouped.columns = ['t_user_id', 't_createdat', 't_amount']
u_grouped.set_index('t_user_id', inplace=True)
d_user.set_index('user_id', inplace=True)
comb = pd.merge(u_grouped, d_user, left_index=True, right_index=True)
comb = comb[['t_amount','t_createdat', 'createdat']]
#comb['day_interval'] = comb['t_createdat'] - comb['createdat']
comb['t_interval'] = comb.apply(lambda row: row, axis=1)

# %%
