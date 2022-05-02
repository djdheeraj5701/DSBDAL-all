import pandas as pd
import json

d=pd.read_csv("Iris.csv")
df=pd.DataFrame(d)

species=["Iris-setosa","Iris-versicolor","Iris-virginica"]

mean=dict()
median=dict()
minimum=dict()
maximum=dict()
stddev=dict()
percentile=dict()

frames=[df[df['Id']<51],None,df[df['Id']>100]]
frames[1]=df[df['Id']>50]
frames[1]=frames[1][df['Id']<101]

for i in range(3):
    mean[species[i]]=dict()
    median[species[i]] = dict()
    minimum[species[i]] = dict()
    maximum[species[i]] = dict()
    stddev[species[i]] = dict()
    percentile[species[i]]=dict()
    for j in "SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm".split():
        mean[species[i]][j]=frames[i][j].mean()
        median[species[i]][j] = frames[i][j].median()
        minimum[species[i]][j] = frames[i][j].min()
        maximum[species[i]][j] = frames[i][j].max()
        stddev[species[i]][j] = frames[i][j].std()
        percentile[species[i]][j]={
            10: frames[i][j].quantile(0.1),
            20: frames[i][j].quantile(0.2),
            30: frames[i][j].quantile(0.3),
            40: frames[i][j].quantile(0.4),
            50: frames[i][j].quantile(0.5),
            60: frames[i][j].quantile(0.6),
            70: frames[i][j].quantile(0.7),
            80: frames[i][j].quantile(0.8),
            90: frames[i][j].quantile(0.9),
        }

def display(s,d):
    print('*****'*3+s+'*****'*3)
    print(json.dumps(
        d,
        indent=4,
        separators=(',',': ')
    ))

# display("mean",mean)
# display("median",median)
# display("minimum",minimum)
# display("maximum",maximum)
# display("stddev",stddev)
display("percentile",percentile)

