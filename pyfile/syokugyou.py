import pandas as pd

paths = [
    "C:\pwork\csvfile\List of architects.csv",
    "C:\pwork\csvfile\List of astronauts.csv",
    "C:\pwork\csvfile\List of chemist.csv",
    "C:\pwork\csvfile\List of chessplayer.csv",
    "C:\pwork\csvfile\List of classical pianists.csv",
    "C:\pwork\csvfile\List of composers.csv",
    "C:\pwork\csvfile\List of Computer.csv",
    "C:\pwork\csvfile\List of dancers.csv",
    "C:\pwork\csvfile\List of economist.csv",
    "C:\pwork\csvfile\List of English writers.csv",
    "C:\pwork\csvfile\List of female golfers.csv",
    "C:\pwork\csvfile\List of female tennisplayers.csv",
    "C:\pwork\csvfile\List of film and television directors.csv",
    "C:\pwork\csvfile\List of FormulaOnedrivers.csv",
    "C:\pwork\csvfile\List of inventors.csv",
    "C:\pwork\csvfile\List of magicians.csv",
    "C:\pwork\csvfile\List of male golfers.csv",
    "C:\pwork\csvfile\List of male singles tennisplayers.csv",
    "C:\pwork\csvfile\List of math.csv",
    "C:\pwork\csvfile\List of painters.csv",
    "C:\pwork\csvfile\List of philosophers.csv",
    "C:\pwork\csvfile\List of physicians.csv",
    "C:\pwork\csvfile\List of physicists.csv",
    "C:\pwork\csvfile\List of snookerplayers.csv",
]

def getOccupation(filepath):
    df = pd.read_csv(filepath)
    df['zhiye'] = filepath.split(' ')[-1][:-4]
    return df

def checkerr(df,s):
    errorco = []
    a = list(df.columns)  
    b = list(s.columns)
    zijicolu = list(set(a) & set(b))
    for i in zijicolu:
        if df[i].dtype != s[i].dtype:
            print(i)
            errorco.append(i)
    for co in errorco:
        s[co] = s[co].astype('object')
        df[co] = df[co].astype('object')
    return df, s


df = getOccupation(paths[0])
# df = pd.read_csv(paths[0])
# df.shape
for path in paths:
    newone = getOccupation(path)
    df, newone = checkerr(df, newone)
    df = pd.merge(df, newone, how = 'outer')

df.to_csv("mergedataxingzuo.csv")
# getOccupation(paths[1])['zhiye']
# df.shape
len(df['zhiye'].unique())
len(paths)
s = getOccupation(paths[3])
pd.merge(df, s, how = 'outer')

# df['zhiye'].isnull().sum()
# df2 = df
# df2
# df
# a = list(df.columns)  
# b = list(s.columns)
# zijicolu = list(set(a) & set(b))
# df[zijicolu[0]].dtype == s[zijicolu[0]].dtype
# s['Date of birth'].astype('object')
# df['Date of birth'].astype('object')
# s['Date of birth']
# df['Date of birth']
# 'Full name' in list(df.columns)
# for i in zijicolu:
#     if df[i].dtype != s[i].dtype:
#         print(f'{i}:{df[i].dtype},{s[i].dtype}')

df.columns
df1 = df.drop('Unnamed: 0', axis=1)
df1.columns
df1.dropna(axis=0, how='all', inplace=True)
df1.shape
df1 = df1.drop_duplicates(subset='name')
df1.shape

import copy
df2 = copy.deepcopy(df1)
df2['Born']
df2['Born'] = df2['Born'].str.extract('(\d[7-9]\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]))')
df2['Born'].isnull().sum()
# list(df2['Born'].unique())
df3 = df2[~df2['Born'].isnull()]
df4 = df3[['name', 'Born', 'zhiye']]
df4['Born'].isin(['1999-01-01'])
# df4 = df4[~df4['Born'].isin(['1788-11-00', '1494-03-24', '1604-03-10'])]
df4['Born'] = pd.to_datetime(df4['Born'])
df4.to_csv('namedatezhiye.csv')
# df4.set_index('Born', inplace=True)
# df4.reset_index(inplace=True)
# df4.Born.dt.to_period()
# df4.Born
# df4.Born.dt.month
# df4.Born.dt.day
# pd.PeriodIndex(month=df4.Born.dt.month, day=df4.Born.dt.month, freq="D")
# aa = df4.Born.dt.month.astype('str')
# bb = df4.Born.dt.day.astype('str')
# df4['md'] = aa.str.cat(bb, sep=',')
# df4.drop('xingzuo', axis=1, inplace=True)
df4 = pd.read_csv('namedatezhiye.csv')
df4
df4['Born'] = pd.to_datetime(df4['Born'])
df4['month'] = df4.Born.dt.month
df4['day'] = df4.Born.dt.day

