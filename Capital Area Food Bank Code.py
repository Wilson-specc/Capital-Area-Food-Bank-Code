import pandas as pd
import matplotlib.pyplot as plt

#get rid of 'Custom field() in certain cols'
def rename_custom_fields(df):
    df.columns = [col.split('(')[-1].replace(')', '') if 'Custom field' in col else col for col in df.columns]
    return df

pd.set_option('display.max_columns', None)
df = pd.read_excel('data_case2.xlsx')

#drop comment cols at the end
df = df.iloc[:, :-22]
df = rename_custom_fields(df)

#plot different regions
sizes = df.groupby('Region').size()
sizes = sizes[sizes.index != 'All']
sizes['Not Stated'] = 167

print(sizes)

sizes.plot(kind='bar', color='green', edgecolor='black')
plt.title('Distribution of Regions')
plt.xticks(rotation=0)
plt.xlabel('Region')
plt.ylabel('Count')

plt.show()

#plot request types
grouped = df.groupby('Request Type').size()
grouped = grouped.sort_values(ascending=False)
print(grouped)

#some cleaning to make graph more readable
grouped = grouped.iloc[:-5]
grouped['Other'] = 16

ax = grouped.plot(kind='pie', labels=None, autopct='%1.1f%%')
ax.legend(grouped.index, loc='upper right', bbox_to_anchor=(2, 1))
plt.title('Most Common Request Types')

plt.show()