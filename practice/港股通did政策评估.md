```python
import numpy as np
import pandas as pd
```


```python
df = pd.read_excel("最终整理数据第二版修正版.xlsx")
```


```python
df = df.drop(['首次被调入日期', '调入', '调入fill'], axis=1)
```


```python
di = [str(i) for i in list(df['交易月份'].unique())]
```


```python
def get_final_data(path):
    da = pd.read_excel("choice/"+path).dropna()
    da.columns = ['证券代码', '证券名称', *di]
    da_final = da.set_index(["证券代码", "证券名称"]).stack().reset_index()
    da_final.columns = ["证券代码", "证券名称", '交易月份', path.split(".")[0]]
    return da_final
```


```python
_ = get_final_data("大股东持股比例.xls")
```


```python
_.head()
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
      <th>证券代码</th>
      <th>证券名称</th>
      <th>交易月份</th>
      <th>大股东持股比例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>600000.SH</td>
      <td>浦发银行</td>
      <td>201211</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>600000.SH</td>
      <td>浦发银行</td>
      <td>201212</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>600000.SH</td>
      <td>浦发银行</td>
      <td>201301</td>
      <td>20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>600000.SH</td>
      <td>浦发银行</td>
      <td>201302</td>
      <td>20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>600000.SH</td>
      <td>浦发银行</td>
      <td>201303</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
_.columns = ['ts_code', '证券名称', '交易月份', '大股东持股比例']
```


```python
df.columns
```




    Index(['ts_code', '交易月份', 'std', 'turnover_rate_f', 'circ_mv', 'lnmv', 'swing',
           'skew', 'kurt', 'newBM', '证券名称', 'roe', '资产负债率', 'pct_chg',
           'pct_chg_lag1', '证券代码', '是否沪港通', '调入fill02', 'did'],
          dtype='object')




```python
_[['ts_code', '交易月份', '大股东持股比例']].head()
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
      <th>ts_code</th>
      <th>交易月份</th>
      <th>大股东持股比例</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>600000.SH</td>
      <td>201211</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>600000.SH</td>
      <td>201212</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>600000.SH</td>
      <td>201301</td>
      <td>20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>600000.SH</td>
      <td>201302</td>
      <td>20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>600000.SH</td>
      <td>201303</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.head()
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
      <th>ts_code</th>
      <th>交易月份</th>
      <th>std</th>
      <th>turnover_rate_f</th>
      <th>circ_mv</th>
      <th>lnmv</th>
      <th>swing</th>
      <th>skew</th>
      <th>kurt</th>
      <th>newBM</th>
      <th>证券名称</th>
      <th>roe</th>
      <th>资产负债率</th>
      <th>pct_chg</th>
      <th>pct_chg_lag1</th>
      <th>证券代码</th>
      <th>是否沪港通</th>
      <th>调入fill02</th>
      <th>did</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>600004.SH</td>
      <td>201211</td>
      <td>0.011360</td>
      <td>0.089636</td>
      <td>740600.0</td>
      <td>13.515216</td>
      <td>0.015818</td>
      <td>-0.622903</td>
      <td>0.062564</td>
      <td>0.950119</td>
      <td>白云机场</td>
      <td>10.685160</td>
      <td>26.336032</td>
      <td>-0.0228</td>
      <td>-0.0237</td>
      <td>600004</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>600004.SH</td>
      <td>201212</td>
      <td>0.010936</td>
      <td>0.182390</td>
      <td>815350.0</td>
      <td>13.611373</td>
      <td>0.017903</td>
      <td>0.495511</td>
      <td>0.484885</td>
      <td>0.862962</td>
      <td>白云机场</td>
      <td>10.685160</td>
      <td>26.336032</td>
      <td>0.1009</td>
      <td>-0.0228</td>
      <td>600004</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>600004.SH</td>
      <td>201301</td>
      <td>0.016276</td>
      <td>0.234453</td>
      <td>871700.0</td>
      <td>13.678201</td>
      <td>0.021841</td>
      <td>1.201788</td>
      <td>1.251243</td>
      <td>0.807233</td>
      <td>白云机场</td>
      <td>2.949058</td>
      <td>25.471559</td>
      <td>0.0691</td>
      <td>0.1009</td>
      <td>600004</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>600004.SH</td>
      <td>201302</td>
      <td>0.013665</td>
      <td>0.132297</td>
      <td>856750.0</td>
      <td>13.660901</td>
      <td>0.019057</td>
      <td>-0.643313</td>
      <td>0.585689</td>
      <td>0.821288</td>
      <td>白云机场</td>
      <td>2.949058</td>
      <td>25.471559</td>
      <td>-0.0172</td>
      <td>0.0691</td>
      <td>600004</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>600004.SH</td>
      <td>201303</td>
      <td>0.011642</td>
      <td>0.122468</td>
      <td>794650.0</td>
      <td>13.585657</td>
      <td>0.016409</td>
      <td>-0.142751</td>
      <td>-0.397517</td>
      <td>0.909339</td>
      <td>白云机场</td>
      <td>2.949058</td>
      <td>25.471559</td>
      <td>-0.0725</td>
      <td>-0.0172</td>
      <td>600004</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['交易月份'] = df['交易月份'].astype("str")
```


```python
df = df.merge(_[['ts_code', '交易月份', '大股东持股比例']], on=['ts_code', '交易月份'], how='left')
```


```python
df['大股东持股比例'] = df['大股东持股比例'].astype("float")
```


```python
df.shape
```




    (39361, 20)




```python
df_drop = df.dropna()
```


```python
df_drop.shape
```




    (39361, 20)




```python
df_drop = df_drop[df_drop['交易月份'] != '201411']
```


```python
df_drop['date'] = pd.to_datetime(df_drop['交易月份'], format="%Y%m")
```


```python
df_drop_short = df_drop[(df_drop.date >= '2013-11-01') & (df_drop.date <= '2015-11-30')]
```


```python
df_drop.shape
```




    (38568, 21)




```python
df_drop_short.shape
```




    (19090, 21)




```python
df_drop.head()
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
      <th>ts_code</th>
      <th>交易月份</th>
      <th>std</th>
      <th>turnover_rate_f</th>
      <th>circ_mv</th>
      <th>lnmv</th>
      <th>swing</th>
      <th>skew</th>
      <th>kurt</th>
      <th>newBM</th>
      <th>...</th>
      <th>roe</th>
      <th>资产负债率</th>
      <th>pct_chg</th>
      <th>pct_chg_lag1</th>
      <th>证券代码</th>
      <th>是否沪港通</th>
      <th>调入fill02</th>
      <th>did</th>
      <th>大股东持股比例</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>600004.SH</td>
      <td>201211</td>
      <td>0.011360</td>
      <td>0.089636</td>
      <td>740600.0</td>
      <td>13.515216</td>
      <td>0.015818</td>
      <td>-0.622903</td>
      <td>0.062564</td>
      <td>0.950119</td>
      <td>...</td>
      <td>10.685160</td>
      <td>26.336032</td>
      <td>-0.0228</td>
      <td>-0.0237</td>
      <td>600004</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>61.964475</td>
      <td>2012-11-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>600004.SH</td>
      <td>201212</td>
      <td>0.010936</td>
      <td>0.182390</td>
      <td>815350.0</td>
      <td>13.611373</td>
      <td>0.017903</td>
      <td>0.495511</td>
      <td>0.484885</td>
      <td>0.862962</td>
      <td>...</td>
      <td>10.685160</td>
      <td>26.336032</td>
      <td>0.1009</td>
      <td>-0.0228</td>
      <td>600004</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>61.964475</td>
      <td>2012-12-01</td>
    </tr>
    <tr>
      <th>2</th>
      <td>600004.SH</td>
      <td>201301</td>
      <td>0.016276</td>
      <td>0.234453</td>
      <td>871700.0</td>
      <td>13.678201</td>
      <td>0.021841</td>
      <td>1.201788</td>
      <td>1.251243</td>
      <td>0.807233</td>
      <td>...</td>
      <td>2.949058</td>
      <td>25.471559</td>
      <td>0.0691</td>
      <td>0.1009</td>
      <td>600004</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>61.960000</td>
      <td>2013-01-01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>600004.SH</td>
      <td>201302</td>
      <td>0.013665</td>
      <td>0.132297</td>
      <td>856750.0</td>
      <td>13.660901</td>
      <td>0.019057</td>
      <td>-0.643313</td>
      <td>0.585689</td>
      <td>0.821288</td>
      <td>...</td>
      <td>2.949058</td>
      <td>25.471559</td>
      <td>-0.0172</td>
      <td>0.0691</td>
      <td>600004</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>61.960000</td>
      <td>2013-02-01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>600004.SH</td>
      <td>201303</td>
      <td>0.011642</td>
      <td>0.122468</td>
      <td>794650.0</td>
      <td>13.585657</td>
      <td>0.016409</td>
      <td>-0.142751</td>
      <td>-0.397517</td>
      <td>0.909339</td>
      <td>...</td>
      <td>2.949058</td>
      <td>25.471559</td>
      <td>-0.0725</td>
      <td>-0.0172</td>
      <td>600004</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>61.960000</td>
      <td>2013-03-01</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>




```python
df_drop.columns
```




    Index(['ts_code', '交易月份', 'std', 'turnover_rate_f', 'circ_mv', 'lnmv', 'swing',
           'skew', 'kurt', 'newBM', '证券名称', 'roe', '资产负债率', 'pct_chg',
           'pct_chg_lag1', '证券代码', '是否沪港通', '调入fill02', 'did', '大股东持股比例', 'date'],
          dtype='object')




```python
df_drop['mt'] = df_drop['是否沪港通'].astype("str") + df_drop['调入fill02'].astype("str")
```


```python
df_drop.groupby('mt')[['std', 'swing']].describe().T
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
      <th>mt</th>
      <th>00</th>
      <th>01</th>
      <th>10</th>
      <th>11</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">std</th>
      <th>count</th>
      <td>6316.000000</td>
      <td>5999.000000</td>
      <td>13315.000000</td>
      <td>12938.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.022947</td>
      <td>0.036278</td>
      <td>0.022622</td>
      <td>0.033319</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.009008</td>
      <td>0.017908</td>
      <td>0.009246</td>
      <td>0.017435</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000129</td>
      <td>0.000089</td>
      <td>0.000455</td>
      <td>0.000071</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.016705</td>
      <td>0.022392</td>
      <td>0.016171</td>
      <td>0.019557</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.021158</td>
      <td>0.032647</td>
      <td>0.021054</td>
      <td>0.029877</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.027517</td>
      <td>0.046897</td>
      <td>0.027420</td>
      <td>0.044052</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.073879</td>
      <td>0.105232</td>
      <td>0.142767</td>
      <td>0.103194</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">swing</th>
      <th>count</th>
      <td>6316.000000</td>
      <td>5999.000000</td>
      <td>13315.000000</td>
      <td>12938.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.034843</td>
      <td>0.051253</td>
      <td>0.033896</td>
      <td>0.046745</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.011208</td>
      <td>0.021781</td>
      <td>0.011818</td>
      <td>0.021844</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.003651</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.026831</td>
      <td>0.034352</td>
      <td>0.025521</td>
      <td>0.029698</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.032987</td>
      <td>0.047026</td>
      <td>0.032062</td>
      <td>0.042423</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.041023</td>
      <td>0.065306</td>
      <td>0.040371</td>
      <td>0.060982</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.115624</td>
      <td>0.125692</td>
      <td>0.100897</td>
      <td>0.151389</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_drop_02 = df_drop.set_index(['ts_code', 'date'])
