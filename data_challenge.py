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

# Mod dates format
t_dates = []
for i, v in d_transactions.iterrows():
    str_date = v.values[7][:10]
    n_date = dt.datetime.strptime(str_date, '%Y-%m-%d')
    t_dates.append(n_date)
d_transactions['createdat'] = t_dates

d_dates = []
for i, v in d_user.iterrows():
    str_date = v.values[3][:10]
    n_date = dt.datetime.strptime(str_date, '%Y-%m-%d')
    d_dates.append(n_date)
d_user['createdat'] = d_dates

# %% Rates conversion
d_rates.columns = ['currency', 'quote_currency', 'price']
especies = d_rates.currency.unique()
len_rates = len(d_rates)
curr_dist = d_transactions.groupby('currency')['id'].count().reset_index()

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
        quotes.append(['ARS', 'ARS', 1/200, 1/200])

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

# %% Convert transaction amounts
d_transactions.currency.replace('MONEY', 'ARS', inplace=True)
d_transactions.currency.replace('DAI', 'USDT', inplace=True)

curr_dist = d_transactions.groupby('currency')['id'].count().reset_index()
curr_dist.sort_values('currency', inplace=True)

t_rates = new_rates[['currency', 'usd_price']]
t_rates.drop_duplicates(subset='currency', inplace=True)
curr_dist_rates = t_rates['currency'].drop_duplicates().reset_index(drop=True)
curr_dist_rates = pd.DataFrame(curr_dist_rates)
curr_dist_rates.sort_values('currency', inplace=True)

d_transactions.set_index('currency', inplace=True)
t_rates.set_index('currency', inplace=True)
d_transactions_dummy = d_transactions

t_comb = pd.merge(d_transactions, t_rates, left_index=True, right_index=True)
t_comb.reset_index(inplace=True)
t_comb['t_value_usd'] = t_comb['amount'] * t_comb['usd_price']
d_transactions = t_comb
d_transactions.sort_values('createdat', inplace=True)

# %% Add revenue from amounts transacted
revenue = []

for i, v in d_transactions.iterrows():
    tran_type = v.values[6]
    status = v.values[4]
    if status == 'DONE':
        if tran_type == 'CRYPTO_SWAP':
            val_com = v.values[9] * 0.01
            revenue.append(val_com)
        elif (tran_type == 'CRYPTO_SALE') or (tran_type == 'CRYPTO_PURCHASE'):
            val_com = v.values[9] * 0.02
            revenue.append(val_com)
        elif (tran_type == 'LEMON_CARD_PAYMENT'):
            val_com = v.values[9] * 0.05
            revenue.append(val_com)
        else:
            val_com = 0
            revenue.append(val_com)
    else:
        val_com = 0
        revenue.append(val_com)

d_transactions['revenue'] = revenue






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
t_per_month = d_transactions.groupby("createdat")['t_value_usd'].sum().reset_index()
t_stats = t_per_month.describe()

# Operated volume per date
fig = plt.figure(figsize=(10,8))
plt.bar(t_per_month['createdat'], t_per_month['t_value_usd'])

# Transacted volume 25D moving average
t_per_month.rolling(25, min_periods=10).mean().plot()





# %% LTV / Churning
u_grouped = d_transactions.groupby(['user_id', 'createdat'])['revenue'].sum().reset_index()
u_grouped.columns = ['t_user_id', 't_createdat', 'revenue']
u_grouped.set_index('t_user_id', inplace=True)

d_user.set_index('user_id', inplace=True)
comb = pd.merge(u_grouped, d_user, left_index=True, right_index=True)
comb = comb[['revenue','t_createdat', 'createdat']]
comb.reset_index(inplace=True)
comb.sort_values(['index', 't_createdat'], inplace=True)

maturity = []
for i, v in comb.iterrows():
    intervalo = int((v.values[2] - v.values[3]).components.days)
    maturity.append(intervalo)

comb['maturity'] = [round(x/30, 0) for x in maturity]
comb_n = comb.groupby(comb['t_createdat'].dt.to_period("M"))['revenue', 'index'].count().reset_index()
piv_table = comb.pivot_table(index='t_createdat', columns='index', values='revenue', fill_value=0).sort_index(ascending=True)
total_rev, total_users = sum(comb['revenue'])

piv_dates = []
piv_rev_per_day = []
active_users_per_day = []
for i, v in piv_table.iterrows():
    rev_per_day = sum(v.values)
    piv_rev_per_day.append(rev_per_day)
    piv_dates.append(i)
    act_users = np.count_nonzero(v.values)
    active_users_per_day.append(act_users)

df_dates, df_rev, df_users = pd.DataFrame(piv_dates), pd.DataFrame(piv_rev_per_day), pd.DataFrame(active_users_per_day)
comb_per_day = pd.concat([df_dates, df_rev, df_users], axis=1)
comb_per_day.columns = ['date', 'rev', 'users']
comb_per_day_grouped = comb_per_day.groupby(comb_per_day['date'].dt.to_period('M'))['rev', 'users'].sum()
comb_per_day_grouped['ARPU'] = comb_per_day_grouped['rev']/comb_per_day_grouped['users']

# %% Stats per user
rank_users = comb.groupby('index')['t_createdat'].count().reset_index()
rank_users = rank_users.sort_values('t_createdat', ascending=False)

rank_test = comb[comb['index'] == rank_users['index'].values[0]]
rank_test_month = rank_test.groupby(rank_test['t_createdat'].dt.to_period("M"))['index'].count()
rango = pd.date_range(start='2019-11-01', end='2022-05-01', freq='M')

#%% Groups per subscription date
subs_groups = comb.groupby(comb['createdat'].dt.to_period("M"))['index'].count()
subs_groups = pd.DataFrame(subs_groups)
#plt.bar(subs_groups.index.values, subs_groups['index'].values)
