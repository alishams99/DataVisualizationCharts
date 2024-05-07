import pandas as pd
import matplotlib.pyplot as plt

excel_data = pd.read_excel('balance_data.xlsx')

x = "Nature of injury"
activity_values = excel_data[x]

value_counts = activity_values.value_counts()

# Calculate the threshold for the 3% limit
threshold = 0.01 * sum(value_counts)

filtered_values = value_counts.copy()
filtered_values['Other'] = filtered_values[filtered_values < threshold].sum()
filtered_values = filtered_values[filtered_values >= threshold]


plt.figure(figsize=(8, 6))
plt.pie(filtered_values, labels=filtered_values.index, autopct='%1.1f%%', startangle=90)
plt.title(f'Pie Chart of Column {x}')
plt.savefig(f'{x}_pie_chart.png')
plt.show()