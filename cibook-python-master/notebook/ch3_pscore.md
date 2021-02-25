```python
import pandas as pd
import os
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from tqdm import tqdm_notebook
import plotly.express as px
import plotly.graph_objects as go
import random
import numpy as np
import warnings
warnings.filterwarnings('ignore')
```

## (3) データの読み込み


```python
dumped_male_df_path = '../data/male_df.joblib'
dumped_biased_df_path = '../data/biased_df.joblib'

if os.path.exists(dumped_male_df_path):
    male_df = joblib.load(dumped_male_df_path)
    biased_df = joblib.load(dumped_biased_df_path)
else:
    # セレクションバイアスのあるデータの作成
    mail_df = pd.read_csv('http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv')
    ### 女性向けメールが配信されたデータを削除したデータを作成
    male_df = mail_df[mail_df.segment != 'Womens E-Mail'].copy() # 女性向けメールが配信されたデータを削除
    male_df['treatment'] = male_df.segment.apply(lambda x: 1 if x == 'Mens E-Mail' else 0) #介入を表すtreatment変数を追加
    ## バイアスのあるデータの作成
    sample_rules = (male_df.history > 300) | (male_df.recency < 6) | (male_df.channel=='Multichannel')
    biased_df = pd.concat([
        male_df[(sample_rules) & (male_df.treatment == 0)].sample(frac=0.5, random_state=1),
        male_df[(sample_rules) & (male_df.treatment == 1)],
        male_df[(~sample_rules) & (male_df.treatment == 0)],
        male_df[(~sample_rules) & (male_df.treatment == 1)].sample(frac=0.5, random_state=1)
    ], axis=0, ignore_index=True)
```

## (6) 傾向スコアの推定



```python
y = biased_df['treatment']
X = pd.get_dummies(biased_df[['recency', 'channel', 'history']], columns=['channel'], drop_first=True)

ps_model = LogisticRegression(solver='lbfgs').fit(X, y)
```

## (7) 傾向スコアマッチング

### 番外編：確認のため、MatchItによるマッチング結果を見る
事前準備
```
sudo R
>install.packages("MatchIt")
>install.packages("Matching")
```


```python
from rpy2.robjects import r, pandas2ri, globalenv
from rpy2.robjects.packages import importr
pandas2ri.activate()
matchit = importr('MatchIt')
```


```python
biased_df.head(5)
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
      <th>recency</th>
      <th>history_segment</th>
      <th>history</th>
      <th>mens</th>
      <th>womens</th>
      <th>zip_code</th>
      <th>newbie</th>
      <th>channel</th>
      <th>segment</th>
      <th>visit</th>
      <th>conversion</th>
      <th>spend</th>
      <th>treatment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>5) $500 - $750</td>
      <td>572.65</td>
      <td>1</td>
      <td>0</td>
      <td>Urban</td>
      <td>1</td>
      <td>Web</td>
      <td>No E-Mail</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>1) $0 - $100</td>
      <td>42.38</td>
      <td>1</td>
      <td>0</td>
      <td>Urban</td>
      <td>1</td>
      <td>Phone</td>
      <td>No E-Mail</td>
      <td>1</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>7) $1,000 +</td>
      <td>3003.48</td>
      <td>1</td>
      <td>1</td>
      <td>Urban</td>
      <td>1</td>
      <td>Phone</td>
      <td>No E-Mail</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>5) $500 - $750</td>
      <td>662.10</td>
      <td>0</td>
      <td>1</td>
      <td>Urban</td>
      <td>1</td>
      <td>Web</td>
      <td>No E-Mail</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1) $0 - $100</td>
      <td>44.37</td>
      <td>0</td>
      <td>1</td>
      <td>Urban</td>
      <td>0</td>
      <td>Web</td>
      <td>No E-Mail</td>
      <td>0</td>
      <td>0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
r_biased_df = pandas2ri.py2rpy(biased_df)
globalenv['r_biased_df'] = r_biased_df
```


