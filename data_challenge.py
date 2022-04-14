import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from pandas.tseries.offsets import Day, MonthEnd
import math

d_rates = pd.read_csv('rates.csv')
d_transactions = pd.read_csv('transactions.csv')
d_user = pd.read_csv('users.csv')

# Data cleaning
d_rates.dtypes
d_user.dtypes
d_transactions.dtypes

d_user['createdat'] = pd.to_datetime(d_user['createdat'])
d_user['birthdate'] = pd.to_datetime(d_user['birthdated'])
d_transactions['createdat'] = pd.to_datetime(d_user['createdat'])

# Exploratory data for Users Dataset
n_users = d_user['gender'].value_counts().values
n_users_rel = [x/len(d_user) for x in n_users]
dist_users = ((n_users[0]/len(d_user), 'Male'), (n_users[1]/len(d_user), 'Female'))
plt.bar(('Male', 'Female'), n_users_rel, color='yellowgreen', edgecolor='b')

# Exploratory data for transactions Dataset
