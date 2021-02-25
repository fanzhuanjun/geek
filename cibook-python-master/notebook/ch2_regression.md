```python
import pandas as pd
import statsmodels.api as sm
import joblib
import os

import warnings
warnings.filterwarnings('ignore')
```

## セレクションバイアスのあるデータの作成


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

## (6) バイアスのあるデータでの回帰分析


```python
## 回帰分析の実行
y = biased_df.spend
X = biased_df[['treatment', 'history']]
X = sm.add_constant(X) # statsmodelsではβ0を明示的に入れてあげる必要がある
model = sm.OLS(y, X)
results = model.fit()
```


```python
## 分析結果のレポート
summary = results.summary()
summary
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>          <td>spend</td>      <th>  R-squared:         </th>  <td>   0.001</td>  
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th>  <td>   0.001</td>  
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th>  <td>   20.45</td>  
</tr>
<tr>
  <th>Date:</th>             <td>Wed, 10 Feb 2021</td> <th>  Prob (F-statistic):</th>  <td>1.32e-09</td>  
</tr>
<tr>
  <th>Time:</th>                 <td>15:46:53</td>     <th>  Log-Likelihood:    </th> <td>-1.3312e+05</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td> 31925</td>      <th>  AIC:               </th>  <td>2.663e+05</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td> 31922</td>      <th>  BIC:               </th>  <td>2.663e+05</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>     2</td>      <th>                     </th>      <td> </td>     
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>      <td> </td>     
</tr>
</table>
<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.3413</td> <td>    0.147</td> <td>    2.327</td> <td> 0.020</td> <td>    0.054</td> <td>    0.629</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.9088</td> <td>    0.177</td> <td>    5.122</td> <td> 0.000</td> <td>    0.561</td> <td>    1.257</td>
</tr>
<tr>
  <th>history</th>   <td>    0.0011</td> <td>    0.000</td> <td>    3.096</td> <td> 0.002</td> <td>    0.000</td> <td>    0.002</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>70760.532</td> <th>  Durbin-Watson:     </th>   <td>   2.002</td>   
</tr>
<tr>
  <th>Prob(Omnibus):</th>  <td> 0.000</td>   <th>  Jarque-Bera (JB):  </th> <td>352134568.791</td>
</tr>
<tr>
  <th>Skew:</th>           <td>20.807</td>   <th>  Prob(JB):          </th>   <td>    0.00</td>   
</tr>
<tr>
  <th>Kurtosis:</th>       <td>515.825</td>  <th>  Cond. No.          </th>   <td>    833.</td>   
</tr>
</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.




```python
## 推定されたパラメーターの取り出し
biased_reg_coef = summary.tables[1]
biased_reg_coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.3413</td> <td>    0.147</td> <td>    2.327</td> <td> 0.020</td> <td>    0.054</td> <td>    0.629</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.9088</td> <td>    0.177</td> <td>    5.122</td> <td> 0.000</td> <td>    0.561</td> <td>    1.257</td>
</tr>
<tr>
  <th>history</th>   <td>    0.0011</td> <td>    0.000</td> <td>    3.096</td> <td> 0.002</td> <td>    0.000</td> <td>    0.002</td>
</tr>
</table>



## (7) RCTデータでの回帰分析とバイアスのあるデータでの回帰分析の比較


```python
## RCTデータでの単回帰
y = male_df.spend
X = male_df[['treatment']]
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
rct_reg_coef = results.summary().tables[1]
rct_reg_coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.6528</td> <td>    0.103</td> <td>    6.356</td> <td> 0.000</td> <td>    0.451</td> <td>    0.854</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.7698</td> <td>    0.145</td> <td>    5.300</td> <td> 0.000</td> <td>    0.485</td> <td>    1.055</td>
</tr>
</table>




```python
## バイアスのあるデータでの単回帰
y = biased_df.spend
X = biased_df[['treatment']]
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
nonrct_reg_coef = results.summary().tables[1]
nonrct_reg_coef
```




<table class="simpletable">
<tr>
      <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>     <td>    0.5580</td> <td>    0.129</td> <td>    4.328</td> <td> 0.000</td> <td>    0.305</td> <td>    0.811</td>
</tr>
<tr>
  <th>treatment</th> <td>    0.9837</td> <td>    0.176</td> <td>    5.596</td> <td> 0.000</td> <td>    0.639</td> <td>    1.328</td>
</tr>
</table>




```python
## バイアスのあるデータでの重回帰
y = biased_df.spend
# R lmではカテゴリ変数は自動的にダミー変数化されているのでそれを再現
X = pd.get_dummies(biased_df[['treatment', 'recency', 'channel', 'history']], columns=['channel'], drop_first=True)
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
nonrct_mreg_coef = results.summary().tables[1]
nonrct_mreg_coef
```




<table class="simpletable">
<tr>
        <td></td>           <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>         <td>    0.4761</td> <td>    0.386</td> <td>    1.233</td> <td> 0.218</td> <td>   -0.281</td> <td>    1.233</td>
</tr>
<tr>
  <th>treatment</th>     <td>    0.8617</td> <td>    0.181</td> <td>    4.750</td> <td> 0.000</td> <td>    0.506</td> <td>    1.217</td>
</tr>
<tr>
  <th>recency</th>       <td>   -0.0361</td> <td>    0.026</td> <td>   -1.372</td> <td> 0.170</td> <td>   -0.088</td> <td>    0.015</td>
</tr>
<tr>
  <th>history</th>       <td>    0.0010</td> <td>    0.000</td> <td>    2.655</td> <td> 0.008</td> <td>    0.000</td> <td>    0.002</td>
</tr>
<tr>
  <th>channel_Phone</th> <td>   -0.0079</td> <td>    0.310</td> <td>   -0.025</td> <td> 0.980</td> <td>   -0.616</td> <td>    0.600</td>
</tr>
<tr>
  <th>channel_Web</th>   <td>    0.2540</td> <td>    0.310</td> <td>    0.820</td> <td> 0.412</td> <td>   -0.353</td> <td>    0.861</td>
</tr>
</table>



## (8) OVBの確認


```python
## (a) history抜きの回帰分析とパラメーターの取り出し
y = biased_df.spend
X = pd.get_dummies(biased_df[['treatment', 'recency', 'channel']], columns=['channel'], drop_first=True)
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
short_coef = results.summary().tables[1]
short_coef_df = pd.read_html(short_coef.as_html(), header=0, index_col=0)[0] #SimpleTableは扱いなれてないのでpandas DataFrameにする

