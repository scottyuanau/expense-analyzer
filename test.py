import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import math
from findexpensecategory import findExpenseCategory
from dateutil import relativedelta
from datetime import datetime

#  input file setup
original_df = pd.read_csv('input.csv')
start_date = input('What is the start date? format: YYYY-MM-DD\n')
end_date = input('What is the end date? format: YYYY-MM-DD\n')
original_df['Date'] = pd.to_datetime(original_df['Date'], format='%d/%m/%Y')

# only extract data within the given dates
df = original_df.loc[(original_df['Date'] >= f'{start_date}') & (original_df['Date'] <=f'{end_date}')]

# calculate the months differences between 2 dates
r = relativedelta.relativedelta(datetime.strptime(end_date, '%Y-%m-%d'), datetime.strptime(start_date, '%Y-%m-%d'))
total_period = (r.years * 12) + r.months

suppliers = df['Narrative']  # specify the supplier column


