import pandas as pd
import matplotlib
report_path = '/Users/rockesh/Documents/python_test/money_spent_on_amazon/amazon-orders.csv'

df = pd.read_csv(report_path)

df = df.fillna(0)

df['Total Charged'] = df['Total Charged'].str.replace('$','').astype(float)
print('Total Amount Spent on Amazon Orders: ' + str(df['Total Charged'].sum()))
print('Average Amount Spent Per Order: ' + str(df['Total Charged'].mean()))
print('Biggest Order: ' + str(df['Total Charged'].max()))
print('Smallest Order: ' + str(df['Total Charged'].min()))
print(df.plot.bar(x = 'Order Date', y = 'Total Charged', rot = 90))
#print(df.head)
#print(df.shape)