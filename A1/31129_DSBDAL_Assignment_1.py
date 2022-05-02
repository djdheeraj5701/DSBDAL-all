# Importing required libraries
import pandas as pd

# Loading dataset into a dataframe
d=pd.read_csv("melb_data.csv")
df=pd.DataFrame(d)

# Describe variables in dataframe
print("\n# Describe variables in dataframe")
for i in df:
    print(df[i].describe(),end="\n\n")

# Dimensions of dataframe
print("\n# Dimensions of dataframe")
print("ndim:",df.ndim)
print("shape:",df.shape)
print("size:",df.size)
print("memory_usage:")
print(df.memory_usage())

# Check if a column has any missing values
print("\n# Check if a column has any missing values")
for i in df:
    print(f"{i}: {any(df[i].isna())}")

# Types of variables in dataframe
print("\n# Types of variables in dataframe")
print(df.dtypes)

# Change variable to appropriate type
# Postcode         float64 => int64
# Bedroom2         float64 => int64
# Bathroom         float64 => int64
# Car              float64 => int64 ohh but it contains NaN
# YearBuilt        float64 => int64 ohh but it contains NaN

# Filling the missing values with default 0
print("\n# Filling the missing values with default 0")
for i in df:
    df[i].fillna(0,inplace=True)
for i in df:
    print(f"{i}: {any(df[i].isna())}")


# Change variable to appropriate type
print("\n# Change variable to appropriate type")
for i in "Postcode Bedroom2 Bathroom Car YearBuilt".split():
    df[i]=df[i].astype('int64')
    print(i,df[i].dtype)

# Change categorical to quantitative
print("\n# Change categorical to quantitative")
df=pd.get_dummies(df,columns=['Type'])
print(df)

# Write to a file
print("\n# Writing to a file")
df.to_csv('output.csv')
print("# Saved")

