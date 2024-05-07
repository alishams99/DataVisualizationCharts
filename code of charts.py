import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel('balance_data.xlsx')

activity_values = df['Activity']

value_counts = activity_values.value_counts()

threshold = 0.03 * sum(value_counts)

filtered_values = value_counts[value_counts >= threshold]
filtered_values['Other'] = value_counts[value_counts < threshold].sum()

plt.figure(figsize=(8, 6))
plt.pie(filtered_values, labels=filtered_values.index, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart of Column Activity')

plt.savefig('activity_pie_chart.png')
plt.show()







# x_values = df['Classification']

# value_counts = x_values.value_counts()

# # Calculate the threshold for the 3% limit
# threshold = 0.05 * sum(value_counts)

# # Filter the values based on the threshold
# filtered_values = value_counts[value_counts >= threshold]
# filtered_values['other'] = value_counts[value_counts < threshold].sum()

# # Plotting the pie chart
# plt.figure(figsize=(8, 6))
# plt.pie(filtered_values, labels=filtered_values.index, autopct='%1.1f%%', startangle=90)
# plt.title('Pie Chart of Column Classification')

# # Save the pie chart as an image file
# plt.savefig('pie_chart.png')

# # Display the pie chart
# plt.show()


# """
# day-night -- years
# """


# df['Day vs Night'] = df['Day vs Night'].str.strip().str.lower()
# df = df[df['Day vs Night'] != 'unknown']
# counts = df.groupby(['Year', 'Day vs Night']).size().unstack().fillna(0)

# counts.plot(kind='bar', stacked=True)
# plt.xlabel('Year')
# plt.ylabel('Count')
# plt.title('Day vs Night Counts for Each Year')
# plt.show()







# """gender - year
# """


# df['Gender'] = df['Gender'].str.lower()

# gender_mapping = {
#     'reported by female': 'female',
#     'female': 'female',
#     'reported by male': 'male',
#     'male': 'male',
# }

# df['Gender'] = df['Gender'].map(gender_mapping)

# df = df[df['Gender'] != 'unknown']
# df = df[df['Day vs Night'] != 'Unknown']
# grouped_data = df.groupby(['Year', 'Gender']).size().unstack().fillna(0)

# grouped_data.plot(kind='line')
# plt.xlabel('Year')
# plt.ylabel('Count')
# plt.title('Gender Counts for Each Year')
# plt.legend(title='Gender')
# plt.show()




# #Count of Occurrences for Each Month
# df['Date'] = pd.to_datetime(df['Date'])

# df['Month'] = df['Date'].dt.month_name()

# monthly_counts = df['Month'].value_counts()
# monthly_counts.plot(kind='bar')
# plt.xlabel('Month')
# plt.ylabel('Count')
# plt.title('Count of Occurrences for Each Month')
# plt.show()




# #Percentage of Occurrences for Each Month
# df['Date'] = pd.to_datetime(df['Date'])
# df['Month'] = df['Date'].dt.month_name()

# monthly_percentages = df['Month'].value_counts(normalize=True) * 100
# plt.pie(monthly_percentages, labels=monthly_percentages.index, autopct='%1.1f%%')
# plt.title('Percentage of Occurrences for Each Month')
# plt.show()




# #Percentage of Males and Females
# df['Gender'] = df['Gender'].str.lower()

# gender_mapping = {
#     'reported by female': 'female',
#     'female': 'female',
#     'reported by male': 'male',
#     'male': 'male',
# }

# df['Gender'] = df['Gender'].map(gender_mapping)
# gender_percentages = df['Gender'].value_counts(normalize=True) * 100
# plt.pie(gender_percentages, labels=gender_percentages.index, autopct='%1.1f%%')
# plt.title('Percentage of Males and Females')
# plt.show()



# #Percentage of Day and Night
# df['Day vs Night'] = df['Day vs Night'].str.lower()
# df = df[df['Day vs Night'] != 'unknown']

# day_night_percentages = df['Day vs Night'].value_counts(normalize=True) * 100

# plt.pie(day_night_percentages, labels=day_night_percentages.index, autopct='%1.1f%%')
# plt.title('Percentage of Day and Night')
# plt.show()





# #Percentage of Province Names
# df = df[df['Province'] != 'Unknown']
# province_percentages = df['Province'].value_counts(normalize=True) * 100

# threshold = 3

# province_percentages_others = province_percentages[province_percentages >= threshold]
# province_percentages_others['Others'] = province_percentages[province_percentages < threshold].sum()

# plt.pie(province_percentages_others, labels=province_percentages_others.index, autopct='%1.1f%%')
# plt.title('Percentage of Province Names')
# plt.show()