```python
r('set.seed(1)')
```




    <rpy2.rinterface_lib.sexp.NULLType object at 0x000002136AFE8340> [RTYPES.NILSXP]




```python
m_near = r('m_near <- matchit(formula = treatment ~ recency + history + channel,data = r_biased_df,method = "nearest",replace = TRUE)')
```

    R[write to console]: Warning:
    R[write to console]:  Fewer control units than treated units; not all treated units will get a match.


​    


```python
matched_data = r('matched_data <- match.data(m_near)')
```


```python
matched_data.shape
```




    (24328, 15)




```python
biased_df.treatment.value_counts()
```




    1    17168
    0    14757
    Name: treatment, dtype: int64



マッチング後の件数が、treatment = 0　の件数 * 2より少ないので、おそらく一定のしきい値を設けて近傍点をマッチングしている


```python
## マッチング後のデータで効果の推定
y = matched_data.spend
X = matched_data.treatment
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
coef = results.summary().tables[1]
coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.5734</td> <td>    0.198</td> <td>    2.900</td> <td> 0.004</td> <td>    0.186</td> <td>    0.961</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.9683</td> <td>    0.235</td> <td>    4.114</td> <td> 0.000</td> <td>    0.507</td> <td>    1.430</td>
</tr>
</table>



### 追加実験：seedを変えて10回実行し、treatmentのcoefの分布を確認する
std err分かってるから不要だったかも


```python
coefs = []
for i in tqdm_notebook(range(10)):
    r(f"set.seed({i})")
    m_near = r('m_near <- matchit(formula = treatment ~ recency + history + channel,data = r_biased_df,method = "nearest",replace = TRUE)')
    matched_data = r('matched_data <- match.data(m_near)')
    ## マッチング後のデータで効果の推定
    y = matched_data.spend
    X = matched_data.treatment
    X = sm.add_constant(X)
    results = sm.OLS(y, X).fit()
    coef = results.params.loc['treatment']
    print(f'iter: {i}, coef: {coef}')
    coefs.append(coef)
```


    HBox(children=(FloatProgress(value=0.0, max=10.0), HTML(value='')))    
    
    iter: 0, coef: 0.9682903433437239
    
    iter: 1, coef: 0.9682903433437239
    
    iter: 2, coef: 0.9682903433437239
    
    iter: 3, coef: 0.9682903433437239
    
    iter: 4, coef: 0.9682903433437239
    
    iter: 5, coef: 0.9682903433437239
    
    iter: 6, coef: 0.9682903433437239
    
    iter: 7, coef: 0.9682903433437239
    
    iter: 8, coef: 0.9682903433437239
    
    iter: 9, coef: 0.9682903433437239


​    


```python
fig = px.violin(pd.DataFrame({'coef': coefs}), y='coef', box=True, points='all',
                title='MatchItによる傾向スコアマッチング後のtreatmentの効果分布')
fig.show()
```

```python
fig.write_html('../images/ch3_plot0.html', auto_open=False)
```

### Pythonでの実装


```python
y = biased_df['treatment']
X = pd.get_dummies(biased_df[['recency', 'channel', 'history']], columns=['channel'], drop_first=True)

```


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
matchX, matchy = get_matched_dfs_using_propensity_score(X, y)
```


```python
## マッチング後のデータで効果の推定
y = biased_df.loc[matchX.index].spend
X = matchy
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
coef = results.summary().tables[1]
coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.6214</td> <td>    0.143</td> <td>    4.331</td> <td> 0.000</td> <td>    0.340</td> <td>    0.903</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.8160</td> <td>    0.203</td> <td>    4.021</td> <td> 0.000</td> <td>    0.418</td> <td>    1.214</td>
</tr>
</table>



## seedを変えて10回実行し、treatmentのcoefの分布を確認する


```python
coefs_py = []
for i in tqdm_notebook(range(10)):
    random.seed(i)
    os.environ['PYTHONHASHSEED'] = str(i)
    np.random.seed(i)
    y = biased_df['treatment']
    X = pd.get_dummies(biased_df[['recency', 'channel', 'history']], columns=['channel'], drop_first=True)
    matchX, matchy = get_matched_dfs_using_propensity_score(X, y, random_state=i)
    y = biased_df.loc[matchX.index].spend
    X = matchy
    X = sm.add_constant(X)
    results = sm.OLS(y, X).fit()
    coef = results.params.loc['treatment']
    print(f'iter: {i}, coef: {coef}')
    coefs_py.append(coef)
