import pandas as pd
from matplotlib import pyplot as plt
import math
from findexpensecategory import findExpenseCategory
from dateutil import relativedelta
from datetime import datetime
import numpy as np
import os


original_df = pd.read_csv('input.csv')

# ask user to input the start and end date for the report
# start = input('What is the start date? format: DDMMYYYY\n')
# end = input('What is the end date? format: DDMMYYYY\n')
# start_date = f'{start[4:]}-{start[2:4]}-{start[0:2]}'
# end_date = f'{end[4:]}-{end[2:4]}-{end[0:2]}'

start_date = '2021-01-01'
end_date = '2022-12-31'

original_df['Date'] = pd.to_datetime(original_df['Date'], format='%d/%m/%Y')

# only extract data within the given dates
df = original_df.loc[(original_df['Date'] >= f'{start_date}') & (original_df['Date'] <= f'{end_date}')]

# check if results folder exists, and create a folder if it doesn't exist
if not os.path.exists('results'):
    os.makedirs('results')

# calculate the months differences between 2 dates
r = relativedelta.relativedelta(datetime.strptime(end_date, '%Y-%m-%d'), datetime.strptime(start_date, '%Y-%m-%d'))
total_period = (r.years * 12) + r.months


suppliers = df['Narrative']

each_supplier_cost_all = df.groupby(['Narrative'])['Debit Amount'].sum()  # group supplier by name

result = []
for supplier, total_expense in each_supplier_cost_all.items():
    if total_expense != 0:  # drop empty value
        avg_expense = math.floor(total_expense / total_period)
        result.append([supplier, findExpenseCategory(supplier), avg_expense])

# convert result back to dataframe & save to processed.csv
converted_df = pd.DataFrame(result, columns=['Supplier', 'Category', 'Monthly Expenses'])

# use the z-processed-check.csv file to check if the expense has been categorized,
# if not, add them into the findexpensecategory.py
empty_col = converted_df.loc[converted_df['Category'].isna()]['Supplier']
empty_col.to_csv('results/to-be-processed.csv')
converted_df.to_csv('results/monthly-expenses.csv')


# filter out business expense
living_expense_df = converted_df.loc[converted_df['Category'] != 'Business']
# analyze the category
analyzed_result = converted_df.groupby(['Category'])['Monthly Expenses'].sum()
total_living_expense = analyzed_result.sum() - analyzed_result['Business']

# draw visual chart
labels = []
sizes = []
yticks = []  # dollar amount for the yticks in bar chart
threshold = 5
other_percentage = 0  # merge small categories into other
other_amount = 0  # dollar amount for other expenses
for label, amount in analyzed_result.items():
    if label != 'Business' and round(amount / total_living_expense * 100) >= threshold:
        labels.append(label)
        sizes.append(round(amount / total_living_expense * 100))
        yticks.append(round(amount))
    elif label != 'Business' and round(amount / total_living_expense * 100) < threshold:
        other_percentage += round(amount / total_living_expense * 100)
        other_amount += round(amount)
# add other category
labels.append('Other')
sizes.append(other_percentage)
yticks.append(other_amount)

analyzed_df = pd.DataFrame({'Labels': labels, 'Expenses': sizes}).sort_values(by='Expenses', ascending=False)


fig1, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15), dpi=150)
fig1.suptitle(f'Expense Analysis from {start_date} to {end_date}', size=20,weight='bold')
fig1.tight_layout(pad=5)
# set the spacing between subplots
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)
# pie chart

# set up explode for the pie chart
explode = []
for value in analyzed_df['Expenses']:
    if value > 20:
        explode.append(0.2)
    else:
        explode.append(0)


ax1.pie(analyzed_df['Expenses'], labels=analyzed_df['Labels'], autopct='%1.1f%%', explode=explode, startangle=90)
ax1.set_title('Percentage Analysis',fontdict={'size': 16, 'weight': 'bold'})
ax1.axis('equal')
ax1.legend()

# bar chart, top 5 categories
ax2.bar(analyzed_df['Labels'], analyzed_df['Expenses'] / 100 * total_living_expense)
ax2.set_xlabel('Expense Category')
ax2.set_ylabel('Expense per month', labelpad=10)
ax2.set_title('Top Spending Categories', fontdict={'size': 16, 'weight': 'bold'})
ax2.set_yticks(np.arange(0, 1100, 100))
ax2.yaxis.set_major_formatter('${x:1.0f}')  # add dollar sign to y axis

# bar chart, top 10 expenses
ax3.bar(living_expense_df.nlargest(n=10, columns="Monthly Expenses")['Supplier'], living_expense_df.nlargest(n=10, columns="Monthly Expenses")['Monthly Expenses'], width=0.5)
ax3_x_labels = ax3.get_xticklabels()
ax3_truncated_x_labels =[label.get_text()[:10] for label in ax3_x_labels]
ax3.set_xticklabels(ax3_truncated_x_labels, rotation=45)
ax3.set_title('Top Spending Suppliers', fontdict={'size': 16, 'weight': 'bold'})


plt.savefig(f'results/report.pdf', dpi=300)


print('Reports exported.')