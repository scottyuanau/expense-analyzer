import pandas as pd
from matplotlib import pyplot as plt
import math
from findexpensecategory import findExpenseCategory
from dateutil import relativedelta
from datetime import datetime
import os

# input file setup
original_df = pd.read_csv('input.csv')

# ask user to input the start and end date for the report
# start_date = input('What is the start date? format: YYYY-MM-DD\n')
# end_date = input('What is the end date? format: YYYY-MM-DD\n')
start_date ='2022-01-01'
end_date = '2022-06-30'
original_df['Date'] = pd.to_datetime(original_df['Date'], format='%d/%m/%Y')

# only extract data within the given dates
df = original_df.loc[(original_df['Date'] >= f'{start_date}') & (original_df['Date'] <=f'{end_date}')]

# check if results folder exists, and create a folder if it doesn't exist
if not os.path.exists('results'):
    os.makedirs('results')

# calculate the months differences between 2 dates
r = relativedelta.relativedelta(datetime.strptime(end_date, '%Y-%m-%d'), datetime.strptime(start_date, '%Y-%m-%d'))
total_period = (r.years * 12) + r.months

# specify the supplier column
suppliers = df['Narrative']

each_supplier_cost_all = df.groupby(['Narrative'])['Debit Amount'].sum()  # group supplier by name

result = []
for supplier, total_expense in each_supplier_cost_all.items():
    if total_expense != 0:  # drop empty value
        avg_expense = math.floor(total_expense / total_period)
        result.append([supplier, findExpenseCategory(supplier), avg_expense])

# convert result back to dataframe & save to processed.csv
converted_df = pd.DataFrame(result, columns=['Supplier', 'Category', 'Monthly Expenses'])
converted_df.to_csv(f'results/processed-check.csv')

#filter out business expense
living_expense_df = converted_df.loc[converted_df['Category']!='Business']
# analyze the category
analyzed_result = converted_df.groupby(['Category'])['Monthly Expenses'].sum()
total_living_expense = analyzed_result.sum() - analyzed_result['Business']

# draw visual chart
labels = []
sizes = []
threshold = 5
other = 0  # merge small categories into other
for label, amount in analyzed_result.items():
    if label != 'Business' and round(amount / total_living_expense * 100) >= threshold:
        labels.append(label)
        sizes.append(round(amount / total_living_expense * 100))
    elif label != 'Business' and round(amount / total_living_expense * 100) < threshold:
        other += round(amount / total_living_expense * 100)

# add other category
labels.append('Other')
sizes.append(other)

fig1, (ax1, ax2) = plt.subplots(2, 1, figsize=(18, 9), dpi=150)
# pie chart

ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')



# bar chart
ax2.bar(labels, sizes)
ax2.set_xlabel('Expense Category')
ax2.set_ylabel('Expense per month')
ax2.set_title('Category Spending per Month')

plt.savefig(f'results/{start_date} to {end_date} illustration.png', dpi=300)


analyzed_result.nlargest(n=5).to_csv('results/top-5-categories-spending.csv')
living_expense_df.nlargest(n=10, columns="Monthly Expenses").to_csv('results/top-10-expenses.csv', index=False)
print(f'Living Expense per month during these {total_period} months: ${total_living_expense}')
print(f'Top 5 Categories spending during these {total_period} months: \n{analyzed_result.nlargest(n=5)}')
print(f'Top 10 spending supplier during these {total_period} months: \n{living_expense_df.nlargest(n=10, columns="Monthly Expenses")}')
# pd.concat([analyzed_result.nlargest(n=5), living_expense_df.nlargest(n=10, columns="Monthly Expenses")],keys=['Top 5 Category','Top 10 Supplier']).to_csv(f'results/{start_date} to {end_date} analyzed result.csv')

# Todo: 1. Generate output excel report.
# Todo: 2. Change reporting diagram.