```


    HBox(children=(FloatProgress(value=0.0, max=10.0), HTML(value='')))


    iter: 0, coef: 0.8159872667015613
    iter: 1, coef: 0.8159872667015613
    iter: 2, coef: 0.8159872667015613
    iter: 3, coef: 0.8159872667015613
    iter: 4, coef: 0.8159872667015613
    iter: 5, coef: 0.8159872667015613
    iter: 6, coef: 0.8159872667015613
    iter: 7, coef: 0.8159872667015613
    iter: 8, coef: 0.8159872667015613
    iter: 9, coef: 0.8159872667015613


​    

seedを変えても結果は変わらず。。。  
MatchItの結果と比較してやや下振れだが、0.8088+-0.203のためMatchItでの計算結果と大きな乖離があるとは言えない

## (8) 逆確率重み付き推定（IPW）

### 番外編：確認のため、WeightItによる重み付け後の結果を見る
事前準備
```
sudo R
>install.packages("WeightIt")
```


```python
pandas2ri.activate()
weightit = importr('WeightIt')
r_biased_df = pandas2ri.py2rpy(biased_df)
globalenv['r_biased_df'] = r_biased_df
r('set.seed(1)')
## 重みの推定
weighting = r('weighting <- weightit(treatment ~ recency + history + channel,data = r_biased_df,method = "ps",estimand = "ATE")')
```


```python
weighting[0]
```




    array([ 2.04296482,  2.10622021, 11.42858518, ...,  2.86301808,
            2.76930772,  2.95534326])




```python
## 重み付きデータでの効果の推定
y = biased_df.spend
X = biased_df.treatment
X = sm.add_constant(X)
results = sm.WLS(y, X, weights=weighting[0]).fit()
coef = results.summary().tables[1]
coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.5903</td> <td>    0.120</td> <td>    4.920</td> <td> 0.000</td> <td>    0.355</td> <td>    0.825</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.8856</td> <td>    0.170</td> <td>    5.203</td> <td> 0.000</td> <td>    0.552</td> <td>    1.219</td>
</tr>
</table>



## Pythonで実装


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
y = biased_df['treatment']
X = pd.get_dummies(biased_df[['recency', 'channel', 'history']], columns=['channel'], drop_first=True)
weights = get_ipw(X, y)
```


```python
weights
```




    array([ 2.04325576,  2.10624393, 11.44468108, ...,  2.86303711,
            2.76924805,  2.95525343])



WeightItの結果と大体あってそう


```python
## 重み付きデータでの効果の推定
y = biased_df.spend
X = biased_df.treatment
X = sm.add_constant(X)
results = sm.WLS(y, X, weights=weights).fit()
coef = results.summary().tables[1]
coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.5903</td> <td>    0.120</td> <td>    4.920</td> <td> 0.000</td> <td>    0.355</td> <td>    0.825</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.8856</td> <td>    0.170</td> <td>    5.203</td> <td> 0.000</td> <td>    0.552</td> <td>    1.219</td>
</tr>
</table>



## (9) 共変量のバランスを確認