df_drop_short_02 = df_drop_short.set_index(['ts_code', 'date'])
```


```python
# X_cols_02 = ['did', 'turnover_rate_f', 'lnmv', 'skew', 'kurt', 'newBM', 'roe', '资产负债率', 'pct_chg', 'pct_chg_lag1']
X_cols = ['did', 'pct_chg', 'pct_chg_lag1', '大股东持股比例', 'turnover_rate_f', 'newBM', 'roe', '资产负债率', 'skew', 'kurt',]
y_cols = ['std', 'swing', ]
```


```python
df_drop_02[[*X_cols, *y_cols, 'lnmv']].corr()
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
      <th>did</th>
      <th>pct_chg</th>
      <th>pct_chg_lag1</th>
      <th>大股东持股比例</th>
      <th>turnover_rate_f</th>
      <th>newBM</th>
      <th>roe</th>
      <th>资产负债率</th>
      <th>skew</th>
      <th>kurt</th>
      <th>std</th>
      <th>swing</th>
      <th>lnmv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>did</th>
      <td>1.000000</td>
      <td>-0.019601</td>
      <td>-0.012756</td>
      <td>0.059196</td>
      <td>0.182233</td>
      <td>-0.102788</td>
      <td>0.037180</td>
      <td>-0.022734</td>
      <td>-0.047112</td>
      <td>-0.030891</td>
      <td>0.231619</td>
      <td>0.214729</td>
      <td>0.469175</td>
    </tr>
    <tr>
      <th>pct_chg</th>
      <td>-0.019601</td>
      <td>1.000000</td>
      <td>0.001373</td>
      <td>-0.012280</td>
      <td>0.165269</td>
      <td>-0.126866</td>
      <td>0.006597</td>
      <td>0.001174</td>
      <td>0.216130</td>
      <td>0.065847</td>
      <td>-0.069904</td>
      <td>-0.034901</td>
      <td>0.040406</td>
    </tr>
    <tr>
      <th>pct_chg_lag1</th>
      <td>-0.012756</td>
      <td>0.001373</td>
      <td>1.000000</td>
      <td>-0.011107</td>
      <td>0.195524</td>
      <td>-0.121614</td>
      <td>-0.010368</td>
      <td>0.001648</td>
      <td>0.036021</td>
      <td>-0.024261</td>
      <td>0.013875</td>
      <td>0.095776</td>
      <td>0.038403</td>
    </tr>
    <tr>
      <th>大股东持股比例</th>
      <td>0.059196</td>
      <td>-0.012280</td>
      <td>-0.011107</td>
      <td>1.000000</td>
      <td>-0.023385</td>
      <td>0.228089</td>
      <td>0.035456</td>
      <td>0.060050</td>
      <td>0.014719</td>
      <td>0.021346</td>
      <td>-0.053279</td>
      <td>-0.065024</td>
      <td>0.227644</td>
    </tr>
    <tr>
      <th>turnover_rate_f</th>
      <td>0.182233</td>
      <td>0.165269</td>
      <td>0.195524</td>
      <td>-0.023385</td>
      <td>1.000000</td>
      <td>-0.308670</td>
      <td>-0.043820</td>
      <td>-0.012095</td>
      <td>0.055242</td>
      <td>-0.144362</td>
      <td>0.611795</td>
      <td>0.643566</td>
      <td>0.030573</td>
    </tr>
    <tr>
      <th>newBM</th>
      <td>-0.102788</td>
      <td>-0.126866</td>
      <td>-0.121614</td>
      <td>0.228089</td>
      <td>-0.308670</td>
      <td>1.000000</td>
      <td>0.027491</td>
      <td>0.116225</td>
      <td>-0.032373</td>
      <td>0.063134</td>
      <td>-0.296677</td>
      <td>-0.339556</td>
      <td>0.055843</td>
    </tr>
    <tr>
      <th>roe</th>
      <td>0.037180</td>
      <td>0.006597</td>
      <td>-0.010368</td>
      <td>0.035456</td>
      <td>-0.043820</td>
      <td>0.027491</td>
      <td>1.000000</td>
      <td>-0.107554</td>
      <td>0.003849</td>
      <td>0.004669</td>
      <td>-0.048463</td>
      <td>-0.051446</td>
      <td>0.074135</td>
    </tr>
    <tr>
      <th>资产负债率</th>
      <td>-0.022734</td>
      <td>0.001174</td>
      <td>0.001648</td>
      <td>0.060050</td>
      <td>-0.012095</td>
      <td>0.116225</td>
      <td>-0.107554</td>
      <td>1.000000</td>
      <td>0.022726</td>
      <td>0.028121</td>
      <td>0.000746</td>
      <td>0.001808</td>
      <td>0.047144</td>
    </tr>
    <tr>
      <th>skew</th>
      <td>-0.047112</td>
      <td>0.216130</td>
      <td>0.036021</td>
      <td>0.014719</td>
      <td>0.055242</td>
      <td>-0.032373</td>
      <td>0.003849</td>
      <td>0.022726</td>
      <td>1.000000</td>
      <td>0.149342</td>
      <td>0.020069</td>
      <td>0.005445</td>
      <td>0.072942</td>
    </tr>
    <tr>
      <th>kurt</th>
      <td>-0.030891</td>
      <td>0.065847</td>
      <td>-0.024261</td>
      <td>0.021346</td>
      <td>-0.144362</td>
      <td>0.063134</td>
      <td>0.004669</td>
      <td>0.028121</td>
      <td>0.149342</td>
      <td>1.000000</td>
      <td>-0.214967</td>
      <td>-0.285673</td>
      <td>-0.021132</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.231619</td>
      <td>-0.069904</td>
      <td>0.013875</td>
      <td>-0.053279</td>
      <td>0.611795</td>
      <td>-0.296677</td>
      <td>-0.048463</td>
      <td>0.000746</td>
      <td>0.020069</td>
      <td>-0.214967</td>
      <td>1.000000</td>
      <td>0.929900</td>
      <td>0.074597</td>
    </tr>
    <tr>
      <th>swing</th>
      <td>0.214729</td>
      <td>-0.034901</td>
      <td>0.095776</td>
      <td>-0.065024</td>
      <td>0.643566</td>
      <td>-0.339556</td>
      <td>-0.051446</td>
      <td>0.001808</td>
      <td>0.005445</td>
      <td>-0.285673</td>
      <td>0.929900</td>
      <td>1.000000</td>
      <td>0.069011</td>
    </tr>
    <tr>
      <th>lnmv</th>
      <td>0.469175</td>
      <td>0.040406</td>
      <td>0.038403</td>
      <td>0.227644</td>
      <td>0.030573</td>
      <td>0.055843</td>
      <td>0.074135</td>
      <td>0.047144</td>
      <td>0.072942</td>
      <td>-0.021132</td>
      <td>0.074597</td>
      <td>0.069011</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
X_long = df_drop_02[X_cols]
y_long_1 = df_drop_02[y_cols[0]]
y_long_2 = df_drop_02[y_cols[1]]


X_short = df_drop_short_02[X_cols]
y_short_1 = df_drop_short_02[y_cols[0]]
y_short_2 = df_drop_short_02[y_cols[1]]
```


```python
from linearmodels.panel import PanelOLS
from linearmodels.datasets import wage_panel
import statsmodels.api as sm

def fix_effect_model(X, y):
    exog = sm.add_constant(X)
    mod = PanelOLS(y, exog, entity_effects=True)
    res = mod.fit(cov_type='unadjusted')
    return res
