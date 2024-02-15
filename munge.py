# place your code to clean up the data file below.
#I switched to anaconda3 interepreter because panda is not installed in the local Python interpreter
import pandas as pd
import urllib.request
import json 

url = 'https://data.cityofnewyork.us/resource/jb7j-dtam.json?$limit=2000'
response = urllib.request.urlopen(url)
data = json.load(response)

w = open("/Users/yizj/Desktop/Database Design/3-spreadsheet-analysis-beaverjuly/data/original_data_file.csv", "w")

headings = list(data[0].keys())
heading = []
for h in headings:
    s = ""
    for char in h:
        if char == "_":
            s += " "
        else:
            s += char
    headings[headings.index(h)] = s.title()
w.write(",".join(headings))
#I changed this line from "".join(headings) to ",".join(headings)
w.write("\n")

for i in data:
    w.write(",".join(i.values()))
    w.write("\n")

w.close()

df = pd.read_csv("'/Users/yizj/Desktop/Database Design/3-spreadsheet-analysis-beaverjuly/data/original_data_file.csv'")

#sort the DataFrame by 'Race Ethnicity' and then by 'Year' in ascending order
sorted_df = df.sort_values(by=['Race Ethnicity', 'Year'], ascending=[True, True])

sorted_df['Deaths'] = pd.to_numeric(sorted_df['Deaths'], errors='coerce')
sorted_df['Death Rate'] = pd.to_numeric(sorted_df['Death Rate'], errors='coerce')
sorted_df['Population Number'] = sorted_df['Deaths'] / sorted_df['Death Rate']*1000

#remove the original 'Death Rate' column so that it can be recalculated later
sorted_df.drop('Death Rate', axis=1, inplace=True)

#if 'Leading Cause', 'Sex', 'Race Ethnicity' are all the same, then combine these rows by summing 'Deaths' and 'Population Number'
grouped_df = sorted_df.groupby(['Year','Leading Cause', 'Sex', 'Race Ethnicity']).agg({
    'Deaths': 'sum',
    'Population Number': 'sum'
}).reset_index()

#recalculate the death rate
grouped_df['Death Rate'] = (grouped_df['Deaths'] / grouped_df['Population Number']) * 1000
grouped_df['Population Number'] = grouped_df['Population Number'].round(1)
grouped_df['Death Rate'] = grouped_df['Death Rate'].round(1)

import numpy as np
#replace 0.0 values with NaN
grouped_df['Deaths'] =grouped_df['Deaths'].replace(0, np.nan)
grouped_df['Population Number'] =grouped_df['Population Number'].replace(0, np.nan)
grouped_df['Death Rate'] =grouped_df['Death Rate'].replace(0, np.nan)
#also replace infinity values with NaN
grouped_df.replace([np.inf, -np.inf],np.nan,inplace=True)

grouped_file_path = '/Users/yizj/Desktop/Database Design/3-spreadsheet-analysis-beaverjuly/data/clean_data_file.csv'
grouped_df.to_csv(grouped_file_path, index=False)

unique_values = grouped_df['Leading Cause'].unique()
print(unique_values)