```python
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from tqdm import tqdm_notebook

import warnings
warnings.filterwarnings('ignore')
```

## (2) データの読み込み


```python
email_data = pd.read_csv('http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv')

```

## (3) ルールによるメールの配信を行ったログを作成


```python
## データの整形とrunning variableの追加
male_data = email_data[email_data.segment.isin(['Mens E-Mail', 'No E-Mail'])].copy()
male_data['treatment'] = male_data.segment.apply(lambda x: 1 if x=='Mens E-Mail' else 0)
male_data['history_log'] = np.log(male_data.history)
```


```python
## cut-off の値を指定
threshold_value = 5.5

## ルールによる介入を再現したデータを作成
## cut-offよりrunning variableが大きければが配信されたデータのみ残す
## 逆の場合には配信されなかったデータのみ残す
## running variableを0.1単位で区切ったグループわけの変数も追加しておく
male_data['history_log_grp'] = np.round(male_data.history_log / 0.1) * 0.1
rdd_data = male_data[
    ((male_data.history_log > threshold_value) & (male_data.segment == 'Mens E-Mail')) | 
    ((male_data.history_log <= threshold_value) & (male_data.segment == 'No E-Mail'))
]
```

## (4) RCTデータとRDDデータの傾向の比較

### running variableとサイト来訪率のプロット(RCTデータ)


```python
summarised = male_data.groupby(['history_log_grp', 'segment']).agg(visit=('visit', 'mean'), N=('visit', 'count')).reset_index()
summarised = summarised[summarised.N > 10]
```


```python
fig = px.scatter(summarised, x='history_log_grp', y='visit', color='segment', symbol='segment', size='N'
           , title='5.2 実験データにおける来訪率とlog(history_i)')
fig.show()
```




```python
fig.write_html('../images/ch5_plot2_2.html')
```

## rddtoolsの再現（非線形回帰による分析）


```python
class RDDRegression:
# Rパッケージrddtoolsのrdd_reg_lmを再現する
# 参考：https://cran.r-project.org/web/packages/rddtools/rddtools.pdf P23
    def __init__(self, cut_point, degree=4):
        self.cut_point = cut_point
        self.degree = degree
        
    def _preprocess(self, X):
        X = X - threshold_value
        X_poly = PolynomialFeatures(degree=self.degree, include_bias=False).fit_transform(X)
        D_df = X.applymap(lambda x: 1 if x >= 0 else 0)
        X = pd.DataFrame(X_poly, columns=[f'X^{i+1}' for i in range(X_poly.shape[1])])
        X['D'] = D_df
        for i in range(X_poly.shape[1]):
            X[f'D_X^{i+1}'] = X_poly[:, i] * X['D']
        return X
    
    def fit(self, X, y):
        X = X.copy()
        X = self._preprocess(X)
        self.X = X
        self.y = y
        X = sm.add_constant(X)
        self.model = sm.OLS(y, X)
        self.results = self.model.fit()
        coef = self.results.summary().tables[1]
        self.coef = pd.read_html(coef.as_html(), header=0, index_col=0)[0]
        
    def predict(self, X):
        X = self._preprocess(X)
        X = sm.add_constant(X)
        return self.model.predict(self.results.params, X)
```


