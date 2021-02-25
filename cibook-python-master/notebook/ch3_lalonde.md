```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors

import warnings
warnings.filterwarnings('ignore')
```

## (3)NBER archiveからデータを読み込む


```python
cps1_data = pd.read_stata('https://users.nber.org/~rdehejia/data/cps_controls.dta')
cps3_data = pd.read_stata('https://users.nber.org/~rdehejia/data/cps_controls3.dta')
nswdw_data = pd.read_stata('https://users.nber.org/~rdehejia/data/nsw_dw.dta')
```

## (4)データセットの準備


```python
cps1_nsw_data = pd.concat([nswdw_data[nswdw_data.treat == 1], cps1_data], ignore_index=True)
cps3_nsw_data = pd.concat([nswdw_data[nswdw_data.treat == 1], cps3_data], ignore_index=True)
```

## (5) RCT データでの分析


```python
## 共変量なしの回帰分析
y = nswdw_data.re78
X = nswdw_data.treat
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
coef = results.summary().tables[1]
coef
```




<table class="simpletable">
<tr>
    <td></td>       <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th> <td> 4554.8011</td> <td>  408.046</td> <td>   11.162</td> <td> 0.000</td> <td> 3752.855</td> <td> 5356.747</td>
</tr>
<tr>
  <th>treat</th> <td> 1794.3424</td> <td>  632.853</td> <td>    2.835</td> <td> 0.005</td> <td>  550.574</td> <td> 3038.110</td>
</tr>
</table>




```python
## 共変量付きの回帰分析
y = nswdw_data.re78
X = nswdw_data[['treat', 're74', 're75', 'age', 'education', 'black', 'hispanic', 'nodegree', 'married']]
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
coef = results.summary().tables[1]
coef = pd.read_html(coef.as_html(), header=0, index_col=0)[0]
pd.DataFrame(coef.loc['treat']).T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>coef</th>
      <th>std err</th>
      <th>t</th>
      <th>P&gt;|t|</th>
      <th>[0.025</th>
      <th>0.975]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>treat</th>
      <td>1676.3426</td>
      <td>638.682</td>
      <td>2.625</td>
      <td>0.009</td>
      <td>421.056</td>
      <td>2931.629</td>
    </tr>
  </tbody>
</table>
</div>



## (6) バイアスのあるデータでの回帰分析


```python
## CPS1の分析結果
y = cps1_nsw_data.re78
X = cps1_nsw_data[['treat', 're74', 're75', 'age', 'education', 'black', 'hispanic', 'nodegree', 'married']]
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
coef = results.summary().tables[1]
coef = pd.read_html(coef.as_html(), header=0, index_col=0)[0]
pd.DataFrame(coef.loc['treat']).T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>coef</th>
      <th>std err</th>
      <th>t</th>
      <th>P&gt;|t|</th>
      <th>[0.025</th>
      <th>0.975]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>treat</th>
      <td>699.1317</td>
      <td>547.636</td>
      <td>1.277</td>
      <td>0.202</td>
      <td>-374.296</td>
      <td>1772.559</td>
    </tr>
  </tbody>
</table>
</div>




