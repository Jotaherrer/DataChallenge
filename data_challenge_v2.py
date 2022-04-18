# %%
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

# %% Datasets
d_rates = pd.read_csv('rates.csv')
d_transactions = pd.read_csv('transactions.csv')
d_user = pd.read_csv('users.csv')

# %%
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

# %% Function that converts date to year month
def get_month(x):
    return dt.datetime(x.year, x.month, 1)

# Create the invoicemonth period column
d_transactions['tran_month'] = d_transactions['createdat'].apply(get_month)

# %% Group by customerID and select only the invoicemonth column
t_grouping = d_transactions.groupby('user_id')['tran_month']

# Take the earliest date of each customer and assign it back to the orignal dataset
d_transactions['CohortMonth'] = t_grouping.transform('min')

# %% This function gets us the integer value of year and month
def get_date_int(df, column):
   year = df[column].dt.year
   month = df[column].dt.month
   return year, month

# Get the integers for the date parts from the 'InvoiceMonth' column
t_year, t_month = get_date_int(d_transactions, 'tran_month')

# Get the integers for date parts from the 'Cohortmonth' column
t_cohort_year, t_cohort_month = get_date_int(d_transactions, 'CohortMonth')

# Calculate difference in years
t_years_diff = t_year - t_cohort_year

# Calculate difference in months
t_months_diff = t_month - t_cohort_month

# Extract the difference in months from all previous values
d_transactions['CohortIndex'] = t_years_diff * 12 + t_months_diff + 1
t_grouping = d_transactions.groupby(['CohortMonth', 'CohortIndex'])

# Count the number of unique values per Customer ID
t_cohort_data = t_grouping['user_id'].apply(pd.Series.nunique).reset_index()

# %% Create a pivot
t_cohort_counts = t_cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='user_id')

# Select the first column and store it to cohort_sizes
t_cohort_sizes = t_cohort_counts.iloc[:,0]

# %% Divide the cohort count by cohort sizes along the rows
t_retention = t_cohort_counts.divide(t_cohort_sizes, axis=0)*100

# Create list of month names for visualisation
t_month_list = t_retention.reset_index()['CohortMonth']

def get_month_name(x):
   return dt.datetime.strftime(x, '%b-%y')

t_month_list = t_month_list.apply(get_month_name)

# %% Initialize inches plot figure
plt.figure(figsize=(15,7))
plt.title('Retention by Monthly Cohorts')
# Create the heatmap
sns.heatmap(data=t_retention,
annot = True,
cmap = "Blues",
vmin = 0.0,
vmax = list(t_retention.max().sort_values(ascending = False))[1]+3,
fmt = '.1f',
linewidth = 0.3,
yticklabels=t_month_list)
plt.show()

#%% Pivot revenue per user
t_grouping = d_transactions.groupby(['CohortMonth', 'CohortIndex'])

# Count the number of unique values per Customer ID
t_cohort_data = t_grouping['revenue'].sum()
t_cohort_data = t_cohort_data.reset_index()

avg_rev = t_cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='revenue')
t_avg_rev = avg_rev.divide(t_cohort_sizes, axis=0)

# %% Create the heatmap
plt.figure(figsize=(15,7))
plt.title('Average Revenue by Monthly Cohorts')
# Create the heatmap
sns.heatmap(data=t_avg_rev,
annot = True,
cmap = "Reds",
vmin = 0.0,
vmax = list(t_avg_rev.max().sort_values(ascending = False))[1]+3,
fmt = '.1f',
linewidth = 0.3,
yticklabels=t_month_list)
plt.show()

# %%
churn = ((t_retention - 100) * -1)/100
churn.round(1)

ltv = t_avg_rev.divide(churn, axis=0)
ltv[1] = t_avg_rev[1]

# %% Create the heatmap
plt.figure(figsize=(15,7))
plt.title('Lifetime Value  by Monthly Cohorts')
# Create the heatmap
sns.heatmap(data=ltv,
annot = True,
cmap = "Greens",
vmin = 0.0,
vmax = list(ltv.max().sort_values(ascending = False))[1]+3,
fmt = '.1f',
linewidth = 0.3,
yticklabels=t_month_list)
plt.show()

# %%
