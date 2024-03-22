import pandas as pd

df = pd.read_csv('arduino_data.csv')

summary_stats = df.describe()
summary_stats.index = ['Count(N)', 'Mean(u)', 'SD', 'Min', 'Q1(25%)', 'Median(Q2 or 50%)', 'Q3(75%)', 'Max']
summary_stats.to_csv('data_collec/desc_stats/summary_statistics.csv', mode='a', header=False)

mean_values = df.mean()
mean_values.to_csv('data_collec/desc_stats/mean_values.csv', mode='a', header=False)

median_values = df.median()
median_values.to_csv('data_collec/desc_stats/median_values.csv', mode='a', header=False)

mode_values = df.mode().iloc[0] 
mode_values.to_csv('data_collec/desc_stats/mode_values.csv', mode='a', header=False)

std_dev_values = df.std()
std_dev_values.to_csv('data_collec/desc_stats/std_values.csv', mode='a', header=False)

variance_values = df.var()
variance_values.to_csv('data_collec/desc_stats/variance_values.csv', mode='a', header=False)
