# Data Set Details
The data set, [New York City Leading Causes of Death](https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam/about_data), consists of data on the leading causes of death by sex and ethnicity in New York City since 2007, published and annually updated by the Department of Health and Mental Hygiene. For this exercise, we make use of the JSON format of the original data, converted it into CSV, and analyzed the data through Microsoft Excel.

## Sample raw data (the first 20 rows)
| Year  | Leading Cause | Sex  | Race Ethnicity | Deaths  | Death Rate | Age Adjusted Death Rate |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 2011  | Nephritis, Nephrotic Syndrome and Nephrisis (N00-N07, N17-N19, N25-N27)  | F  | Black Non-Hispanic  | 83  | 7.9  | 6.9  |
| 2009  | Human Immunodeficiency Virus Disease (HIV: B20-B24)  | F  | Hispanic  | 96  | 8  | 8.1  |
| 2009  | Chronic Lower Respiratory Diseases (J40-J47)  | F  | Hispanic  | 155  | 12.9  | 16  |
| 2008  | Diseases of Heart (I00-I09, I11, I13, I20-I51)  | F  | Hispanic  | 1445  | 122.3  | 160.7  |
| 2009  | Alzheimer's Disease (G30)  | F  | Asian and Pacific Islander  | 14  | 2.5  | 3.6  |
| 2008  | Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)  | F  | Asian and Pacific Islander  | 36  | 6.8  | 8.5  |
| 2012  | Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)  | M  | White Non-Hispanic  | 286  | 21.4  | 18.8  |
| 2008  | Assault (Homicide: Y87.1, X85-Y09)  | M  | Not Stated/Unknown  | 8  | -  | -  |
| 2009  | Chronic Lower Respiratory Diseases (J40-J47)  | M  | White Non-Hispanic  | 371  | 27.6  | 23.3  |
| 2013  | Diseases of Heart (I00-I09, I11, I13, I20-I51)  | F  | Not Stated/Unknown  | 106  | -  | -  |
| 2014  | Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)  | F  | Asian and Pacific Islander  | 42  | 6.7  | 6.9  |
| 2009  | Nephritis, Nephrotic Syndrome and Nephrisis (N00-N07, N17-N19, N25-N27)  | F  | Other Race/ Ethnicity  | -  | -  | -  |
| 2013  | Alzheimer's Disease (G30)  | F  | Hispanic  | 120  | 9.6  | 11  |
| 2011  | Malignant Neoplasms (Cancer: C00-C97)  | F  | Other Race/ Ethnicity  | 33  | -  | -  |
| 2009  | Essential Hypertension and Renal Diseases (I10, I12)  | F  | Hispanic  | 84  | 7  | 8.8  |
| 2007  | Diabetes Mellitus (E10-E14)  | M  | Other Race/ Ethnicity  | 11  | -  | -  |
| 2007  | Cerebrovascular Disease (Stroke: I60-I69)  | M  | White Non-Hispanic  | 267  | 20  | 16.7  |
| 2012  | Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)  | F  | White Non-Hispanic  | 177  | 12.5  | 8.5  |
| 2007  | Diseases of Heart (I00-I09, I11, I13, I20-I51)  | F  | Not Stated/Unknown  | 82  | -  | -  |
| 2007  | Chronic Lower Respiratory Diseases (J40-J47)  | F  | Hispanic  | 116  | 9.9  | 12.8 |

## Scrubbing task
In the original data, there exist two main issues, while lacking one piece of information we believe is critical to the analysis. Regarding the issues, the first one relates to the disorder of raw data, in which the entire dataset is not ordered based on any pattern, and the second one relates to the commas existing in the leading cause category. Spreadsheets might mistake them for a delimiter, thus resulting in autofilling parts of the text, despite it should be regarded as a whole, into different columns.

To address the first issue, we use the sort_values function in pandas:
```python
sorted_df = df.sort_values(by=['Race Ethnicity', 'Year'], ascending=[True, True])
```
As for the second issue, we put double quotes surrounding data with said problem:
 ```python
if "," in x:
    v = '"' + x + '"'
    x = v
```
The one piece of information we deem missing from the original data is population numbers. Population numbers serve as an indicator of the sex composition of each demographic within the provided data. Additionally, when combined with age adjustment, population numbers could help to deduce the age distribution across different races and ethnicities, allowing for an assessment of susceptibility to specific causes of death across populations of different ages.

To calculate population numbers using data on deaths and death rate, we have code:
```python
sorted_df['Population Number'] = sorted_df['Deaths'] / sorted_df['Death Rate']*1000
```
An additional minor confusion we encountered was that in the official introduction of the dataset, there are no specific descriptions as to how death numbers are collected, and why there exists seemingly dupicate rows where all categorical columns have the same value, yet the correponding death count and death rate values are not the same. 

We dealt with this by assuming that the death counts recorded in the categorically identical rows correspond to non-overlapping populations, and thus combined these rows by aggregating the death count and recomputing the death rate. 

## Analysis (Important: my partner and I did not collaborate on this aspect; we computed different statistics and made graphs with different strategies)

I computed the Mean, the Median, and the Standard Deviation of death rate over the entire range of years for each ethnic group and for each Leading Cause of Death (meaning two conditions for each value computed) using Excel built-in formulas.
In addition, I computed the difference between mean and median.

**Comparison of Mean shows Variability Among Ethnic Groups** 
There is a noticeable variation in mean death rates **between** different ethnic groups for certain diseases. 

For instance, the mean death rate for 'Accidents Except Drug Poisoning' and 'All Other Causes' is significantly higher in the 'White Non-Hispanic' group compared to other ethnic groups.

**Standard Deviation (SD) as a Measure of Disparity** 
The SD provides insight into the variability of death rates **within** each ethnic group for a given cause. 

For example, 'All Other Causes' shows a relatively high SD in the 'White Non-Hispanic' group, indicating more variability in death rates.

**Comparing Mean and Median** 
For many diseases, the mean and median values are close, suggesting a relatively symmetrical distribution of data around the central value. However, where there are significant differences between mean and median, it might indicate a skewed distribution, possibly due to outliers or an asymmetrical spread of death rates.

The largest discrepency between mean and median death rates occurs for the Leading Cause of Death of Diseases of Heart (I00-I09, I11, I13, I20-I51) among the White, Non-Hispanic population. The Mean is higher than the Median by 22.99, indicating a positive skew.

**Bar Charts**

![Mean Bar Chart](/Mean_Bar_Chart.png)

![Median Bar Chart](/Median_Bar_Chart.png)


These charts are for more convenient comparisons between ethnic groups.

White Non-Hispanics generally have higher death rates for the causes listed, with the exception of diabetes and hypertension-related diseases, where Black Non-Hispanics have the highest rates. 

## Links to data files:
- [New York City Leading Causes of Death](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-beaverjuly/blob/main/data/original_data_file.csv)
- [Munged Data: New York City Leading Causes of Death](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-beaverjuly/blob/main/data/clean_data_file.csv)
- [Spreadsheet: New York City Leading Causes of Death](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-beaverjuly/blob/main/data/Spreadsheet%20File.xlsx)