```


```python
fix_effect_model(X_long, y_long_1)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>           <td>std</td>       <th>  R-squared:         </th>     <td>0.4705</td>   
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>0.1195</td>   
</tr>
<tr>
  <th>No. Observations:</th>       <td>38568</td>      <th>  R-squared (Within):</th>     <td>0.4705</td>   
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.4475</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>10:53:55</td>     <th>  Log-likelihood     </th>    <td>1.205e+05</td> 
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>3351.5</td>   
</tr>
<tr>
  <th>Entities:</th>                <td>845</td>       <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Avg Obs:</th>               <td>45.643</td>      <th>  Distribution:      </th>   <td>F(10,37713)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>17.000</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>48.000</td>      <th>  F-statistic (robust):</th>   <td>3351.5</td>   
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Time periods:</th>            <td>48</td>        <th>  Distribution:      </th>   <td>F(10,37713)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>803.50</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Min Obs:</th>               <td>737.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>831.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>      
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>          <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>   <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>             <td>0.0235</td>    <td>0.0006</td>   <td>36.321</td>  <td>0.0000</td>    <td>0.0222</td>     <td>0.0248</td>  
</tr>
<tr>
  <th>did</th>               <td>0.0032</td>    <td>0.0001</td>   <td>21.778</td>  <td>0.0000</td>    <td>0.0029</td>     <td>0.0035</td>  
</tr>
<tr>
  <th>pct_chg</th>           <td>-0.0197</td>   <td>0.0004</td>   <td>-52.949</td> <td>0.0000</td>    <td>-0.0204</td>    <td>-0.0189</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>      <td>-0.0135</td>   <td>0.0004</td>   <td>-36.956</td> <td>0.0000</td>    <td>-0.0142</td>    <td>-0.0128</td> 
</tr>
<tr>
  <th>大股东持股比例</th>          <td>1.428e-06</td> <td>1.215e-05</td> <td>0.1176</td>  <td>0.9064</td>  <td>-2.238e-05</td>  <td>2.524e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>   <td>0.0136</td>    <td>0.0001</td>   <td>130.60</td>  <td>0.0000</td>    <td>0.0134</td>     <td>0.0139</td>  
</tr>
<tr>
  <th>newBM</th>             <td>-0.0135</td>   <td>0.0005</td>   <td>-29.731</td> <td>0.0000</td>    <td>-0.0144</td>    <td>-0.0126</td> 
</tr>
<tr>
  <th>roe</th>             <td>-7.482e-06</td> <td>1.85e-06</td>  <td>-4.0434</td> <td>0.0001</td>  <td>-1.111e-05</td> <td>-3.855e-06</td>
</tr>
<tr>
  <th>资产负债率</th>            <td>1.395e-05</td> <td>7.76e-06</td>  <td>1.7979</td>  <td>0.0722</td>  <td>-1.258e-06</td>  <td>2.916e-05</td>
</tr>
<tr>
  <th>skew</th>              <td>0.0009</td>   <td>7.348e-05</td> <td>11.966</td>  <td>0.0000</td>    <td>0.0007</td>     <td>0.0010</td>  
</tr>
<tr>
  <th>kurt</th>              <td>-0.0009</td>  <td>3.054e-05</td> <td>-29.089</td> <td>0.0000</td>    <td>-0.0009</td>    <td>-0.0008</td> 
</tr>
</table><br/><br/>F-test for Poolability: 3.8801<br/>P-value: 0.0000<br/>Distribution: F(844,37713)<br/><br/>Included effects: Entity<br/>id: 0x1bff837d430




```python
fix_effect_model(X_long, y_long_2)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>          <td>swing</td>      <th>  R-squared:         </th>     <td>0.5146</td>   
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>0.1941</td>   
</tr>
<tr>
  <th>No. Observations:</th>       <td>38568</td>      <th>  R-squared (Within):</th>     <td>0.5146</td>   
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.4875</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>10:53:55</td>     <th>  Log-likelihood     </th>    <td>1.141e+05</td> 
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>3998.8</td>   
</tr>
<tr>
  <th>Entities:</th>                <td>845</td>       <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Avg Obs:</th>               <td>45.643</td>      <th>  Distribution:      </th>   <td>F(10,37713)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>17.000</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>48.000</td>      <th>  F-statistic (robust):</th>   <td>3998.8</td>   
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Time periods:</th>            <td>48</td>        <th>  Distribution:      </th>   <td>F(10,37713)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>803.50</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Min Obs:</th>               <td>737.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>831.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>      
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>         <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>   <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>            <td>0.0362</td>    <td>0.0008</td>   <td>47.484</td>  <td>0.0000</td>    <td>0.0347</td>     <td>0.0377</td>  
</tr>
<tr>
  <th>did</th>              <td>0.0032</td>    <td>0.0002</td>   <td>17.962</td>  <td>0.0000</td>    <td>0.0028</td>     <td>0.0035</td>  
</tr>
<tr>
  <th>pct_chg</th>          <td>-0.0198</td>   <td>0.0004</td>   <td>-45.101</td> <td>0.0000</td>    <td>-0.0206</td>    <td>-0.0189</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>     <td>-0.0075</td>   <td>0.0004</td>   <td>-17.424</td> <td>0.0000</td>    <td>-0.0083</td>    <td>-0.0066</td> 
</tr>
<tr>
  <th>大股东持股比例</th>         <td>1.347e-05</td> <td>1.432e-05</td> <td>0.9410</td>  <td>0.3467</td>  <td>-1.459e-05</td>  <td>4.154e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>  <td>0.0168</td>    <td>0.0001</td>   <td>136.42</td>  <td>0.0000</td>    <td>0.0166</td>     <td>0.0170</td>  
</tr>
<tr>
  <th>newBM</th>            <td>-0.0195</td>   <td>0.0005</td>   <td>-36.336</td> <td>0.0000</td>    <td>-0.0205</td>    <td>-0.0184</td> 
</tr>
<tr>
  <th>roe</th>             <td>-8.06e-06</td> <td>2.181e-06</td> <td>-3.6953</td> <td>0.0002</td>  <td>-1.234e-05</td> <td>-3.785e-06</td>
</tr>
<tr>
  <th>资产负债率</th>           <td>2.099e-05</td> <td>9.147e-06</td> <td>2.2945</td>  <td>0.0218</td>   <td>3.059e-06</td>  <td>3.892e-05</td>
</tr>
<tr>
  <th>skew</th>             <td>0.0006</td>   <td>8.662e-05</td> <td>7.3200</td>  <td>0.0000</td>    <td>0.0005</td>     <td>0.0008</td>  
</tr>
<tr>
  <th>kurt</th>             <td>-0.0018</td>  <td> 3.6e-05</td>  <td>-49.759</td> <td>0.0000</td>    <td>-0.0019</td>    <td>-0.0017</td> 
</tr>
</table><br/><br/>F-test for Poolability: 5.0963<br/>P-value: 0.0000<br/>Distribution: F(844,37713)<br/><br/>Included effects: Entity<br/>id: 0x1bf8601d310




```python
fix_effect_model(X_short, y_short_1)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>           <td>std</td>       <th>  R-squared:         </th>     <td>0.6134</td>   
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>-0.4389</td>  
</tr>
<tr>
  <th>No. Observations:</th>       <td>19090</td>      <th>  R-squared (Within):</th>     <td>0.6134</td>   
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.5382</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>10:53:56</td>     <th>  Log-likelihood     </th>    <td>5.99e+04</td>  
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>2892.7</td>   
</tr>
<tr>
  <th>Entities:</th>                <td>845</td>       <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Avg Obs:</th>               <td>22.592</td>      <th>  Distribution:      </th>   <td>F(10,18235)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>5.0000</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>24.000</td>      <th>  F-statistic (robust):</th>   <td>2892.7</td>   
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Time periods:</th>            <td>24</td>        <th>  Distribution:      </th>   <td>F(10,18235)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>795.42</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Min Obs:</th>               <td>737.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>828.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>      
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>          <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>   <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>             <td>0.0321</td>    <td>0.0012</td>   <td>26.533</td>  <td>0.0000</td>    <td>0.0297</td>     <td>0.0344</td>  
</tr>
<tr>
  <th>did</th>               <td>0.0074</td>    <td>0.0002</td>   <td>31.884</td>  <td>0.0000</td>    <td>0.0069</td>     <td>0.0078</td>  
</tr>
<tr>
  <th>pct_chg</th>           <td>-0.0221</td>   <td>0.0005</td>   <td>-45.188</td> <td>0.0000</td>    <td>-0.0231</td>    <td>-0.0211</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>      <td>-0.0192</td>   <td>0.0005</td>   <td>-38.874</td> <td>0.0000</td>    <td>-0.0202</td>    <td>-0.0183</td> 
</tr>
<tr>
  <th>大股东持股比例</th>           <td>-0.0001</td>  <td>2.337e-05</td> <td>-5.8863</td> <td>0.0000</td>    <td>-0.0002</td>  <td>-9.174e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>   <td>0.0147</td>    <td>0.0002</td>   <td>92.518</td>  <td>0.0000</td>    <td>0.0143</td>     <td>0.0150</td>  
</tr>
<tr>
  <th>newBM</th>             <td>-0.0150</td>   <td>0.0007</td>   <td>-20.776</td> <td>0.0000</td>    <td>-0.0164</td>    <td>-0.0136</td> 
</tr>
<tr>
  <th>roe</th>             <td>-1.075e-05</td> <td>2.625e-06</td> <td>-4.0943</td> <td>0.0000</td>  <td>-1.589e-05</td> <td>-5.602e-06</td>
</tr>
<tr>
  <th>资产负债率</th>           <td>-5.009e-05</td> <td>1.495e-05</td> <td>-3.3506</td> <td>0.0008</td>   <td>-7.94e-05</td> <td>-2.079e-05</td>
</tr>
<tr>
  <th>skew</th>              <td>0.0011</td>    <td>0.0001</td>   <td>10.420</td>  <td>0.0000</td>    <td>0.0009</td>     <td>0.0014</td>  
</tr>
<tr>
  <th>kurt</th>              <td>-0.0010</td>  <td>4.547e-05</td> <td>-21.763</td> <td>0.0000</td>    <td>-0.0011</td>    <td>-0.0009</td> 