print('\n'+'*****'*3+"Iris-setosa"+'*****'*3)
print(frames[0].describe())
print('\n'+'*****'*3+"Iris-versicolor"+'*****'*3)
print(frames[1].describe())
print('\n'+'*****'*3+"Iris-virginica"+'*****'*3)
print(frames[2].describe())
'''
Findings:
Avg values of Iris-setosa is more only in sepalwidth in comparison to other varities,
Although Avg sepalLW of versicolor > virginica, the avg petalLW of versicolor < virginica,

based on std dev,
setosa has lesser value than others in 
sepal length, petal width, petal length
meaning most of them are near mean length

similarly: versicolor for sepal width

samples taken for virginica have most variation 
in the measured characteristics

'''
'''
Output:

***************percentile***************
{
    "Iris-setosa": {
        "SepalLengthCm": {
            "10": 4.59,
            "20": 4.7,
            "30": 4.8,
            "40": 4.96,
            "50": 5.0,
            "60": 5.1,
            "70": 5.1,
            "80": 5.32,
            "90": 5.41
        },
        "SepalWidthCm": {
            "10": 3.0,
            "20": 3.1,
            "30": 3.2,
            "40": 3.3600000000000003,
            "50": 3.4,
            "60": 3.5,
            "70": 3.53,
            "80": 3.7200000000000006,
            "90": 3.9
        },
        "PetalLengthCm": {
            "10": 1.3,
            "20": 1.3,
            "30": 1.4,
            "40": 1.4,
            "50": 1.5,
            "60": 1.5,
            "70": 1.5,
            "80": 1.6,
            "90": 1.7
        },
        "PetalWidthCm": {
            "10": 0.1,
            "20": 0.2,
            "30": 0.2,
            "40": 0.2,
            "50": 0.2,
            "60": 0.2,
            "70": 0.3,
            "80": 0.3,
            "90": 0.4
        }
    },
    "Iris-versicolor": {
        "SepalLengthCm": {
            "10": 5.38,
            "20": 5.5,
            "30": 5.6,
            "40": 5.7,
            "50": 5.9,
            "60": 6.039999999999999,
            "70": 6.2,
            "80": 6.4,
            "90": 6.7
        },
        "SepalWidthCm": {
            "10": 2.3,
            "20": 2.5,
            "30": 2.6,
            "40": 2.7,
            "50": 2.8,
            "60": 2.9,
            "70": 3.0,
            "80": 3.0,
            "90": 3.1100000000000003
        },
        "PetalLengthCm": {
            "10": 3.5900000000000003,
            "20": 3.9,
            "30": 4.0,
            "40": 4.2,
            "50": 4.35,
            "60": 4.5,
            "70": 4.5,
            "80": 4.7,
            "90": 4.8
        },
        "PetalWidthCm": {
            "10": 1.0,
            "20": 1.1800000000000002,
            "30": 1.27,
            "40": 1.3,
            "50": 1.3,
            "60": 1.4,
            "70": 1.4299999999999997,
            "80": 1.5,
            "90": 1.5100000000000002
        }
    },
    "Iris-virginica": {
        "SepalLengthCm": {
            "10": 5.8,
            "20": 6.1,
            "30": 6.3,
            "40": 6.4,
            "50": 6.5,
            "60": 6.699999999999999,
            "70": 6.83,
            "80": 7.2,
            "90": 7.61
        },
        "SepalWidthCm": {
            "10": 2.5900000000000003,
            "20": 2.7,
            "30": 2.8,
            "40": 2.9,
            "50": 3.0,
            "60": 3.0,
            "70": 3.1,
            "80": 3.2,
            "90": 3.31
        },
        "PetalLengthCm": {
            "10": 4.9,
            "20": 5.1,
            "30": 5.1,
            "40": 5.36,
            "50": 5.55,
            "60": 5.6,
            "70": 5.8,
            "80": 6.0,
            "90": 6.3100000000000005
        },
        "PetalWidthCm": {
            "10": 1.7900000000000003,
            "20": 1.8,
            "30": 1.7999999999999998,
            "40": 1.9,
            "50": 2.0,
            "60": 2.1,
            "70": 2.2,
            "80": 2.3,
            "90": 2.4
        }
    }
}

***************Iris-setosa***************
             Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
count  50.00000       50.00000     50.000000      50.000000      50.00000
mean   25.50000        5.00600      3.418000       1.464000       0.24400
std    14.57738        0.35249      0.381024       0.173511       0.10721
min     1.00000        4.30000      2.300000       1.000000       0.10000
25%    13.25000        4.80000      3.125000       1.400000       0.20000
50%    25.50000        5.00000      3.400000       1.500000       0.20000
75%    37.75000        5.20000      3.675000       1.575000       0.30000
max    50.00000        5.80000      4.400000       1.900000       0.60000

***************Iris-versicolor***************
              Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
count   50.00000      50.000000     50.000000      50.000000     50.000000
mean    75.50000       5.936000      2.770000       4.260000      1.326000
std     14.57738       0.516171      0.313798       0.469911      0.197753
min     51.00000       4.900000      2.000000       3.000000      1.000000
25%     63.25000       5.600000      2.525000       4.000000      1.200000
50%     75.50000       5.900000      2.800000       4.350000      1.300000
75%     87.75000       6.300000      3.000000       4.600000      1.500000
max    100.00000       7.000000      3.400000       5.100000      1.800000

***************Iris-virginica***************
              Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
count   50.00000       50.00000     50.000000      50.000000      50.00000
mean   125.50000        6.58800      2.974000       5.552000       2.02600
std     14.57738        0.63588      0.322497       0.551895       0.27465
min    101.00000        4.90000      2.200000       4.500000       1.40000
25%    113.25000        6.22500      2.800000       5.100000       1.80000
50%    125.50000        6.50000      3.000000       5.550000       2.00000
75%    137.75000        6.90000      3.175000       5.875000       2.30000
max    150.00000        7.90000      3.800000       6.900000       2.50000

Process finished with exit code 0

'''