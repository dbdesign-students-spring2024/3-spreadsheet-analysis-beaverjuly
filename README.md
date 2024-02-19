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

## Links to data files:
- [New York City Leading Causes of Death](https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam/data_preview)
- [Munged Data: New York City Leading Causes of Death](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-shaw2065/blob/main/data/clean_data.csv)
- [Spreadsheet: New York City Leading Causes of Death](https://github.com/dbdesign-students-spring2024/3-spreadsheet-analysis-shaw2065/blob/main/data/clean_data.xlsx)

# Spreadsheet Analysis
## 1. Maximum and Minimum of Deaths and Death Rate 
We use the MIN() and MAX() functions to find the minimum and maximum values of deaths and death rates. To further examine the data, we employ the INDEX() and MATCH() functions to retrieve other relevant data: leading cause, sex, race/ethnicity, and corresponding deaths and death rates. We utilize this data to assess the mortality rate of each cause of death, specifically analyzing the factors contributing to these statistics.
### Maximum Deaths
| Maximum Deaths  | Leading Cause | Sex  | Race Ethnicity | Death Rate  |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 7050  | Diseases of Heart (I00-I09, I11, I13, I20-I51)  | F  | White Non-Hispanic  | 491.4  |

Heart disease emerges as the leading cause of death among white non-Hispanic females, with 7050 deaths recorded. This underscores the necessity for targeted interventions to address cardiovascular health issues in this demographic group. Additionally, it's noteworthy that the high mortality rate may be partially attributed to the larger population numbers of white non-Hispanic females in New York City.

### Maximum Death Rate
| Maximum Death Rate  | Leading Cause | Sex  | Race Ethnicity | Deaths  |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 491.4  | Diseases of Heart (I00-I09, I11, I13, I20-I51)  | F  | White Non-Hispanic  | 7050  |

Among white non-Hispanic females, heart disease exhibits the highest death rate at 491.4, which also constitutes the highest number of deaths. This high death rate highlights the urgent need to prevent and manage heart disease in this demographic group. Meanwhile, given that cardiovascular health is relevant to all races, such measures should be applied across ethnic groups.

### Minimum Deaths
| Minimum Deaths  | Leading Cause | Sex  | Race Ethnicity | Death Rate  |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 5  | Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)  | M  | Other Race/ Ethnicity  | -  |

The minimum sum of deaths can be attributed to two factors: smaller populations and a low incidence of fatalities. Firstly, the "other race/ethnicity" category comprises a smaller population compared to the four other ethnic groups that make up the majority of the dataset. Secondly, accidents are not highly repeatable events with a generally high mortality rate, which explains the lowest sum of deaths.

### Minimum Death Rate
| Minimum Death Rate  | Leading Cause | Sex  | Race Ethnicity | Deaths  |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| 2.4  | Nephritis, Nephrotic Syndrome and Nephrisis (N00-N07, N17-N19, N25-N27)  | F  | Asian and Pacific Islander  | 13  |

The data shows a low death rate, 2.4, for nephritis, nephrotic syndrome, and nephrosis among Asian and Pacific Islander females, with 13 deaths recorded. This suggests relatively favorable health outcomes for this demographic group concerning these conditions, which may result from healthier habits related to these issues.

## 2. Mean Death Rate of Each Unique Leading Cause of Death for Each Race Ethnicity 

We also computed the Mean, the Median, and the Standard Deviation of death rate over the entire range of years for each ethnic group and for each Leading Cause of Death (meaning two conditions for each value computed) using Excel built-in formulas.
In addition, we computed the difference between mean and median.

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

![MeanBarChart](Mean_Bar_Chart.png)
![MedianBarChart](Median_Bar_Chart.png)



These charts are for more convenient comparisons between ethnic groups.

White Non-Hispanics generally have higher death rates for the causes listed, with the exception of diabetes and hypertension-related diseases, where Black Non-Hispanics have the highest rates. 

## 3. Specific Analysis for the Leading Death Cause of Diabetes
We use pivot table and pivot chart to examine the average death rate of diabetes mellitus among different ethnic groups from 2007 to the most recent data available. Below are the details provided by both the pivot table and pivot chart:
### Pivot Table
| Year  | Asian and Pacific Islander | Black Non-Hispanic  | Hispanic | Not Stated/ Unknown  | Other Race/ Ethnicity | White Non-Hispanic  | Total |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 2007  |  8.15  | 31.45  | 16.90  | -  | -  | 16.90  | 18.35  |
| 2008  |  9.60  | 33.75  | 18.30  | -  | -  | 16.45  | 19.53  |
| 2009  |  9.70  | 35.15  | 16.65  | -  | -  | 18.75  | 20.06  |
| 2010  |  10.70 | 34.70  | 17.20  | -  | -  | 18.15  | 20.19  |
| 2011  |  10.15  | 37.60  | 16.65  | -  | -  | 18.60  | 20.75  |
| 2012  |  11.95  | 37.55  | 16.35  | -  | -  | 19.35  | 21.30  |
| 2013  |  13.65  | 37.15  | 17.00  | -  | -  | 18.20  | 21.50  |
| 2014  |  10.20  | 37.35  | 16.05  | -  | -  | 18.90  | 20.63  |
| Average  |  10.51  | 35.59  | 16.89  | -  | -  | 18.16  | 20.29  |

In the pivot table, the average death rate of diabetes mellitus is displayed. Each cell corresponds to a specific year and ethnic group, showcasing the average death rate across both sexes included in the dataset. For cells representing a year and total, the enclosed data represents the average death rate across all populations included for that particular year. The "Average" row displays the average death rate of each ethnic group, or all combined, across the years included in the dataset.

### Pivot Chart
![Pivot Chart on Deaths and Death Rate of Diabetes Mellitus](Diabetes_Pivot_Chart.png)
The pivot chart visualizes the changing average death rate of diabetes mellitus over time. The horizontal axis represents each year included in the dataset, while the vertical axis displays the average death rate. Each line on the chart represents the changing average death rate, inclusive of both sexes, for each ethnic group across the years.

## Analysis
Tthe pivot table and pivot chart reveals significant disparities in the death rate of diabetes mellitus among different ethnic groups. Specifically, Black non-Hispanic populations exhibit a higher death rate compared to other ethnic groups. While other ethnic groups show relatively stable trends in death rates, the trend for Black non-Hispanic populations demonstrates a sharp increase over time. On the other hand, Asian and Pacific Islander populations consistently maintain the lowest death rates across all years, while Hispanic and White non-Hispanic populations exhibit similar average death rates.  
Several factors may contribute to these disparities, including lifestyle choices and socioeconomic status. Families with healthier eating habits and regular exercise routines tend to have lower rates of obesity and diabetes. However, access to healthier food options and opportunities for exercise may be limited by household income. Therefore, socioeconomic factors likely play a significant role in the observed differences in diabetes-related health outcomes among ethnic groups.

## Extra-credit
This assignment deserves extra credit because we use Python to retrieve the data directly from the webpage using urllib.request instead of downloading the provided CSV file. Additionally, this dataset currently contains a total of 1,094 rows, and we write our code to be capable of retrieving a total of 2,000 rows for future updates on the dataset.