```python
## CPS3の分析結果
y = cps3_nsw_data.re78
X = cps3_nsw_data[['treat', 're74', 're75', 'age', 'education', 'black', 'hispanic', 'nodegree', 'married']]
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
coef = results.summary().tables[1]
coef = pd.read_html(coef.as_html(), header=0, index_col=0)[0]
pd.DataFrame(coef.loc['treat']).T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>coef</th>
      <th>std err</th>
      <th>t</th>
      <th>P&gt;|t|</th>
      <th>[0.025</th>
      <th>0.975]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>treat</th>
      <td>1548.2438</td>
      <td>781.279</td>
      <td>1.982</td>
      <td>0.048</td>
      <td>13.89</td>
      <td>3082.598</td>
    </tr>
  </tbody>
</table>
</div>



## (7) 傾向スコアマッチングによる効果推定


```python
def get_matched_dfs_using_propensity_score(X, y, random_state=0):
    # 傾向スコアを計算する
    ps_model = LogisticRegression(solver='lbfgs', random_state=random_state).fit(X, y)
    ps_score = ps_model.predict_proba(X)[:, 1]
    all_df = pd.DataFrame({'treatment': y, 'ps_score': ps_score})
    treatments = all_df.treatment.unique()
    if len(treatments) != 2:
        print('2群のマッチングしかできません。2群は必ず[0, 1]で表現してください。')
        raise ValueError
    # treatment == 1をgroup1, treatment == 0をgroup2とする。group1にマッチするgroup2を抽出するのでATTの推定になるはず
    group1_df = all_df[all_df.treatment==1].copy()
    group1_indices = group1_df.index
    group1_df = group1_df.reset_index(drop=True)
    group2_df = all_df[all_df.treatment==0].copy()
    group2_indices = group2_df.index
    group2_df = group2_df.reset_index(drop=True)

    # 全体の傾向スコアの標準偏差 * 0.2をしきい値とする
    threshold = all_df.ps_score.std() * 0.2

    matched_group1_dfs = []
    matched_group2_dfs = []
    _group1_df = group1_df.copy()
    _group2_df = group2_df.copy()

    while True:
        # NearestNeighborsで最近傍点1点を見つけ、マッチングする
        neigh = NearestNeighbors(n_neighbors=1)
        neigh.fit(_group1_df.ps_score.values.reshape(-1, 1))
        distances, indices = neigh.kneighbors(_group2_df.ps_score.values.reshape(-1, 1))
        # 重複点を削除する
        distance_df = pd.DataFrame({'distance': distances.reshape(-1), 'indices': indices.reshape(-1)})
        distance_df.index = _group2_df.index
        distance_df = distance_df.drop_duplicates(subset='indices')
        # しきい値を超えたレコードを削除する
        distance_df = distance_df[distance_df.distance < threshold]
        if len(distance_df) == 0:
            break
        # マッチングしたレコードを抽出、削除する
        group1_matched_indices = _group1_df.iloc[distance_df['indices']].index.tolist()
        group2_matched_indices = distance_df.index
        matched_group1_dfs.append(_group1_df.loc[group1_matched_indices])
        matched_group2_dfs.append(_group2_df.loc[group2_matched_indices])
        _group1_df = _group1_df.drop(group1_matched_indices)
        _group2_df = _group2_df.drop(group2_matched_indices)

    # マッチしたレコードを返す
    group1_df.index = group1_indices
    group2_df.index = group2_indices
    matched_df = pd.concat([
        group1_df.iloc[pd.concat(matched_group1_dfs).index],
        group2_df.iloc[pd.concat(matched_group2_dfs).index]
    ]).sort_index()
    matched_indices = matched_df.index

    return X.loc[matched_indices], y.loc[matched_indices]
```


```python
X = cps1_nsw_data[['age', 'education', 'black', 'hispanic', 'nodegree', 'married', 're74', 're75']]
# 元のソースコードでは入れてるが、入れるとマッチング数が減って推定結果もおかしくなるのでやらない
#X['re74_2'] = X.re74 ** 2
#X['re75_2'] = X.re75 ** 2
y = cps1_nsw_data['treat']
matchX, matchy = get_matched_dfs_using_propensity_score(X, y)
```


```python
# マッチング後のデータ作成
matched_data = cps1_nsw_data.loc[matchX.index]
# マッチング後のデータで効果の推定
y = matched_data.re78
X = matched_data[['treat']]
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
coef = results.summary().tables[1]
coef = pd.read_html(coef.as_html(), header=0, index_col=0)[0]
pd.DataFrame(coef.loc['treat']).T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>coef</th>
      <th>std err</th>
      <th>t</th>
      <th>P&gt;|t|</th>
      <th>[0.025</th>
      <th>0.975]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>treat</th>
      <td>332.7242</td>
      <td>825.766</td>
      <td>0.403</td>
      <td>0.687</td>
      <td>-1291.97</td>
      <td>1957.418</td>
    </tr>
  </tbody>
</table>
</div>



結構下振れしている。マッチングアルゴリズムがあまり良くないかも。p-valueも大きい。  
色々（共変量の選択や、ロジスティック回帰の手法など）を変えて色々試すと分かるが、効果の推定結果のブレが大きい。

### 共変量のバランスを確認