def cal_constellation(month, day):
    constellation = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
    start_day = ((1,20), (2,19), (3,21), (4,21), (5,21), (6,22), (7,23), (8,23), (9,23), (10,23), (11,23), (12,23))
    return constellation[len(list(filter(lambda y:y<=(month,day), start_day)))%12]

# df4['md'][0]
import numpy as np
df4['xingzuo'] = np.nan
for i in range(df4.shape[0]):
    df4['xingzuo'][i] = cal_constellation(df4['month'][i], df4['day'][i]) 

df4['xingzuo']
# 统计星座人数
df4.groupby("xingzuo")[['name']].count()
# 统计职业人数
df4.groupby("zhiye")[['name']].count()
# 星座职业交叉人数
table1 = df4.groupby(['xingzuo', 'zhiye'])[['name']].count().unstack()
# table1.to_csv('table1.csv', encoding='utf-8_sig')
table1

ss = {
    "Computer":1,
    "FormulaOnedrivers":3,
    "architects":2,
    "astronauts":4,
    "chemist":1,
    "chessplayer":3,
    "composers":2,
    "dancers":3,
    "directors":2,
    "economist":1,
    "golfers":3,
    "inventors":1,
    "magicians":2,
    "math":1,
    "painters":2,
    "philosophers":1,
    "physicians":1,
    "physicists":1,
    "pianists":2,
    "snookerplayers":3,
    "tennisplayers":3,
    "writers":2,
}
# ss[df['zhiye'][5]]
df4['type'] = np.nan
for i in range(df4.shape[0]):
    df4['type'][i] = ss[df4['zhiye'][i]]

df4['type'].isnull().sum()
df4['type'].unique()

from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
enc.fit(df4['zhiye'])
df4['zy'] = enc.transform(df4['zhiye'])
df4['zy']
enc2 = LabelEncoder()
enc2.fit(df4['xingzuo'])
df4['xz'] = enc2.transform(df4['xingzuo'])
df4['xingzuo'].unique()
# from collections import Counter
# len(df4['zhiye'].unique())
# Counter(enc.transform(df4['zhiye']))
df4[['zy', 'type', 'xz']].corr()
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df4[['xz']], df4['zhiye'])
tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train))) 
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))

X0 = pd.get_dummies(df4[['xingzuo']])
# X0.corr().to_csv('xiangguanzhiye.csv', encoding='utf-8_sig')
X_train, X_test, y_train, y_test = train_test_split(X0, df4['zhiye'])
tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(tree.score(X_train, y_train))) 
print("Accuracy on test set: {:.3f}".format(tree.score(X_test, y_test)))

# from sklearn.cluster import AgglomerativeClustering
# agg = AgglomerativeClustering(n_clusters=3)
# X1 = pd.get_dummies(df4['xingzuo'])

agg.fit_predict(X1)

# ----
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, ward 
 
X, y = make_blobs(random_state=0, n_samples=12) # 将ward聚类应用于数据数组X 
# SciPy的ward函数返回一个数组，指定执行凝聚聚类时跨越的距离
X
linkage_array = ward(X)
# 现在为包含簇之间距离的linkage_array绘制树状图 
dendrogram(linkage_array)
# plt.show()
import matplotlib.pyplot as plt
ax = plt.gca()
bounds = ax.get_xbound() 
ax.plot(bounds, [7.25, 7.25], '--', c='k') 
ax.plot(bounds, [4, 4], '--', c='k') 
 
ax.text(bounds[1], 7.25, ' two clusters', va='center', fontdict={'size': 15}) 
ax.text(bounds[1], 4, ' three clusters', va='center', fontdict={'size': 15}) 
plt.xlabel("Sample index") 
plt.ylabel("Cluster distance")
plt.show()
# 在树中标记划分成两个簇或三个簇的位置 ax = plt.gca() 
# ----
xx = np.array(X1)
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, ward 
linkage_array = ward(xx)