</tr>
</table><br/><br/>F-test for Poolability: 3.9099<br/>P-value: 0.0000<br/>Distribution: F(844,18235)<br/><br/>Included effects: Entity<br/>id: 0x1bf8601ff10




```python
fix_effect_model(X_short, y_short_2)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>          <td>swing</td>      <th>  R-squared:         </th>     <td>0.6632</td>   
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>-0.2592</td>  
</tr>
<tr>
  <th>No. Observations:</th>       <td>19090</td>      <th>  R-squared (Within):</th>     <td>0.6632</td>   
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.5799</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>10:53:56</td>     <th>  Log-likelihood     </th>    <td>5.748e+04</td> 
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>3590.2</td>   
</tr>
<tr>
  <th>Entities:</th>                <td>845</td>       <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Avg Obs:</th>               <td>22.592</td>      <th>  Distribution:      </th>   <td>F(10,18235)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>5.0000</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>24.000</td>      <th>  F-statistic (robust):</th>   <td>3590.2</td>   
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Time periods:</th>            <td>24</td>        <th>  Distribution:      </th>   <td>F(10,18235)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>795.42</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Min Obs:</th>               <td>737.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>828.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>      
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>          <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>   <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>             <td>0.0464</td>    <td>0.0014</td>   <td>33.829</td>  <td>0.0000</td>    <td>0.0437</td>     <td>0.0491</td>  
</tr>
<tr>
  <th>did</th>               <td>0.0086</td>    <td>0.0003</td>   <td>32.767</td>  <td>0.0000</td>    <td>0.0081</td>     <td>0.0091</td>  
</tr>
<tr>
  <th>pct_chg</th>           <td>-0.0199</td>   <td>0.0006</td>   <td>-35.752</td> <td>0.0000</td>    <td>-0.0209</td>    <td>-0.0188</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>      <td>-0.0133</td>   <td>0.0006</td>   <td>-23.669</td> <td>0.0000</td>    <td>-0.0144</td>    <td>-0.0122</td> 
</tr>
<tr>
  <th>大股东持股比例</th>           <td>-0.0001</td>  <td>2.652e-05</td> <td>-5.4840</td> <td>0.0000</td>    <td>-0.0002</td>  <td>-9.347e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>   <td>0.0181</td>    <td>0.0002</td>   <td>100.87</td>  <td>0.0000</td>    <td>0.0178</td>     <td>0.0185</td>  
</tr>
<tr>
  <th>newBM</th>             <td>-0.0217</td>   <td>0.0008</td>   <td>-26.509</td> <td>0.0000</td>    <td>-0.0233</td>    <td>-0.0201</td> 
</tr>
<tr>
  <th>roe</th>             <td>-1.033e-05</td> <td>2.979e-06</td> <td>-3.4679</td> <td>0.0005</td>  <td>-1.617e-05</td> <td>-4.492e-06</td>
</tr>
<tr>
  <th>资产负债率</th>           <td>-7.328e-05</td> <td>1.697e-05</td> <td>-4.3182</td> <td>0.0000</td>    <td>-0.0001</td>  <td>-4.002e-05</td>
</tr>
<tr>
  <th>skew</th>              <td>0.0009</td>    <td>0.0001</td>   <td>7.0277</td>  <td>0.0000</td>    <td>0.0006</td>     <td>0.0011</td>  
</tr>
<tr>
  <th>kurt</th>              <td>-0.0017</td>  <td>5.161e-05</td> <td>-33.690</td> <td>0.0000</td>    <td>-0.0018</td>    <td>-0.0016</td> 
</tr>
</table><br/><br/>F-test for Poolability: 5.1140<br/>P-value: 0.0000<br/>Distribution: F(844,18235)<br/><br/>Included effects: Entity<br/>id: 0x1bf8602e3a0



# 所有自变量


```python
df_drop['mv分3组'] = df_drop.groupby("交易月份")['lnmv'].apply(lambda x: pd.qcut(x, 3, labels=range(1,4)))
df_drop['mv分2组'] = df_drop.groupby("交易月份")['lnmv'].apply(lambda x: pd.qcut(x, 2, labels=[1, 2]))
```


```python
df_drop.groupby("mv分2组")[[*X_cols, *y_cols, 'lnmv']].corr()
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
      <th></th>
      <th>did</th>
      <th>pct_chg</th>
      <th>pct_chg_lag1</th>
      <th>大股东持股比例</th>
      <th>turnover_rate_f</th>
      <th>newBM</th>
      <th>roe</th>
      <th>资产负债率</th>
      <th>skew</th>
      <th>kurt</th>
      <th>std</th>
      <th>swing</th>
      <th>lnmv</th>
    </tr>
    <tr>
      <th>mv分2组</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="13" valign="top">1</th>
      <th>did</th>
      <td>1.000000</td>
      <td>-0.033612</td>
      <td>-0.020580</td>
      <td>0.032952</td>
      <td>0.149539</td>
      <td>-0.034671</td>
      <td>0.034402</td>
      <td>-0.034992</td>
      <td>-0.050605</td>
      <td>-0.023598</td>
      <td>0.174456</td>
      <td>0.155590</td>
      <td>0.500139</td>
    </tr>
    <tr>
      <th>pct_chg</th>
      <td>-0.033612</td>
      <td>1.000000</td>
      <td>-0.013191</td>
      <td>-0.010162</td>
      <td>0.126645</td>
      <td>-0.135662</td>
      <td>0.009639</td>
      <td>-0.002566</td>
      <td>0.210988</td>
      <td>0.085142</td>
      <td>-0.134803</td>
      <td>-0.102365</td>
      <td>0.095043</td>
    </tr>
    <tr>
      <th>pct_chg_lag1</th>
      <td>-0.020580</td>
      <td>-0.013191</td>
      <td>1.000000</td>
      <td>-0.000229</td>
      <td>0.162570</td>
      <td>-0.129901</td>
      <td>-0.008748</td>
      <td>-0.001153</td>
      <td>0.039639</td>
      <td>-0.014905</td>
      <td>-0.020427</td>
      <td>0.070218</td>
      <td>0.100879</td>
    </tr>
    <tr>
      <th>大股东持股比例</th>
      <td>0.032952</td>
      <td>-0.010162</td>
      <td>-0.000229</td>
      <td>1.000000</td>
      <td>0.019242</td>
      <td>0.164789</td>
      <td>0.026775</td>
      <td>0.046249</td>
      <td>-0.001413</td>
      <td>0.028496</td>
      <td>-0.025414</td>
      <td>-0.029688</td>
      <td>-0.053492</td>
    </tr>
    <tr>
      <th>turnover_rate_f</th>
      <td>0.149539</td>
      <td>0.126645</td>
      <td>0.162570</td>
      <td>0.019242</td>
      <td>1.000000</td>
      <td>-0.285587</td>
      <td>-0.033225</td>
      <td>-0.011546</td>
      <td>0.090443</td>
      <td>-0.145405</td>
      <td>0.597142</td>
      <td>0.628603</td>
      <td>0.278578</td>
    </tr>
    <tr>
      <th>newBM</th>
      <td>-0.034671</td>
      <td>-0.135662</td>
      <td>-0.129901</td>
      <td>0.164789</td>
      <td>-0.285587</td>
      <td>1.000000</td>
      <td>0.051490</td>
      <td>0.010055</td>
      <td>-0.071446</td>
      <td>0.062606</td>
      <td>-0.262982</td>
      <td>-0.308038</td>
      <td>-0.142827</td>
    </tr>
    <tr>
      <th>roe</th>
      <td>0.034402</td>
      <td>0.009639</td>
      <td>-0.008748</td>
      <td>0.026775</td>
      <td>-0.033225</td>
      <td>0.051490</td>
      <td>1.000000</td>
      <td>-0.134802</td>
      <td>-0.011807</td>
      <td>0.009328</td>
      <td>-0.047304</td>
      <td>-0.051202</td>
      <td>0.012359</td>
    </tr>
    <tr>
      <th>资产负债率</th>
      <td>-0.034992</td>
      <td>-0.002566</td>
      <td>-0.001153</td>
      <td>0.046249</td>
      <td>-0.011546</td>
      <td>0.010055</td>
      <td>-0.134802</td>
      <td>1.000000</td>
      <td>0.026288</td>
      <td>0.032349</td>
      <td>0.001915</td>
      <td>0.000939</td>
      <td>0.030509</td>
    </tr>
    <tr>
      <th>skew</th>
      <td>-0.050605</td>
      <td>0.210988</td>
      <td>0.039639</td>
      <td>-0.001413</td>
      <td>0.090443</td>
      <td>-0.071446</td>
      <td>-0.011807</td>
      <td>0.026288</td>
      <td>1.000000</td>
      <td>0.102779</td>
      <td>0.055350</td>
      <td>0.040072</td>
      <td>0.021357</td>
    </tr>
    <tr>
      <th>kurt</th>
      <td>-0.023598</td>
      <td>0.085142</td>
      <td>-0.014905</td>
      <td>0.028496</td>
      <td>-0.145405</td>
      <td>0.062606</td>
      <td>0.009328</td>
      <td>0.032349</td>
      <td>0.102779</td>
      <td>1.000000</td>
      <td>-0.226914</td>
      <td>-0.298411</td>
      <td>-0.040962</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.174456</td>
      <td>-0.134803</td>
      <td>-0.020427</td>
      <td>-0.025414</td>
      <td>0.597142</td>
      <td>-0.262982</td>
      <td>-0.047304</td>
      <td>0.001915</td>
      <td>0.055350</td>
      <td>-0.226914</td>
      <td>1.000000</td>
      <td>0.924479</td>
      <td>0.273450</td>
    </tr>
    <tr>
      <th>swing</th>
      <td>0.155590</td>
      <td>-0.102365</td>
      <td>0.070218</td>
      <td>-0.029688</td>
      <td>0.628603</td>
      <td>-0.308038</td>
      <td>-0.051202</td>
      <td>0.000939</td>
      <td>0.040072</td>
      <td>-0.298411</td>
      <td>0.924479</td>
      <td>1.000000</td>
      <td>0.280480</td>
    </tr>
    <tr>
      <th>lnmv</th>
      <td>0.500139</td>
      <td>0.095043</td>
      <td>0.100879</td>
      <td>-0.053492</td>
      <td>0.278578</td>
      <td>-0.142827</td>
      <td>0.012359</td>
      <td>0.030509</td>
      <td>0.021357</td>
      <td>-0.040962</td>
      <td>0.273450</td>
      <td>0.280480</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th rowspan="13" valign="top">2</th>
      <th>did</th>
      <td>1.000000</td>
      <td>-0.012117</td>
      <td>-0.005211</td>
      <td>0.004770</td>
      <td>0.267866</td>
      <td>-0.212783</td>
      <td>-0.008534</td>
      <td>-0.036332</td>
      <td>-0.083526</td>
      <td>-0.032879</td>
      <td>0.308861</td>
      <td>0.289477</td>
      <td>0.397159</td>
    </tr>
    <tr>
      <th>pct_chg</th>
      <td>-0.012117</td>
      <td>1.000000</td>
      <td>0.014684</td>
      <td>-0.016090</td>
      <td>0.205898</td>
      <td>-0.123800</td>
      <td>-0.000167</td>
      <td>0.004740</td>
      <td>0.222164</td>
      <td>0.047110</td>
      <td>-0.006923</td>
      <td>0.027936</td>
      <td>0.027631</td>
    </tr>
    <tr>
      <th>pct_chg_lag1</th>
      <td>-0.005211</td>
      <td>0.014684</td>
      <td>1.000000</td>
      <td>-0.019188</td>
      <td>0.229554</td>
      <td>-0.116609</td>
      <td>-0.018203</td>
      <td>0.005183</td>
      <td>0.033327</td>
      <td>-0.033810</td>
      <td>0.047426</td>
      <td>0.119713</td>
      <td>0.034909</td>
    </tr>
    <tr>
      <th>大股东持股比例</th>
      <td>0.004770</td>
      <td>-0.016090</td>
      <td>-0.019188</td>
      <td>1.000000</td>
      <td>-0.032899</td>
      <td>0.243260</td>
      <td>0.022459</td>
      <td>0.060439</td>
      <td>0.004637</td>
      <td>0.020252</td>
      <td>-0.071490</td>
      <td>-0.088693</td>
      <td>0.265072</td>
    </tr>
    <tr>
      <th>turnover_rate_f</th>
      <td>0.267866</td>
      <td>0.205898</td>
      <td>0.229554</td>
      <td>-0.032899</td>
      <td>1.000000</td>
      <td>-0.317681</td>
      <td>-0.063695</td>
      <td>-0.003881</td>
      <td>0.031738</td>
      <td>-0.147019</td>
      <td>0.628095</td>
      <td>0.660172</td>
      <td>0.042541</td>
    </tr>
    <tr>
      <th>newBM</th>
      <td>-0.212783</td>
      <td>-0.123800</td>
      <td>-0.116609</td>
      <td>0.243260</td>
      <td>-0.317681</td>
      <td>1.000000</td>
      <td>-0.052036</td>
      <td>0.208934</td>
      <td>-0.018507</td>
      <td>0.068836</td>
      <td>-0.326843</td>
      <td>-0.366377</td>
      <td>-0.004946</td>
    </tr>
    <tr>
      <th>roe</th>
      <td>-0.008534</td>
      <td>-0.000167</td>
      <td>-0.018203</td>
      <td>0.022459</td>
      <td>-0.063695</td>
      <td>-0.052036</td>
      <td>1.000000</td>
      <td>-0.072876</td>
      <td>0.026823</td>
      <td>-0.002655</td>
      <td>-0.063668</td>
      <td>-0.066637</td>
      <td>0.076247</td>
    </tr>
    <tr>
      <th>资产负债率</th>
      <td>-0.036332</td>
      <td>0.004740</td>
      <td>0.005183</td>
      <td>0.060439</td>
      <td>-0.003881</td>
      <td>0.208934</td>
      <td>-0.072876</td>
      <td>1.000000</td>
      <td>0.011183</td>
      <td>0.024605</td>
      <td>0.001990</td>
      <td>0.005449</td>
      <td>0.015412</td>
    </tr>
    <tr>
      <th>skew</th>
      <td>-0.083526</td>
      <td>0.222164</td>
      <td>0.033327</td>
      <td>0.004637</td>
      <td>0.031738</td>
      <td>-0.018507</td>
      <td>0.026823</td>
      <td>0.011183</td>
      <td>1.000000</td>
      <td>0.203025</td>
      <td>-0.013458</td>
      <td>-0.025851</td>
      <td>0.035585</td>
    </tr>
    <tr>
      <th>kurt</th>
      <td>-0.032879</td>
      <td>0.047110</td>
      <td>-0.033810</td>
      <td>0.020252</td>
      <td>-0.147019</td>
      <td>0.068836</td>
      <td>-0.002655</td>
      <td>0.024605</td>
      <td>0.203025</td>
      <td>1.000000</td>
      <td>-0.203178</td>
      <td>-0.273952</td>
      <td>-0.000740</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.308861</td>
      <td>-0.006923</td>
      <td>0.047426</td>
      <td>-0.071490</td>
      <td>0.628095</td>
      <td>-0.326843</td>
      <td>-0.063668</td>
      <td>0.001990</td>
      <td>-0.013458</td>
      <td>-0.203178</td>
      <td>1.000000</td>
      <td>0.935667</td>
      <td>0.045094</td>
    </tr>
    <tr>
      <th>swing</th>
      <td>0.289477</td>
      <td>0.027936</td>
      <td>0.119713</td>
      <td>-0.088693</td>
      <td>0.660172</td>
      <td>-0.366377</td>
      <td>-0.066637</td>
      <td>0.005449</td>
      <td>-0.025851</td>
      <td>-0.273952</td>
      <td>0.935667</td>
      <td>1.000000</td>
      <td>0.032119</td>
    </tr>
    <tr>
      <th>lnmv</th>
      <td>0.397159</td>
      <td>0.027631</td>
      <td>0.034909</td>
      <td>0.265072</td>
      <td>0.042541</td>
      <td>-0.004946</td>
      <td>0.076247</td>
      <td>0.015412</td>
      <td>0.035585</td>
      <td>-0.000740</td>
      <td>0.045094</td>
      <td>0.032119</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_drop_short_mv = df_drop[(df_drop.date >= '2013-11-01') & (df_drop.date <= '2015-11-30')]