```python
def calc_absolute_mean_difference(df):
    # (treatment群の平均 - control群の平均) / 全体の標準誤差
    return ((df[df.treatment==1].drop('treatment', axis=1).mean() - df[df.treatment==0].drop('treatment', axis=1).mean()) \
            / df.drop('treatment', axis=1).std()).abs()

## 調整前のAbsolute Mean Difference
unadjusted_df = pd.get_dummies(biased_df[['treatment', 'recency', 'channel', 'history']], columns=['channel'])
unadjusted_amd = calc_absolute_mean_difference(unadjusted_df)

# 傾向スコアマッチング後のAbusolute Mean Difference
after_matching_df = pd.get_dummies(biased_df.loc[matchX.index][['treatment', 'recency', 'history', 'channel']], columns=['channel'])
after_matching_amd = calc_absolute_mean_difference(after_matching_df)

# IPWで重み付け後のAbusolute Mean Difference
# 重みのぶんレコードを増やして計算する（もっといいやり方を知りたい）
after_weighted_df = pd.get_dummies(biased_df[['treatment', 'recency', 'channel', 'history']], columns=['channel'])
weights_int = (weights * 100).astype(int)
weighted_df = []
for i, value in enumerate(after_weighted_df.values):
    weighted_df.append(np.tile(value, (weights_int[i], 1)))
weighted_df = np.concatenate(weighted_df).reshape(-1, 6)
weighted_df = pd.DataFrame(weighted_df)
weighted_df.columns = after_weighted_df.columns
after_weighted_amd = calc_absolute_mean_difference(weighted_df)
```

### マッチングしたデータでの共変量のバランス


```python
balance_df = pd.concat([
    pd.DataFrame({'Absolute Mean Difference': unadjusted_amd, 'Sample': 'Unadjusted'}),
    pd.DataFrame({'Absolute Mean Difference': after_matching_amd, 'Sample': 'Adjusted'})
])
fig = px.scatter(balance_df, x='Absolute Mean Difference', y=balance_df.index, color='Sample',
                title='3.5 マッチングしたデータでの共変量のバランス')
fig.show()
```



```python
fig.write_html('../images/ch3_plot1.html', auto_open=False)
```

### 重み付きデータでの共変量のバランス


```python
balance_df = pd.concat([
    pd.DataFrame({'Absolute Mean Difference': unadjusted_amd, 'Sample': 'Unadjusted'}),
    pd.DataFrame({'Absolute Mean Difference': after_weighted_amd, 'Sample': 'Adjusted'})
])
fig = px.scatter(balance_df, x='Absolute Mean Difference', y=balance_df.index, color='Sample',
                title='重み付けしたデータでの共変量のバランス')
fig.show()
```

```python
fig.write_html('../images/ch3_plot2.html', auto_open=False)
```

## (10) 統計モデルを用いたメールの配信のログを分析


```python
random_state = 0
```


```python
## 学習データと配信ログを作るデータに分割
male_df_train, male_df_test = train_test_split(male_df, test_size=0.5, random_state=random_state)
male_df_train = male_df_train[male_df_train.treatment == 0]
```


```python
## 売上が発生する確率を予測するモデルを作成
model = LogisticRegression(random_state=random_state)
y_train = male_df_train['conversion']
X_train = pd.get_dummies(
    male_df_train[['recency', 'history_segment', 'channel', 'zip_code']], columns=['history_segment', 'channel', 'zip_code'], drop_first=True
)
X_test = pd.get_dummies(
    male_df_test[['recency', 'history_segment', 'channel', 'zip_code']], columns=['history_segment', 'channel', 'zip_code'], drop_first=True
)
model.fit(X_train, y_train)
## 売上の発生確率からメールの配信確率を決める
pred_cv = model.predict_proba(X_test)[:, 1]
pred_cv_rank = pd.Series(pred_cv, name='proba').rank(pct=True)
## 配信確率を元にメールの配信を決める
mail_assign = pred_cv_rank.apply(lambda x: np.random.binomial(n=1, p=x))
```


```python
## 配信ログを作成
male_df_test['mail_assign'] = mail_assign
male_df_test['ps'] = pred_cv_rank

ml_male_df = male_df_test[
    ((male_df_test.treatment == 1) & (male_df_test.mail_assign == 1)) |
    ((male_df_test.treatment == 0) & (male_df_test.mail_assign == 0))
].copy()
```