## aの結果から介入効果に関するパラメーターのみを取り出す
alpha_1 = results.params['treatment'] # summaryのデータは小数点が四捨五入されているため、正確な値をとってくる

```


```python
## (b) historyを追加した回帰分析とパラメーターの取り出し
y = biased_df.spend
X = pd.get_dummies(biased_df[['treatment', 'recency', 'channel', 'history']], columns=['channel'], drop_first=True)
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
long_coef = results.summary().tables[1]
long_coef_df = pd.read_html(long_coef.as_html(), header=0, index_col=0)[0] #SimpleTableは扱いなれてないのでpandas DataFrameにする

## bの結果から介入とhistoryに関するパラメーターを取り出す
beta_1 = results.params['treatment']
beta_2 = results.params['history']
```


```python
## (c) 脱落した変数と介入変数での回帰分析
y = biased_df.history
X = pd.get_dummies(biased_df[['treatment', 'recency', 'channel']], columns=['channel'], drop_first=True)
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
omitted_coef = results.summary().tables[1]
omitted_coef_df = pd.read_html(omitted_coef.as_html(), header=0, index_col=0)[0] #SimpleTableは扱いなれてないのでpandas DataFrameにする
gamma_1 = results.params['treatment']
```


```python
## OVBの確認
print(beta_2 * gamma_1)
print(alpha_1 - beta_1)
```

    0.028816423676831623
    0.028816423676829572
    

## (10) 入れてはいけない変数を入れてみる


```python
## visitとtreatmentの相関
y = biased_df.treatment
X = pd.get_dummies(biased_df[['visit', 'channel', 'recency', 'history']], columns=['channel'], drop_first=True)
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
results.summary().tables[1]
```




<table class="simpletable">
<tr>
        <td></td>           <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>         <td>    0.7153</td> <td>    0.011</td> <td>   63.968</td> <td> 0.000</td> <td>    0.693</td> <td>    0.737</td>
</tr>
<tr>
  <th>visit</th>         <td>    0.1509</td> <td>    0.008</td> <td>   19.820</td> <td> 0.000</td> <td>    0.136</td> <td>    0.166</td>
</tr>
<tr>
  <th>recency</th>       <td>   -0.0282</td> <td>    0.001</td> <td>  -35.621</td> <td> 0.000</td> <td>   -0.030</td> <td>   -0.027</td>
</tr>
<tr>
  <th>history</th>       <td>    0.0001</td> <td> 1.17e-05</td> <td>    9.705</td> <td> 0.000</td> <td> 9.06e-05</td> <td>    0.000</td>
</tr>
<tr>
  <th>channel_Phone</th> <td>   -0.0708</td> <td>    0.009</td> <td>   -7.453</td> <td> 0.000</td> <td>   -0.089</td> <td>   -0.052</td>
</tr>
<tr>
  <th>channel_Web</th>   <td>   -0.0771</td> <td>    0.009</td> <td>   -8.131</td> <td> 0.000</td> <td>   -0.096</td> <td>   -0.059</td>
</tr>
</table>




```python
# visitを入れた回帰分析を実行
y = biased_df.spend
X = pd.get_dummies(biased_df[['treatment', 'channel', 'recency', 'history', 'visit']], columns=['channel'], drop_first=True)
X = sm.add_constant(X)
results = sm.OLS(y, X).fit()
results.summary().tables[1]
```




<table class="simpletable">
<tr>
        <td></td>           <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>         <td>   -0.4057</td> <td>    0.382</td> <td>   -1.062</td> <td> 0.288</td> <td>   -1.155</td> <td>    0.343</td>
</tr>
<tr>
  <th>treatment</th>     <td>    0.2784</td> <td>    0.180</td> <td>    1.546</td> <td> 0.122</td> <td>   -0.075</td> <td>    0.631</td>
</tr>
<tr>
  <th>recency</th>       <td>    0.0090</td> <td>    0.026</td> <td>    0.346</td> <td> 0.729</td> <td>   -0.042</td> <td>    0.060</td>
</tr>
<tr>
  <th>history</th>       <td>    0.0005</td> <td>    0.000</td> <td>    1.316</td> <td> 0.188</td> <td>   -0.000</td> <td>    0.001</td>
</tr>
<tr>
  <th>visit</th>         <td>    7.2368</td> <td>    0.246</td> <td>   29.368</td> <td> 0.000</td> <td>    6.754</td> <td>    7.720</td>
</tr>
<tr>
  <th>channel_Phone</th> <td>    0.0978</td> <td>    0.306</td> <td>    0.320</td> <td> 0.749</td> <td>   -0.502</td> <td>    0.697</td>
</tr>
<tr>
  <th>channel_Web</th>   <td>    0.1160</td> <td>    0.306</td> <td>    0.380</td> <td> 0.704</td> <td>   -0.483</td> <td>    0.715</td>
</tr>
</table>