df_dropMV3 = df_drop[df_drop['mv分3组'] == 3].set_index(['ts_code', 'date'])
df_dropMV1 = df_drop[df_drop['mv分3组'] == 1].set_index(['ts_code', 'date'])

df_drop_shortMV3 = df_drop_short_mv[df_drop_short_mv['mv分3组'] == 3].set_index(['ts_code', 'date'])
df_drop_shortMV1 = df_drop_short_mv[df_drop_short_mv['mv分3组'] == 1].set_index(['ts_code', 'date'])
```


```python
X_long = df_dropMV3[X_cols]
y_long_1 = df_dropMV3[y_cols[0]]
y_long_2 = df_dropMV3[y_cols[1]]


X_short = df_drop_shortMV3[X_cols]
y_short_1 = df_drop_shortMV3[y_cols[0]]
y_short_2 = df_drop_shortMV3[y_cols[1]]
```


```python
fix_effect_model(X_long, y_long_1)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>           <td>std</td>       <th>  R-squared:         </th>     <td>0.5043</td>   
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>0.5584</td>   
</tr>
<tr>
  <th>No. Observations:</th>       <td>12858</td>      <th>  R-squared (Within):</th>     <td>0.5043</td>   
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.5098</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>10:59:46</td>     <th>  Log-likelihood     </th>    <td>4.148e+04</td> 
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>1261.3</td>   
</tr>
<tr>
  <th>Entities:</th>                <td>451</td>       <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Avg Obs:</th>               <td>28.510</td>      <th>  Distribution:      </th>   <td>F(10,12397)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>1.0000</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>48.000</td>      <th>  F-statistic (robust):</th>   <td>1261.3</td>   
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Time periods:</th>            <td>48</td>        <th>  Distribution:      </th>   <td>F(10,12397)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>267.88</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Min Obs:</th>               <td>246.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>277.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>      
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>          <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>   <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>             <td>0.0210</td>    <td>0.0014</td>   <td>14.946</td>  <td>0.0000</td>    <td>0.0183</td>     <td>0.0238</td>  
</tr>
<tr>
  <th>did</th>               <td>0.0022</td>    <td>0.0002</td>   <td>9.9532</td>  <td>0.0000</td>    <td>0.0018</td>     <td>0.0026</td>  
</tr>
<tr>
  <th>pct_chg</th>           <td>-0.0173</td>   <td>0.0006</td>   <td>-29.114</td> <td>0.0000</td>    <td>-0.0185</td>    <td>-0.0161</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>      <td>-0.0128</td>   <td>0.0006</td>   <td>-21.852</td> <td>0.0000</td>    <td>-0.0140</td>    <td>-0.0117</td> 
</tr>
<tr>
  <th>大股东持股比例</th>          <td>9.384e-06</td> <td>2.256e-05</td> <td>0.4159</td>  <td>0.6775</td>  <td>-3.485e-05</td>  <td>5.361e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>   <td>0.0162</td>    <td>0.0002</td>   <td>80.620</td>  <td>0.0000</td>    <td>0.0158</td>     <td>0.0166</td>  