```python
rdd_data = rdd_data.reset_index(drop=True)
rddr = RDDRegression(cut_point=threshold_value, degree=4)
rddr.fit(rdd_data[['history_log']], rdd_data.visit)
coef = rddr.results.summary().tables[1]
coef = pd.read_html(coef.as_html(), header=0, index_col=0)[0]
coef
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
      <th>const</th>
      <td>0.1327</td>
      <td>0.014</td>
      <td>9.654</td>
      <td>0.000</td>
      <td>0.106</td>
      <td>0.160</td>
    </tr>
    <tr>
      <th>X^1</th>
      <td>0.1522</td>
      <td>0.092</td>
      <td>1.661</td>
      <td>0.097</td>
      <td>-0.027</td>
      <td>0.332</td>
    </tr>
    <tr>
      <th>X^2</th>
      <td>0.1877</td>
      <td>0.178</td>
      <td>1.056</td>
      <td>0.291</td>
      <td>-0.161</td>
      <td>0.536</td>
    </tr>
    <tr>
      <th>X^3</th>
      <td>0.1068</td>
      <td>0.126</td>
      <td>0.847</td>
      <td>0.397</td>
      <td>-0.140</td>
      <td>0.354</td>
    </tr>
    <tr>
      <th>X^4</th>
      <td>0.0224</td>
      <td>0.029</td>
      <td>0.769</td>
      <td>0.442</td>
      <td>-0.035</td>
      <td>0.079</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.0741</td>
      <td>0.020</td>
      <td>3.774</td>
      <td>0.000</td>
      <td>0.036</td>
      <td>0.113</td>
    </tr>
    <tr>
      <th>D_X^1</th>
      <td>-0.0406</td>
      <td>0.135</td>
      <td>-0.300</td>
      <td>0.764</td>
      <td>-0.306</td>
      <td>0.225</td>
    </tr>
    <tr>
      <th>D_X^2</th>
      <td>-0.3928</td>
      <td>0.271</td>
      <td>-1.449</td>
      <td>0.147</td>
      <td>-0.924</td>
      <td>0.139</td>
    </tr>
    <tr>
      <th>D_X^3</th>
      <td>0.0278</td>
      <td>0.198</td>
      <td>0.140</td>
      <td>0.888</td>
      <td>-0.360</td>
      <td>0.415</td>
    </tr>
    <tr>
      <th>D_X^4</th>
      <td>-0.0484</td>
      <td>0.047</td>
      <td>-1.032</td>
      <td>0.302</td>
      <td>-0.140</td>
      <td>0.044</td>
    </tr>
  </tbody>
</table>
</div>



変数Dのcoefを見る。書籍のrddtoolsによる推定とp-value含めほぼ一致。


```python
y_pred = rddr.predict(rdd_data[['history_log']])
visualized = pd.DataFrame({'history_log': rdd_data['history_log'], 'y_pred': y_pred})
visualized = visualized.sort_values('history_log')
```

### 追加：回帰の結果の可視化


```python
fig = px.scatter(summarised, x='history_log_grp', y='visit', color='segment', symbol='segment', size='N'
           , title='RDDの可視化：非実験データにおける来訪率とlog(history_i)')
fig.add_trace(go.Scatter(
    x=[threshold_value, threshold_value],
    y=[0, 0.35],
    mode="lines",
    line=dict(color='gray', dash='dot'),
    name='cut-off value'
))
fig.add_trace(go.Scatter(
    x=visualized.history_log,
    y=visualized.y_pred,
    mode='lines',
    name='回帰の結果'
))
```




```python
fig.write_html('../images/ch5_plot2_3.html')
```

## (7) 分析に使うデータの幅と分析結果のプロット


```python
bound_list = [i / 100 for i in range(2, 101)]
lates = []
Ns = []
ses = []
for bound in bound_list:
    bounded_data = rdd_data[(rdd_data.history_log >= threshold_value - bound) & (rdd_data.history_log < threshold_value + bound)]
    agg_data = bounded_data.groupby('treatment').agg(count=('visit', 'count'), visit_rate=('visit', 'mean'))
    lates.append(agg_data.loc[1, 'visit_rate'] - agg_data.loc[0, 'visit_rate'])
    N = sum(agg_data['count'])
    Ns.append(N)
    ses.append(np.sqrt(sum(agg_data.visit_rate ** 2)) / np.sqrt(N))
    
result_data = pd.DataFrame({
    'bound': bound_list,
    'late': lates,
    'N': Ns,
    'se': ses
})
```



```python
fig = px.line(result_data, x='bound', y='late', title='5.5 利用するデータの範囲と推定結果')
fig.add_trace(go.Scatter(
    x=result_data.bound,
    y=result_data.late - (1.96 * result_data.se),
    fill=None,
    mode='lines',
    line_color='indigo',
    ))
fig.add_trace(go.Scatter(
    x=result_data.bound,
    y=result_data.late + (1.96 * result_data.se),
    fill='tonexty', # fill area between trace0 and trace1
    mode='lines', line_color='indigo'))
```




```python
fig.write_html('../images/ch5_plot3.html')
```

## (8) nonparametric RDD

 Imbens-Kalyanaraman(2011)の手法で最適なデータ幅を推定するみたいだが、よくわからなかったので雑に調べる


```python
train, test = train_test_split(rdd_data, test_size=0.1, random_state=0)
train.reset_index(drop=True, inplace=True)
test.reset_index(drop=True, inplace=True)

bound_list = [i / 100 for i in range(2, 301)]
min_mse = np.inf
# 0.01刻みでバンド幅を変えて、test dataのMSEが小さくなるときのバンド幅を出す
for bound in tqdm_notebook(bound_list):
    bounded_data = train[(train.history_log >= threshold_value - bound) & (train.history_log < threshold_value + bound)]
    bounded_data = bounded_data.reset_index(drop=True)
    rddr = RDDRegression(cut_point=threshold_value, degree=4)
    rddr.fit(bounded_data[['history_log']], bounded_data.visit)
    mse = mean_squared_error(test.history_log, rddr.predict(test[['history_log']]))
    if mse < min_mse:
        min_mse = mse
        min_bound = bound
        min_rddr = rddr
        print(f'min mse: {min_mse}, bound: {min_bound}')