'''
/usr/bin/python3.8 /home/pict/31129_DSBDAL/A1/31129_DSBDAL_Assignment_1.py

# Describe variables in dataframe
count         13580
unique          314
top       Reservoir
freq            359
Name: Suburb, dtype: object

count                13580
unique               13378
top       36 Aberfeldie St
freq                     3
Name: Address, dtype: object

count    13580.000000
mean         2.937997
std          0.955748
min          1.000000
25%          2.000000
50%          3.000000
75%          3.000000
max         10.000000
Name: Rooms, dtype: float64

count     13580
unique        3
top           h
freq       9449
Name: Type, dtype: object

count    1.358000e+04
mean     1.075684e+06
std      6.393107e+05
min      8.500000e+04
25%      6.500000e+05
50%      9.030000e+05
75%      1.330000e+06
max      9.000000e+06
Name: Price, dtype: float64

count     13580
unique        5
top           S
freq       9022
Name: Method, dtype: object

count      13580
unique       268
top       Nelson
freq        1565
Name: SellerG, dtype: object

count          13580
unique            58
top       27/05/2017
freq             473
Name: Date, dtype: object

count    13580.000000
mean        10.137776
std          5.868725
min          0.000000
25%          6.100000
50%          9.200000
75%         13.000000
max         48.100000
Name: Distance, dtype: float64

count    13580.000000
mean      3105.301915
std         90.676964
min       3000.000000
25%       3044.000000
50%       3084.000000
75%       3148.000000
max       3977.000000
Name: Postcode, dtype: float64

count    13580.000000
mean         2.914728
std          0.965921
min          0.000000
25%          2.000000
50%          3.000000
75%          3.000000
max         20.000000
Name: Bedroom2, dtype: float64

count    13580.000000
mean         1.534242
std          0.691712
min          0.000000
25%          1.000000
50%          1.000000
75%          2.000000
max          8.000000
Name: Bathroom, dtype: float64

count    13518.000000
mean         1.610075
std          0.962634
min          0.000000
25%          1.000000
50%          2.000000
75%          2.000000
max         10.000000
Name: Car, dtype: float64

count     13580.000000
mean        558.416127
std        3990.669241
min           0.000000
25%         177.000000
50%         440.000000
75%         651.000000
max      433014.000000
Name: Landsize, dtype: float64

count     7130.000000
mean       151.967650
std        541.014538
min          0.000000
25%         93.000000
50%        126.000000
75%        174.000000
max      44515.000000
Name: BuildingArea, dtype: float64

count    8205.000000
mean     1964.684217
std        37.273762
min      1196.000000
25%      1940.000000
50%      1970.000000
75%      1999.000000
max      2018.000000
Name: YearBuilt, dtype: float64

count        12211
unique          33
top       Moreland
freq          1163
Name: CouncilArea, dtype: object

count    13580.000000
mean       -37.809203
std          0.079260
min        -38.182550
25%        -37.856822
50%        -37.802355
75%        -37.756400
max        -37.408530
Name: Lattitude, dtype: float64

count    13580.000000
mean       144.995216
std          0.103916
min        144.431810
25%        144.929600
50%        145.000100
75%        145.058305
max        145.526350
Name: Longtitude, dtype: float64

count                     13580
unique                        8
top       Southern Metropolitan
freq                       4695
Name: Regionname, dtype: object

count    13580.000000
mean      7454.417378
std       4378.581772
min        249.000000
25%       4380.000000
50%       6555.000000
75%      10331.000000
max      21650.000000
Name: Propertycount, dtype: float64


# Dimensions of dataframe
ndim: 2
shape: (13580, 21)
size: 285180
memory_usage:
Index               128
Suburb           108640
Address          108640
Rooms            108640
Type             108640
Price            108640
Method           108640
SellerG          108640
Date             108640
Distance         108640
Postcode         108640
Bedroom2         108640
Bathroom         108640
Car              108640
Landsize         108640
BuildingArea     108640
YearBuilt        108640
CouncilArea      108640
Lattitude        108640
Longtitude       108640
Regionname       108640
Propertycount    108640
dtype: int64

# Check if a column has any missing values
Suburb: False
Address: False
Rooms: False
Type: False
Price: False
Method: False
SellerG: False
Date: False
Distance: False
Postcode: False
Bedroom2: False
Bathroom: False
Car: True
Landsize: False
BuildingArea: True
YearBuilt: True
CouncilArea: True
Lattitude: False
Longtitude: False
Regionname: False
Propertycount: False

# Types of variables in dataframe
Suburb            object
Address           object
Rooms              int64
Type              object
Price            float64
Method            object
SellerG           object
Date              object
Distance         float64
Postcode         float64
Bedroom2         float64
Bathroom         float64
Car              float64
Landsize         float64
BuildingArea     float64
YearBuilt        float64
CouncilArea       object
Lattitude        float64
Longtitude       float64
Regionname        object
Propertycount    float64
dtype: object

# Filling the missing values with default 0
Suburb: False
Address: False
Rooms: False
Type: False
Price: False
Method: False
SellerG: False
Date: False
Distance: False
Postcode: False
Bedroom2: False
Bathroom: False
Car: False
Landsize: False
BuildingArea: False
YearBuilt: False
CouncilArea: False
Lattitude: False
Longtitude: False
Regionname: False
Propertycount: False

# Change variable to appropriate type
Postcode int64
Bedroom2 int64
Bathroom int64
Car int64
YearBuilt int64

# Change categorical to quantitative
              Suburb           Address  Rooms  ...  Type_h Type_t Type_u
0         Abbotsford      85 Turner St      2  ...       1      0      0
1         Abbotsford   25 Bloomburg St      2  ...       1      0      0
2         Abbotsford      5 Charles St      3  ...       1      0      0
3         Abbotsford  40 Federation La      3  ...       1      0      0
4         Abbotsford       55a Park St      4  ...       1      0      0
...              ...               ...    ...  ...     ...    ...    ...
13575  Wheelers Hill      12 Strada Cr      4  ...       1      0      0
13576   Williamstown     77 Merrett Dr      3  ...       1      0      0
13577   Williamstown       83 Power St      3  ...       1      0      0
13578   Williamstown      96 Verdon St      4  ...       1      0      0
13579     Yarraville        6 Agnes St      4  ...       1      0      0

[13580 rows x 23 columns]

# Writing to a file
# Saved

Process finished with exit code 0

'''