</tr>
<tr>
  <th>newBM</th>             <td>-0.0102</td>   <td>0.0007</td>   <td>-14.735</td> <td>0.0000</td>    <td>-0.0116</td>    <td>-0.0089</td> 
</tr>
<tr>
  <th>roe</th>             <td>-2.283e-05</td> <td>9.219e-06</td> <td>-2.4763</td> <td>0.0133</td>   <td>-4.09e-05</td> <td>-4.759e-06</td>
</tr>
<tr>
  <th>资产负债率</th>            <td>6.713e-06</td> <td>1.777e-05</td> <td>0.3777</td>  <td>0.7057</td>  <td>-2.813e-05</td>  <td>4.155e-05</td>
</tr>
<tr>
  <th>skew</th>              <td>0.0004</td>    <td>0.0001</td>   <td>3.6420</td>  <td>0.0003</td>    <td>0.0002</td>     <td>0.0007</td>  
</tr>
<tr>
  <th>kurt</th>              <td>-0.0006</td>  <td>4.974e-05</td> <td>-11.121</td> <td>0.0000</td>    <td>-0.0007</td>    <td>-0.0005</td> 
</tr>
</table><br/><br/>F-test for Poolability: 3.3650<br/>P-value: 0.0000<br/>Distribution: F(450,12397)<br/><br/>Included effects: Entity<br/>id: 0x1bf89f80a00




```python
fix_effect_model(X_long, y_long_2)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>          <td>swing</td>      <th>  R-squared:         </th>     <td>0.5531</td>   
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>0.5546</td>   
</tr>
<tr>
  <th>No. Observations:</th>       <td>12858</td>      <th>  R-squared (Within):</th>     <td>0.5531</td>   
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.5538</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>10:59:49</td>     <th>  Log-likelihood     </th>    <td>3.906e+04</td> 
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>1534.2</td>   
</tr>
<tr>
  <th>Entities:</th>                <td>451</td>       <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Avg Obs:</th>               <td>28.510</td>      <th>  Distribution:      </th>   <td>F(10,12397)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>1.0000</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>48.000</td>      <th>  F-statistic (robust):</th>   <td>1534.2</td>   
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Time periods:</th>            <td>48</td>        <th>  Distribution:      </th>   <td>F(10,12397)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>267.88</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Min Obs:</th>               <td>246.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>277.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>      
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>          <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>   <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>             <td>0.0319</td>    <td>0.0017</td>   <td>18.772</td>  <td>0.0000</td>    <td>0.0286</td>     <td>0.0352</td>  
</tr>
<tr>
  <th>did</th>               <td>0.0017</td>    <td>0.0003</td>   <td>6.4405</td>  <td>0.0000</td>    <td>0.0012</td>     <td>0.0022</td>  
</tr>
<tr>
  <th>pct_chg</th>           <td>-0.0174</td>   <td>0.0007</td>   <td>-24.258</td> <td>0.0000</td>    <td>-0.0188</td>    <td>-0.0160</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>      <td>-0.0086</td>   <td>0.0007</td>   <td>-12.208</td> <td>0.0000</td>    <td>-0.0100</td>    <td>-0.0073</td> 
</tr>
<tr>
  <th>大股东持股比例</th>          <td>1.026e-05</td> <td>2.724e-05</td> <td>0.3766</td>  <td>0.7065</td>  <td>-4.313e-05</td>  <td>6.364e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>   <td>0.0207</td>    <td>0.0002</td>   <td>85.084</td>  <td>0.0000</td>    <td>0.0202</td>     <td>0.0212</td>  
</tr>
<tr>
  <th>newBM</th>             <td>-0.0157</td>   <td>0.0008</td>   <td>-18.737</td> <td>0.0000</td>    <td>-0.0174</td>    <td>-0.0141</td> 
</tr>
<tr>
  <th>roe</th>             <td>-3.115e-05</td> <td>1.113e-05</td> <td>-2.7993</td> <td>0.0051</td>  <td>-5.296e-05</td> <td>-9.337e-06</td>
</tr>
<tr>
  <th>资产负债率</th>            <td>4.768e-05</td> <td>2.145e-05</td> <td>2.2226</td>  <td>0.0263</td>   <td>5.63e-06</td>   <td>8.974e-05</td>
</tr>
<tr>
  <th>skew</th>              <td>0.0002</td>    <td>0.0001</td>   <td>1.0475</td>  <td>0.2949</td>    <td>-0.0001</td>    <td>0.0004</td>  
</tr>
<tr>
  <th>kurt</th>              <td>-0.0014</td>  <td>6.003e-05</td> <td>-23.885</td> <td>0.0000</td>    <td>-0.0016</td>    <td>-0.0013</td> 
</tr>
</table><br/><br/>F-test for Poolability: 4.3410<br/>P-value: 0.0000<br/>Distribution: F(450,12397)<br/><br/>Included effects: Entity<br/>id: 0x1bf89f25b80




```python
fix_effect_model(X_short, y_short_1)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>           <td>std</td>       <th>  R-squared:         </th>     <td>0.6152</td>  
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>0.4933</td>  
</tr>
<tr>
  <th>No. Observations:</th>       <td>6364</td>       <th>  R-squared (Within):</th>     <td>0.6152</td>  
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.5956</td>  
</tr>
<tr>
  <th>Time:</th>                 <td>11:00:07</td>     <th>  Log-likelihood     </th>    <td>2.061e+04</td>
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>     
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>953.37</td>  
</tr>
<tr>
  <th>Entities:</th>                <td>392</td>       <th>  P-value            </th>     <td>0.0000</td>  
</tr>
<tr>
  <th>Avg Obs:</th>               <td>16.235</td>      <th>  Distribution:      </th>   <td>F(10,5962)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>1.0000</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Max Obs:</th>               <td>24.000</td>      <th>  F-statistic (robust):</th>   <td>953.37</td>  
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>  
</tr>
<tr>
  <th>Time periods:</th>            <td>24</td>        <th>  Distribution:      </th>   <td>F(10,5962)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>265.17</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Min Obs:</th>               <td>246.00</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Max Obs:</th>               <td>276.00</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>     
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>          <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>   <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>             <td>0.0254</td>    <td>0.0026</td>   <td>9.6494</td>  <td>0.0000</td>    <td>0.0202</td>     <td>0.0305</td>  
</tr>
<tr>
  <th>did</th>               <td>0.0092</td>    <td>0.0004</td>   <td>25.447</td>  <td>0.0000</td>    <td>0.0085</td>     <td>0.0099</td>  
</tr>
<tr>
  <th>pct_chg</th>           <td>-0.0201</td>   <td>0.0008</td>   <td>-26.038</td> <td>0.0000</td>    <td>-0.0216</td>    <td>-0.0186</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>      <td>-0.0166</td>   <td>0.0008</td>   <td>-21.257</td> <td>0.0000</td>    <td>-0.0181</td>    <td>-0.0151</td> 
</tr>
<tr>
  <th>大股东持股比例</th>         <td>-9.322e-05</td> <td>4.211e-05</td> <td>-2.2136</td> <td>0.0269</td>    <td>-0.0002</td>  <td>-1.067e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>   <td>0.0125</td>    <td>0.0003</td>   <td>43.505</td>  <td>0.0000</td>    <td>0.0119</td>     <td>0.0130</td>  
</tr>
<tr>
  <th>newBM</th>             <td>-0.0111</td>   <td>0.0011</td>   <td>-10.452</td> <td>0.0000</td>    <td>-0.0132</td>    <td>-0.0091</td> 
</tr>
<tr>
  <th>roe</th>              <td>2.16e-05</td>  <td>1.53e-05</td>  <td>1.4115</td>  <td>0.1582</td>  <td>-8.399e-06</td>  <td>5.159e-05</td>
</tr>
<tr>
  <th>资产负债率</th>            <td>2.796e-05</td> <td>3.542e-05</td> <td>0.7894</td>  <td>0.4299</td>  <td>-4.148e-05</td>  <td>9.74e-05</td> 
</tr>
<tr>
  <th>skew</th>              <td>0.0011</td>    <td>0.0002</td>   <td>6.0300</td>  <td>0.0000</td>    <td>0.0008</td>     <td>0.0015</td>  
</tr>
<tr>
  <th>kurt</th>              <td>-0.0007</td>  <td>7.474e-05</td> <td>-9.2429</td> <td>0.0000</td>    <td>-0.0008</td>    <td>-0.0005</td> 
</tr>
</table><br/><br/>F-test for Poolability: 3.3538<br/>P-value: 0.0000<br/>Distribution: F(391,5962)<br/><br/>Included effects: Entity<br/>id: 0x1bf89d2e8e0




