import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
excel_file_path = 'balance_data.xlsx'
df = pd.read_excel(excel_file_path)

# Group by 'Year' and 'Nature of injury' and calculate the percentage
grouped_data = df.groupby(['Year', 'Nature of injury']).size().unstack(fill_value=0)
percentage_data = grouped_data.div(grouped_data.sum(axis=1), axis=0) * 100

# Plot the line chart
plt.figure(figsize=(10, 6))

for injury_type in percentage_data.columns:
    plt.plot(percentage_data.index, percentage_data[injury_type], label=injury_type)

plt.title('Percentage of Nature of Injury over the Years')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.legend(loc='upper right')
plt.grid(True)
plt.show()