```python
## 平均の比較
## 実験をしていた場合の平均の差を確認
y = male_df_test.spend
X = male_df_test.treatment
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
coef = results.summary().tables[1]
coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.5585</td> <td>    0.149</td> <td>    3.752</td> <td> 0.000</td> <td>    0.267</td> <td>    0.850</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.9251</td> <td>    0.211</td> <td>    4.389</td> <td> 0.000</td> <td>    0.512</td> <td>    1.338</td>
</tr>
</table>



RCTを行っていた場合は$0.925の売上増加が期待できる


```python
## セレクションバイアスの影響を受けている平均の比較
y = ml_male_df.spend
X = ml_male_df.treatment
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
coef = results.summary().tables[1]
coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.4850</td> <td>    0.337</td> <td>    1.440</td> <td> 0.150</td> <td>   -0.175</td> <td>    1.145</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.9733</td> <td>    0.480</td> <td>    2.026</td> <td> 0.043</td> <td>    0.031</td> <td>    1.915</td>
</tr>
</table>



### 傾向スコアマッチングの推定(TPS)


```python
def get_matched_dfs_using_obtained_propensity_score(X, y, ps_score, random_state=0):
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
matchX, matchy = get_matched_dfs_using_obtained_propensity_score(ml_male_df, ml_male_df.treatment, ps_score=ml_male_df.ps)
```


```python
## マッチング後のデータで効果の推定
y = matchX.spend
X = matchy
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
coef = results.summary().tables[1]
coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.3307</td> <td>    0.379</td> <td>    0.873</td> <td> 0.383</td> <td>   -0.412</td> <td>    1.073</td>
</tr>
<tr>
  <th>treatment</th> <td>    1.0771</td> <td>    0.535</td> <td>    2.012</td> <td> 0.044</td> <td>    0.027</td> <td>    2.127</td>
</tr>
</table>



treatmentの効果は書籍より少ないが、std errの範囲内であり、且つp値が大きいのは一致している

### IPWの推定


```python
def get_ipw_obtained_ps(X, y, ps_score, random_state=0):
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
weights = get_ipw_obtained_ps(ml_male_df, ml_male_df.treatment, ps_score=ml_male_df.ps)
## 重み付きデータでの効果の推定
y = ml_male_df.spend
X = ml_male_df.treatment
X = sm.add_constant(X)
results = sm.WLS(y, X, weights=weights).fit()
coef = results.summary().tables[1]
coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.5067</td> <td>    0.319</td> <td>    1.588</td> <td> 0.112</td> <td>   -0.119</td> <td>    1.132</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.7484</td> <td>    0.454</td> <td>    1.650</td> <td> 0.099</td> <td>   -0.141</td> <td>    1.638</td>
</tr>
</table>
```python
# RCTの効果と傾向スコアマッチング後の効果の差分
0.9251 - 0.7197
```


    0.20540000000000003


```python
# RCTの効果とIPW重み付け後の効果の差分
0.9251 - 1.0987
```


    -0.17359999999999998

書籍の記載より大きい。傾向スコアマッチング後の推定された効果よりはRCTで推定された効果に近く、p-valueも小さい

### 重み付きデータの共変量のバランス


```python
## 調整前のAbsolute Mean Difference
unadjusted_df = pd.get_dummies(
    ml_male_df[['treatment', 'recency', 'history_segment', 'channel', 'zip_code']], columns=['history_segment', 'channel', 'zip_code']
)
unadjusted_amd = calc_absolute_mean_difference(unadjusted_df)

# IPWで重み付け後のAbusolute Mean Difference
# 重みのぶんレコードを増やして計算する（もっといいやり方を知りたい）
after_weighted_df = pd.get_dummies(
    ml_male_df[['treatment', 'recency', 'history_segment', 'channel', 'zip_code']], columns=['history_segment', 'channel', 'zip_code']
)
weights_int = (weights * 100).astype(int)
weighted_df = []
for i, value in enumerate(after_weighted_df.values):
    weighted_df.append(np.tile(value, (weights_int[i], 1)))
weighted_df = np.concatenate(weighted_df).reshape(-1, 15)
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
                title='重み付けしたデータでの共変量のバランス')
fig.show()
```

```python
fig.write_html('../images/ch3_plot3.html', auto_open=False)
```