```python
fix_effect_model(X_short, y_short_2)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>          <td>swing</td>      <th>  R-squared:         </th>     <td>0.6699</td>  
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>0.5480</td>  
</tr>
<tr>
  <th>No. Observations:</th>       <td>6364</td>       <th>  R-squared (Within):</th>     <td>0.6699</td>  
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.6411</td>  
</tr>
<tr>
  <th>Time:</th>                 <td>11:00:17</td>     <th>  Log-likelihood     </th>    <td>1.967e+04</td>
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>     
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>1209.7</td>  
</tr>
<tr>
  <th>Entities:</th>                <td>392</td>       <th>  P-value            </th>     <td>0.0000</td>  
</tr>
<tr>
  <th>Avg Obs:</th>               <td>16.235</td>      <th>  Distribution:      </th>   <td>F(10,5962)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>1.0000</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Max Obs:</th>               <td>24.000</td>      <th>  F-statistic (robust):</th>   <td>1209.7</td>  
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>  
</tr>
<tr>
  <th>Time periods:</th>            <td>24</td>        <th>  Distribution:      </th>   <td>F(10,5962)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>265.17</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Min Obs:</th>               <td>246.00</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Max Obs:</th>               <td>276.00</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>     
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>         <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>   <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>            <td>0.0367</td>    <td>0.0031</td>   <td>12.039</td>  <td>0.0000</td>    <td>0.0307</td>     <td>0.0427</td>  
</tr>
<tr>
  <th>did</th>              <td>0.0108</td>    <td>0.0004</td>   <td>25.738</td>  <td>0.0000</td>    <td>0.0100</td>     <td>0.0116</td>  
</tr>
<tr>
  <th>pct_chg</th>          <td>-0.0178</td>   <td>0.0009</td>   <td>-19.938</td> <td>0.0000</td>    <td>-0.0196</td>    <td>-0.0161</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>     <td>-0.0136</td>   <td>0.0009</td>   <td>-14.966</td> <td>0.0000</td>    <td>-0.0153</td>    <td>-0.0118</td> 
</tr>
<tr>
  <th>大股东持股比例</th>          <td>-0.0001</td>  <td>4.887e-05</td> <td>-2.9056</td> <td>0.0037</td>    <td>-0.0002</td>  <td>-4.619e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>  <td>0.0161</td>    <td>0.0003</td>   <td>48.554</td>  <td>0.0000</td>    <td>0.0155</td>     <td>0.0168</td>  
</tr>
<tr>
  <th>newBM</th>            <td>-0.0163</td>   <td>0.0012</td>   <td>-13.181</td> <td>0.0000</td>    <td>-0.0187</td>    <td>-0.0139</td> 
</tr>
<tr>
  <th>roe</th>             <td>2.494e-05</td> <td>1.776e-05</td> <td>1.4044</td>  <td>0.1603</td>  <td>-9.872e-06</td>  <td>5.975e-05</td>
</tr>
<tr>
  <th>资产负债率</th>           <td>8.624e-05</td> <td>4.111e-05</td> <td>2.0980</td>  <td>0.0359</td>   <td>5.659e-06</td>   <td>0.0002</td>  
</tr>
<tr>
  <th>skew</th>             <td>0.0010</td>    <td>0.0002</td>   <td>4.5607</td>  <td>0.0000</td>    <td>0.0006</td>     <td>0.0014</td>  
</tr>
<tr>
  <th>kurt</th>             <td>-0.0015</td>  <td>8.673e-05</td> <td>-17.161</td> <td>0.0000</td>    <td>-0.0017</td>    <td>-0.0013</td> 
</tr>
</table><br/><br/>F-test for Poolability: 4.4432<br/>P-value: 0.0000<br/>Distribution: F(391,5962)<br/><br/>Included effects: Entity<br/>id: 0x1bf89cfefa0




```python
X_long = df_dropMV1[X_cols]
y_long_1 = df_dropMV1[y_cols[0]]
y_long_2 = df_dropMV1[y_cols[1]]


X_short = df_drop_shortMV1[X_cols]
y_short_1 = df_drop_shortMV1[y_cols[0]]
y_short_2 = df_drop_shortMV1[y_cols[1]]
```


```python
fix_effect_model(X_long, y_long_1)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>           <td>std</td>       <th>  R-squared:         </th>     <td>0.5214</td>   
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>0.4010</td>   
</tr>
<tr>
  <th>No. Observations:</th>       <td>12870</td>      <th>  R-squared (Within):</th>     <td>0.5214</td>   
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.4915</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>11:01:00</td>     <th>  Log-likelihood     </th>    <td>4.092e+04</td> 
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>1349.3</td>   
</tr>
<tr>
  <th>Entities:</th>                <td>474</td>       <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Avg Obs:</th>               <td>27.152</td>      <th>  Distribution:      </th>   <td>F(10,12386)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>1.0000</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>48.000</td>      <th>  F-statistic (robust):</th>   <td>1349.3</td>   
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Time periods:</th>            <td>48</td>        <th>  Distribution:      </th>   <td>F(10,12386)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>268.12</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Min Obs:</th>               <td>246.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>277.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>      
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>          <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>  <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>             <td>0.0202</td>    <td>0.0009</td>   <td>21.517</td>  <td>0.0000</td>    <td>0.0184</td>    <td>0.0221</td>  
</tr>
<tr>
  <th>did</th>               <td>0.0035</td>    <td>0.0004</td>   <td>8.9269</td>  <td>0.0000</td>    <td>0.0027</td>    <td>0.0043</td>  
</tr>
<tr>
  <th>pct_chg</th>           <td>-0.0285</td>   <td>0.0006</td>   <td>-44.023</td> <td>0.0000</td>    <td>-0.0298</td>   <td>-0.0272</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>      <td>-0.0182</td>   <td>0.0006</td>   <td>-28.998</td> <td>0.0000</td>    <td>-0.0194</td>   <td>-0.0170</td> 
</tr>
<tr>
  <th>大股东持股比例</th>          <td>2.409e-05</td> <td>1.985e-05</td> <td>1.2133</td>  <td>0.2250</td>  <td>-1.483e-05</td> <td>6.301e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>   <td>0.0157</td>    <td>0.0002</td>   <td>87.470</td>  <td>0.0000</td>    <td>0.0154</td>    <td>0.0161</td>  
</tr>
<tr>
  <th>newBM</th>             <td>-0.0131</td>   <td>0.0009</td>   <td>-14.341</td> <td>0.0000</td>    <td>-0.0149</td>   <td>-0.0113</td> 
</tr>
<tr>
  <th>roe</th>             <td>-2.936e-06</td> <td>1.905e-06</td> <td>-1.5411</td> <td>0.1233</td>   <td>-6.67e-06</td> <td>7.982e-07</td>
</tr>
<tr>
  <th>资产负债率</th>            <td>1.329e-05</td> <td>1.174e-05</td> <td>1.1319</td>  <td>0.2577</td>  <td>-9.726e-06</td> <td>3.631e-05</td>
</tr>
<tr>
  <th>skew</th>              <td>0.0009</td>    <td>0.0001</td>   <td>7.9997</td>  <td>0.0000</td>    <td>0.0007</td>    <td>0.0012</td>  
</tr>
<tr>
  <th>kurt</th>              <td>-0.0007</td>  <td>4.926e-05</td> <td>-14.319</td> <td>0.0000</td>    <td>-0.0008</td>   <td>-0.0006</td> 
</tr>
</table><br/><br/>F-test for Poolability: 3.2644<br/>P-value: 0.0000<br/>Distribution: F(473,12386)<br/><br/>Included effects: Entity<br/>id: 0x1bf89d2e760




```python
fix_effect_model(X_long, y_long_2)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>          <td>swing</td>      <th>  R-squared:         </th>     <td>0.5592</td>   
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>0.3511</td>   
</tr>
<tr>
  <th>No. Observations:</th>       <td>12870</td>      <th>  R-squared (Within):</th>     <td>0.5592</td>   
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.5218</td>   
</tr>
<tr>
  <th>Time:</th>                 <td>11:01:01</td>     <th>  Log-likelihood     </th>    <td>3.908e+04</td> 
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>1571.0</td>   
</tr>
<tr>
  <th>Entities:</th>                <td>474</td>       <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Avg Obs:</th>               <td>27.152</td>      <th>  Distribution:      </th>   <td>F(10,12386)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>1.0000</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>48.000</td>      <th>  F-statistic (robust):</th>   <td>1571.0</td>   
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>   
</tr>
<tr>
  <th>Time periods:</th>            <td>48</td>        <th>  Distribution:      </th>   <td>F(10,12386)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>268.12</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Min Obs:</th>               <td>246.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th>Max Obs:</th>               <td>277.00</td>      <th>                     </th>        <td></td>      
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>      
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>          <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>  <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>             <td>0.0321</td>    <td>0.0011</td>   <td>29.620</td>  <td>0.0000</td>    <td>0.0300</td>    <td>0.0342</td>  
</tr>
<tr>
  <th>did</th>               <td>0.0041</td>    <td>0.0005</td>   <td>9.0420</td>  <td>0.0000</td>    <td>0.0032</td>    <td>0.0050</td>  
</tr>
<tr>
  <th>pct_chg</th>           <td>-0.0281</td>   <td>0.0007</td>   <td>-37.637</td> <td>0.0000</td>    <td>-0.0296</td>   <td>-0.0266</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>      <td>-0.0118</td>   <td>0.0007</td>   <td>-16.243</td> <td>0.0000</td>    <td>-0.0132</td>   <td>-0.0103</td> 
</tr>
<tr>
  <th>大股东持股比例</th>          <td>4.967e-05</td> <td>2.29e-05</td>  <td>2.1690</td>  <td>0.0301</td>   <td>4.782e-06</td> <td>9.455e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>   <td>0.0191</td>    <td>0.0002</td>   <td>92.031</td>  <td>0.0000</td>    <td>0.0187</td>    <td>0.0195</td>  
</tr>
<tr>
  <th>newBM</th>             <td>-0.0179</td>   <td>0.0011</td>   <td>-17.024</td> <td>0.0000</td>    <td>-0.0200</td>   <td>-0.0159</td> 
</tr>
<tr>
  <th>roe</th>             <td>-4.155e-06</td> <td>2.197e-06</td> <td>-1.8911</td> <td>0.0586</td>  <td>-8.461e-06</td> <td>1.517e-07</td>
</tr>
<tr>
  <th>资产负债率</th>            <td>5.024e-06</td> <td>1.354e-05</td> <td>0.3710</td>  <td>0.7107</td>  <td>-2.152e-05</td> <td>3.157e-05</td>
</tr>
<tr>
  <th>skew</th>              <td>0.0005</td>    <td>0.0001</td>   <td>3.8207</td>  <td>0.0001</td>    <td>0.0003</td>    <td>0.0008</td>  
</tr>
<tr>
  <th>kurt</th>              <td>-0.0016</td>  <td>5.681e-05</td> <td>-27.559</td> <td>0.0000</td>    <td>-0.0017</td>   <td>-0.0015</td> 
</tr>
</table><br/><br/>F-test for Poolability: 4.0825<br/>P-value: 0.0000<br/>Distribution: F(473,12386)<br/><br/>Included effects: Entity<br/>id: 0x1bf89ce4970




```python
fix_effect_model(X_short, y_short_1)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>           <td>std</td>       <th>  R-squared:         </th>     <td>0.6167</td>  
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>0.4132</td>  
</tr>
<tr>
  <th>No. Observations:</th>       <td>6370</td>       <th>  R-squared (Within):</th>     <td>0.6167</td>  
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.5343</td>  
</tr>
<tr>
  <th>Time:</th>                 <td>11:01:01</td>     <th>  Log-likelihood     </th>    <td>2.01e+04</td> 
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>     
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>954.67</td>  
</tr>
<tr>
  <th>Entities:</th>                <td>426</td>       <th>  P-value            </th>     <td>0.0000</td>  
