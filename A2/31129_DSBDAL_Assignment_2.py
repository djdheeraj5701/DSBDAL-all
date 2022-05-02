import time

import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset
print("\n# Reading the dataset")
d = pd.read_csv("StudentsPerformance.csv")
df = pd.DataFrame(d)

# Check if a column has any missing values
print("\n# Check if a column has any missing values")
for i in df:
    print(f"{i}: {any(df[i].isna())}")

# Remove the rows with missing values
print("\n# Remove the rows with missing values")
print(df.shape)
df.dropna(inplace=True)
print(df.shape)

# Remove inconsistency like female and Female, male and Male
print("\n# Remove inconsistency")
df.replace(regex=[r"female|Female"], value="F", inplace=True)
df.replace(regex=[r"male|Male"], value="M", inplace=True)
for i in "ABCDE":
    df.replace(regex=[r"group " + i], value=i, inplace=True)

# Change categorical to quantitative
print("\n# Change categorical to quantitative")
df = pd.get_dummies(df, columns=['gender', 'test preparation'])
print(df)

# Boxplot the numerical values to find outliers
print("\n# Boxplot the numerical values to find outliers")
df.boxplot(column=["math score", "reading score", "writing score"])
plt.savefig("boxplot.png")
plt.close()

# Handling the outliers
'''
An Outlier is an observation in a given dataset that lies far from the rest of the observations. 
That means an outlier is vastly larger or smaller than the remaining values in the set.
An outlier may occur due to the variability in the data, or due to experimental error/human error.
They may indicate an experimental error or heavy skewness in the data(heavy-tailed distribution).
Mean is the accurate measure to describe the data when we do not have any outliers present.
Median is used if there is an outlier in the dataset.
Mode is used if there is an outlier AND about ½ or more of the data is the same.
‘Mean’ is the only measure of central tendency that is affected by the outliers which in turn impacts Standard deviation.

Below are some of the techniques of detecting outliers
Boxplots
Z-score
Inter Quantile Range(IQR)

Below are some of the methods of treating the outliers
Trimming/removing the outlier : Although it is not a good practice
Quantile based flooring and capping : at a certain value above the 90th percentile value or floored at a factor below the 10th percentile value.
Mean/Median imputation : As the mean value is highly influenced by the outliers, it is advised to replace the outliers with the median value.
'''
print("\n# Handling the outliers")
for i in ["math score", "reading score", "writing score"]:
    q1 = df[i].quantile(0.25)
    q2 = df[i].median()
    q3 = df[i].quantile(0.75)

    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    lower_outliers = df[i] < lower_limit
    upper_outliers = df[i] > upper_limit

    df[i] = df[i][~(lower_outliers | upper_outliers)]
df.dropna(inplace=True)

print("Outliers were removed")
df.boxplot(column=["math score", "reading score", "writing score"])
plt.savefig("boxplot_outlier_removed.png")
plt.close()

# Performing normalization
'''
Normalization is a technique often applied as part of data preparation for machine learning. 
The goal of normalization is to change the values of numeric columns in the 
dataset to use a common scale, without distorting differences in the ranges 
of values or losing information.

Z-score is a variation of scaling that represents the number of standard deviations away 
from the mean. You would use z-score to ensure your feature distributions 
have mean = 0 and std = 1. It's useful when there are a few outliers, but 
not so extreme that you need clipping.

Another way to normalize the input features/variables (apart from the 
standardization that scales the features so that they have μ=0and σ=1) 
is the Min-Max scaler. By doing so, all features will be transformed 
into the range [0,1] meaning that the minimum and maximum value of a 
feature/variable is going to be 0 and 1, respectively.

'''
df2 = df[["math score", "reading score", "writing score"]]
print("\nBefore normalization")
print(df2.describe())

print("\nNormalization by z score")

dfzscore = (df2 - df2.mean()) / df2.std()
print(dfzscore.describe())

dfzscore.boxplot()
plt.savefig("boxplot_zscore.png")
plt.close()

print("\nNormalization by min-max")
dfminmax = (df2 - df2.min()) / (df2.max() - df2.min())
print(dfminmax.describe())

dfminmax.boxplot()
plt.savefig("boxplot_minmax.png")
plt.close()

df.to_csv("output.csv", index=False)

'''
C:\Users\DJdheeraj\PycharmProjects\westart\venv\Scripts\python.exe C:/Users/DJdheeraj/PycharmProjects/westart/DSBDA/31129_DSBDAL_Assignment_2.py

# Reading the dataset

# Check if a column has any missing values
gender: False
batch: False
test preparation: False
math score: True
reading score: True
writing score: True

# Remove the rows with missing values
(1000, 6)
(989, 6)

# Remove inconsistency

# Change categorical to quantitative
    batch  math score  ...  test preparation_completed  test preparation_none
1       C        69.0  ...                           1                      0
2       B        90.0  ...                           0                      1
3       A        47.0  ...                           0                      1
4       C        76.0  ...                           0                      1
5       B        71.0  ...                           0                      1
..    ...         ...  ...                         ...                    ...
995     E        88.0  ...                           1                      0
996     C        62.0  ...                           0                      1
997     C        59.0  ...                           1                      0
998     D        68.0  ...                           1                      0
999     D        77.0  ...                           0                      1

[989 rows x 8 columns]

# Boxplot the numerical values to find outliers

# Handling the outliers
Outliers were removed

Before normalization
       math score  reading score  writing score
count  977.000000     977.000000     977.000000
mean    66.637666      69.667349      68.595701
std     14.407411      13.991174      14.511418
min     27.000000      29.000000      27.000000
25%     57.000000      60.000000      58.000000
50%     66.000000      70.000000      69.000000
75%     77.000000      80.000000      79.000000
max    100.000000     100.000000     100.000000

Normalization by z score
         math score  reading score  writing score
count  9.770000e+02   9.770000e+02   9.770000e+02
mean   1.781811e-16  -2.872716e-16  -1.999992e-16
std    1.000000e+00   1.000000e+00   1.000000e+00
min   -2.751200e+00  -2.906643e+00  -2.866412e+00
25%   -6.689381e-01  -6.909605e-01  -7.301630e-01
50%   -4.425960e-02   2.377577e-02   2.786074e-02
75%    7.192363e-01   7.385121e-01   7.169733e-01
max    2.315637e+00   2.167985e+00   2.164110e+00

Normalization by min-max
       math score  reading score  writing score
count  977.000000     977.000000     977.000000
mean     0.542982       0.572780       0.569804
std      0.197362       0.197059       0.198787
min      0.000000       0.000000       0.000000
25%      0.410959       0.436620       0.424658
50%      0.534247       0.577465       0.575342
75%      0.684932       0.718310       0.712329
max      1.000000       1.000000       1.000000

Process finished with exit code 0

'''
