from math import *
import pandas as pd
import matplotlib.pyplot as plt

d=pd.read_csv("nba.csv")
df=pd.DataFrame(d,columns=["Age","Weight","Salary"])

df.dropna(inplace=True)


print(df.describe())
dfage=[] # age from 19 to 40
for i in [19,26,34]:
    dfage.append(df[(df['Age']>=i) & (df['Age']<i+7)])

# dfweight=[] # weight from 161 to 279
# for i in [161,201,242]:
#     dfweight.append(df[(df['Weight']>=i) & (df['Weight']<i+40)])


for i in range(3):
    print(f'\nAge group: {dfage[i]["Age"].min()} to {dfage[i]["Age"].max()}')
    print(dfage[i]['Salary'].describe())
    plt.scatter(dfage[i]['Age'],dfage[i]['Salary'])
    plt.savefig(f'Age group'+str(i)+'.png')
    plt.close()
plt.scatter(df['Age'],df['Salary'])
plt.savefig(f'Age group total.png')
plt.close()

# for i in range(3):
#     print(f'\nWeight group: {dfweight[i]["Weight"].min()} to {dfweight[i]["Weight"].max()}')
#     print(dfweight[i]['Salary'].describe())
#     plt.scatter(dfweight[i]['Weight'],dfweight[i]['Salary'])
#     plt.savefig(f'Weight group'+str(i)+'.png')
#     plt.close()
#
# plt.scatter(df['Weight'],df['Salary'])
# plt.savefig(f'Weight group total.png')
# plt.close()

'''
Output:
              Age      Weight        Salary
count  446.000000  446.000000  4.460000e+02
mean    26.919283  221.753363  4.842684e+06
std      4.398951   26.157899  5.229238e+06
min     19.000000  161.000000  3.088800e+04
25%     24.000000  200.000000  1.044792e+06
50%     26.000000  220.000000  2.839073e+06
75%     30.000000  240.000000  6.500000e+06
max     40.000000  307.000000  2.500000e+07

Age group: 19 to 25
count    1.940000e+02
mean     2.983969e+06
std      3.569683e+06
min      3.088800e+04
25%      9.472760e+05
50%      1.623120e+06
75%      3.251517e+06
max      1.640750e+07
Name: Salary, dtype: float64

Age group: 26 to 32
count    1.980000e+02
mean     6.742684e+06
std      5.980729e+06
min      5.572200e+04
25%      1.480830e+06
50%      5.000000e+06
75%      1.041208e+07
max      2.297050e+07
Name: Salary, dtype: float64

Age group: 34 to 40
count    4.000000e+01
mean     4.771635e+06
std      5.112349e+06
min      2.228880e+05
25%      9.476135e+05
50%      3.459250e+06
75%      5.692870e+06
max      2.500000e+07
Name: Salary, dtype: float64

Process finished with exit code 0

'''