</tr>
<tr>
  <th>Avg Obs:</th>               <td>14.953</td>      <th>  Distribution:      </th>   <td>F(10,5934)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>1.0000</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Max Obs:</th>               <td>24.000</td>      <th>  F-statistic (robust):</th>   <td>954.67</td>  
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>  
</tr>
<tr>
  <th>Time periods:</th>            <td>24</td>        <th>  Distribution:      </th>   <td>F(10,5934)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>265.42</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Min Obs:</th>               <td>246.00</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Max Obs:</th>               <td>276.00</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>     
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>          <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>   <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>             <td>0.0316</td>    <td>0.0017</td>   <td>18.087</td>  <td>0.0000</td>    <td>0.0282</td>     <td>0.0350</td>  
</tr>
<tr>
  <th>did</th>               <td>0.0055</td>    <td>0.0006</td>   <td>9.5328</td>  <td>0.0000</td>    <td>0.0044</td>     <td>0.0066</td>  
</tr>
<tr>
  <th>pct_chg</th>           <td>-0.0274</td>   <td>0.0009</td>   <td>-30.069</td> <td>0.0000</td>    <td>-0.0292</td>    <td>-0.0256</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>      <td>-0.0237</td>   <td>0.0009</td>   <td>-25.887</td> <td>0.0000</td>    <td>-0.0255</td>    <td>-0.0219</td> 
</tr>
<tr>
  <th>大股东持股比例</th>         <td>-2.378e-05</td> <td>3.805e-05</td> <td>-0.6249</td> <td>0.5321</td>  <td>-9.837e-05</td>  <td>5.082e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>   <td>0.0163</td>    <td>0.0003</td>   <td>60.735</td>  <td>0.0000</td>    <td>0.0158</td>     <td>0.0168</td>  
</tr>
<tr>
  <th>newBM</th>             <td>-0.0250</td>   <td>0.0016</td>   <td>-16.105</td> <td>0.0000</td>    <td>-0.0280</td>    <td>-0.0219</td> 
</tr>
<tr>
  <th>roe</th>             <td>-8.068e-06</td> <td>2.758e-06</td> <td>-2.9256</td> <td>0.0035</td>  <td>-1.347e-05</td> <td>-2.662e-06</td>
</tr>
<tr>
  <th>资产负债率</th>           <td>-8.232e-05</td> <td>2.287e-05</td> <td>-3.5997</td> <td>0.0003</td>    <td>-0.0001</td>  <td>-3.749e-05</td>
</tr>
<tr>
  <th>skew</th>              <td>0.0009</td>    <td>0.0002</td>   <td>5.1445</td>  <td>0.0000</td>    <td>0.0006</td>     <td>0.0013</td>  
</tr>
<tr>
  <th>kurt</th>              <td>-0.0008</td>  <td>7.547e-05</td> <td>-10.331</td> <td>0.0000</td>    <td>-0.0009</td>    <td>-0.0006</td> 
</tr>
</table><br/><br/>F-test for Poolability: 3.3693<br/>P-value: 0.0000<br/>Distribution: F(425,5934)<br/><br/>Included effects: Entity<br/>id: 0x1bf89f251c0




```python
fix_effect_model(X_short, y_short_2)
```




<table class="simpletable">
<caption>PanelOLS Estimation Summary</caption>
<tr>
  <th>Dep. Variable:</th>          <td>swing</td>      <th>  R-squared:         </th>     <td>0.6665</td>  
</tr>
<tr>
  <th>Estimator:</th>            <td>PanelOLS</td>     <th>  R-squared (Between):</th>    <td>0.3421</td>  
</tr>
<tr>
  <th>No. Observations:</th>       <td>6370</td>       <th>  R-squared (Within):</th>     <td>0.6665</td>  
</tr>
<tr>
  <th>Date:</th>             <td>Sat, May 15 2021</td> <th>  R-squared (Overall):</th>    <td>0.5621</td>  
</tr>
<tr>
  <th>Time:</th>                 <td>11:01:01</td>     <th>  Log-likelihood     </th>    <td>1.945e+04</td>
</tr>
<tr>
  <th>Cov. Estimator:</th>      <td>Unadjusted</td>    <th>                     </th>        <td></td>     
</tr>
<tr>
  <th></th>                          <td></td>         <th>  F-statistic:       </th>     <td>1185.7</td>  
</tr>
<tr>
  <th>Entities:</th>                <td>426</td>       <th>  P-value            </th>     <td>0.0000</td>  
</tr>
<tr>
  <th>Avg Obs:</th>               <td>14.953</td>      <th>  Distribution:      </th>   <td>F(10,5934)</td>
</tr>
<tr>
  <th>Min Obs:</th>               <td>1.0000</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Max Obs:</th>               <td>24.000</td>      <th>  F-statistic (robust):</th>   <td>1185.7</td>  
</tr>
<tr>
  <th></th>                          <td></td>         <th>  P-value            </th>     <td>0.0000</td>  
</tr>
<tr>
  <th>Time periods:</th>            <td>24</td>        <th>  Distribution:      </th>   <td>F(10,5934)</td>
</tr>
<tr>
  <th>Avg Obs:</th>               <td>265.42</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Min Obs:</th>               <td>246.00</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th>Max Obs:</th>               <td>276.00</td>      <th>                     </th>        <td></td>     
</tr>
<tr>
  <th></th>                          <td></td>         <th>                     </th>        <td></td>     
</tr>
</table>
<table class="simpletable">
<caption>Parameter Estimates</caption>
<tr>
         <td></td>          <th>Parameter</th> <th>Std. Err.</th> <th>T-stat</th>  <th>P-value</th>  <th>Lower CI</th>   <th>Upper CI</th> 
</tr>
<tr>
  <th>const</th>             <td>0.0455</td>    <td>0.0019</td>   <td>23.520</td>  <td>0.0000</td>    <td>0.0417</td>     <td>0.0493</td>  
</tr>
<tr>
  <th>did</th>               <td>0.0067</td>    <td>0.0006</td>   <td>10.514</td>  <td>0.0000</td>    <td>0.0054</td>     <td>0.0079</td>  
</tr>
<tr>
  <th>pct_chg</th>           <td>-0.0236</td>   <td>0.0010</td>   <td>-23.336</td> <td>0.0000</td>    <td>-0.0256</td>    <td>-0.0216</td> 
</tr>
<tr>
  <th>pct_chg_lag1</th>      <td>-0.0168</td>   <td>0.0010</td>   <td>-16.554</td> <td>0.0000</td>    <td>-0.0188</td>    <td>-0.0148</td> 
</tr>
<tr>
  <th>大股东持股比例</th>          <td>1.37e-05</td>  <td>4.214e-05</td> <td>0.3251</td>  <td>0.7451</td>  <td>-6.892e-05</td>  <td>9.632e-05</td>
</tr>
<tr>
  <th>turnover_rate_f</th>   <td>0.0200</td>    <td>0.0003</td>   <td>67.503</td>  <td>0.0000</td>    <td>0.0195</td>     <td>0.0206</td>  
</tr>
<tr>
  <th>newBM</th>             <td>-0.0336</td>   <td>0.0017</td>   <td>-19.582</td> <td>0.0000</td>    <td>-0.0370</td>    <td>-0.0303</td> 
</tr>
<tr>
  <th>roe</th>             <td>-8.797e-06</td> <td>3.054e-06</td> <td>-2.8803</td> <td>0.0040</td>  <td>-1.478e-05</td>  <td>-2.81e-06</td>
</tr>
<tr>
  <th>资产负债率</th>             <td>-0.0001</td>  <td>2.533e-05</td> <td>-5.1776</td> <td>0.0000</td>    <td>-0.0002</td>  <td>-8.149e-05</td>
</tr>
<tr>
  <th>skew</th>              <td>0.0004</td>    <td>0.0002</td>   <td>1.9127</td>  <td>0.0558</td>  <td>-9.417e-06</td>   <td>0.0008</td>  
</tr>
<tr>
  <th>kurt</th>              <td>-0.0015</td>  <td>8.359e-05</td> <td>-17.752</td> <td>0.0000</td>    <td>-0.0016</td>    <td>-0.0013</td> 
</tr>
</table><br/><br/>F-test for Poolability: 4.3621<br/>P-value: 0.0000<br/>Distribution: F(425,5934)<br/><br/>Included effects: Entity<br/>id: 0x1bf89f3bf70




```python

```


```python
df_drop.to_excel("最终使用的数据.xlsx", index=None)
```


```python

```