```python
def calc_absolute_mean_difference(df):
    # (treatment群の平均 - control群の平均) / 全体の標準誤差
    return ((df[df.treat==1].drop('treat', axis=1).mean() - df[df.treat==0].drop('treat', axis=1).mean()) \
            / df.drop('treat', axis=1).std()).abs()

## 調整前のAbsolute Mean Difference
unadjusted_df = cps1_nsw_data[['treat', 'age', 'education', 'black', 'hispanic', 'nodegree', 'married', 're74', 're75']]
unadjusted_amd = calc_absolute_mean_difference(unadjusted_df)

# 傾向スコアマッチング後のAbusolute Mean Difference
after_matching_df = cps1_nsw_data.loc[matchX.index][['treat', 'age', 'education', 'black', 'hispanic', 'nodegree', 'married', 're74', 're75']]
after_matching_amd = calc_absolute_mean_difference(after_matching_df)
```


```python
balance_df = pd.concat([
    pd.DataFrame({'Absolute Mean Difference': unadjusted_amd, 'Sample': 'Unadjusted'}),
    pd.DataFrame({'Absolute Mean Difference': after_matching_amd, 'Sample': 'Adjusted'})
])
fig = px.scatter(balance_df, x='Absolute Mean Difference', y=balance_df.index, color='Sample',
                title='3.9 マッチングの共変量のバランス')
fig.show()
```




```python
fig.write_html('../images/ch3_plot4.html', auto_open=False)
```

## (8) IPWによる効果推定


```python
def get_ipw(X, y, random_state=0):
    # 傾向スコアを計算する
    ps_model = LogisticRegression(solver='lbfgs', random_state=random_state).fit(X, y)
    ps_score = ps_model.predict_proba(X)[:, 1]
    all_df = pd.DataFrame({'treatment': y, 'ps_score': ps_score})
    treatments = all_df.treatment.unique()
    if len(treatments) != 2:
        print('2群のマッチングしかできません。2群は必ず[0, 1]で表現してください。')
        raise ValueError
    # treatment == 1をgroup1, treatment == 0をgroup2とする。
    group1_df = all_df[all_df.treatment==1].copy()
    group2_df = all_df[all_df.treatment==0].copy()
    group1_df['weight'] = 1 / group1_df.ps_score
    group2_df['weight'] = 1 / (1 - group2_df.ps_score)
    weights = pd.concat([group1_df, group2_df]).sort_index()['weight'].values
    return weights
```


```python
X = cps1_nsw_data[['age', 'education', 'black', 'hispanic', 'nodegree', 'married', 're74', 're75']]
y = cps1_nsw_data['treat']
weights = get_ipw(X, y)
```


```python
## 重み付きデータでの効果の推定
y = cps1_nsw_data.re78
X = cps1_nsw_data.treat
X = sm.add_constant(X)
results = sm.WLS(y, X, weights=weights).fit()
coef = results.summary().tables[1]
coef
```




<table class="simpletable">
<tr>
    <td></td>       <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th> <td> 1.474e+04</td> <td>   82.771</td> <td>  178.071</td> <td> 0.000</td> <td> 1.46e+04</td> <td> 1.49e+04</td>
</tr>
<tr>
  <th>treat</th> <td>-7772.9662</td> <td>  144.131</td> <td>  -53.930</td> <td> 0.000</td> <td>-8055.479</td> <td>-7490.453</td>
</tr>
</table>



### 共変量のバランスを確認


```python
# IPWで重み付け後のAbusolute Mean Difference
# 重みのぶんレコードを増やして計算する（もっといいやり方を知りたい）
after_weighted_df = cps1_nsw_data.loc[matchX.index][['treat', 'age', 'education', 'black', 'hispanic', 'nodegree', 'married', 're74', 're75']]
weights_int = (weights * 100).astype(int)
weighted_df = []
for i, value in enumerate(after_weighted_df.values):
    weighted_df.append(np.tile(value, (weights_int[i], 1)))
weighted_df = np.concatenate(weighted_df).reshape(-1, 9)
weighted_df = pd.DataFrame(weighted_df)
weighted_df.columns = after_weighted_df.columns
after_weighted_amd = calc_absolute_mean_difference(weighted_df)
```


```python
balance_df = pd.concat([
    pd.DataFrame({'Absolute Mean Difference': unadjusted_amd, 'Sample': 'Unadjusted'}),
    pd.DataFrame({'Absolute Mean Difference': after_weighted_amd, 'Sample': 'Adjusted'})
])
fig = px.scatter(balance_df, x='Absolute Mean Difference', y=balance_df.index, color='Sample',
                title='3.10 マッチングの共変量のバランス')
fig.show()
```





```python
fig.write_html('../images/ch3_plot5.html', auto_open=False)
```