```


    HBox(children=(FloatProgress(value=0.0, max=299.0), HTML(value='')))


    min mse: 2.5243202077652755e+17, bound: 0.02
    min mse: 3081618022828634.0, bound: 0.03
    min mse: 109616673657887.28, bound: 0.04
    min mse: 29447688284724.8, bound: 0.05
    min mse: 2246295024527.305, bound: 0.06
    min mse: 820539191140.5446, bound: 0.07
    min mse: 727782333876.8143, bound: 0.09
    min mse: 141322573518.7531, bound: 0.1
    min mse: 50720103617.07564, bound: 0.11
    min mse: 25016889912.390812, bound: 0.12
    min mse: 2487593264.3424916, bound: 0.13
    min mse: 1209245062.974647, bound: 0.14
    min mse: 896062178.4056213, bound: 0.15
    min mse: 291190524.29759717, bound: 0.16
    min mse: 23781040.405873988, bound: 0.17
    min mse: 2077515.3012353708, bound: 0.2
    min mse: 815887.1912123369, bound: 0.22
    min mse: 206106.4522611691, bound: 0.29
    min mse: 24325.29532961157, bound: 0.32
    min mse: 1660.5301907681837, bound: 0.38
    min mse: 1610.8386911459193, bound: 0.43
    min mse: 175.5477628875156, bound: 0.51
    min mse: 104.02217011240118, bound: 0.55
    min mse: 60.43729325782254, bound: 0.59
    min mse: 57.10864216379814, bound: 0.82
    min mse: 43.14169833658822, bound: 0.85
    min mse: 41.94341597378361, bound: 0.87
    min mse: 38.29040623209319, bound: 0.88
    min mse: 26.636848720254378, bound: 0.89
    min mse: 22.319463371120715, bound: 0.9
    min mse: 21.45941261827524, bound: 0.91
    
    


```python
bounded_data = rdd_data[(rdd_data.history_log >= threshold_value - min_bound) & (rdd_data.history_log < threshold_value + min_bound)]
```


```python
coef = min_rddr.results.summary().tables[1]
coef = pd.read_html(coef.as_html(), header=0, index_col=0)[0]
```


```python
print(f'''
Bandwidth:\t{min_bound}
Observations:\t{len(bounded_data)}
Estimate:\t\t{min_rddr.results.params['D']: .4f}
std err:\t\t{coef.loc['D', 'std err']}
''')
```

    
    Bandwidth:	0.91
    Observations:	11960
    Estimate:		 0.1031
    std err:		0.033
    
    

RDestimateの推定（書籍の記述）より少しバンド幅が広い

### 分析結果の可視化


```python
visualized = rdd_data.copy()
visualized['y_pred'] = min_rddr.predict(rdd_data[['history_log']])
# 可視化する際cut off値で繋げないようにデータを分ける
left_rdd_data = visualized[visualized.history_log < threshold_value].copy()
right_rdd_data = visualized[visualized.history_log >= threshold_value].copy()
left_rdd_data = left_rdd_data.sort_values('history_log')
left_rdd_data['y_pred'] = left_rdd_data.y_pred.apply(lambda x: np.nan if x > 0.2 else x) # 可視化のため大きい数値をなくす
right_rdd_data = right_rdd_data.sort_values('history_log')
right_rdd_data['y_pred'] = right_rdd_data.y_pred.apply(lambda x: np.nan if x > 0.5 else x) # 可視化のため大きい数値をなくす


fig = px.scatter(summarised, x='history_log_grp', y='visit', color='segment', symbol='segment', size='N'
           , title='RDDの可視化：バンド幅を調整後')
fig.add_trace(go.Scatter(
    x=[threshold_value, threshold_value],
    y=[0, 0.35],
    mode="lines",
    line=dict(color='gray', dash='dot'),
    name='cut-off value'
))
fig.add_trace(go.Scatter(
    x=left_rdd_data.history_log,
    y=left_rdd_data.y_pred,
    mode='lines',
    name='回帰の結果(left)'
))
fig.add_trace(go.Scatter(
    x=right_rdd_data.history_log,
    y=right_rdd_data.y_pred,
    mode='lines',
    name='回帰の結果(right)'
))
```



```python
fig.write_html('../images/ch5_plot4.html')
```

なんかあまり良くない気がする。やっぱり雑に調整するのは良くなかったのか
