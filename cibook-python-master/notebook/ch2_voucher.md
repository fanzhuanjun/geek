```python
import pandas as pd
import statsmodels.api as sm
import plotly.express as px

from rpy2.robjects import r, pandas2ri
from rpy2.robjects.packages import importr
pandas2ri.activate()

import rdata

import warnings
warnings.filterwarnings('ignore')
```

## rdaファイルを読み込む方法

### 1. rpy2を使ってR経由でDataFrameに変換する
#### 事前の環境構築（Ubuntu18.04）
Rのインストールから
```
echo -e "\n## For R package"  | sudo tee -a /etc/apt/sources.list
echo "deb https://cran.rstudio.com/bin/linux/ubuntu $(lsb_release -cs)-cran35/" | sudo tee -a /etc/apt/sources.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo apt update
sudo apt install r-base
sudo apt install libxml2-dev libssl-dev libcurl4-openssl-dev
sudo R
>install.packages("devtools")
>devtools::install_github("itamarcaspi/experimentdatar")

```
参考
```
https://qiita.com/JeJeNeNo/items/43fc95c4710c668e86a2
https://qiita.com/MTNakata/items/129d334cea397a6ec0c3
```


```python
experimentdatar = importr('experimentdatar')
vouchers = r['vouchers']
```

### 2. rdataを使う
https://pypi.org/project/rdata/  
R不要で読み込めるのでこちらの方が良い  
参考： https://qiita.com/nekoumei/items/648726e89d05cba6f432#comment-0ea9751e3f01b27b0adb


```python
# # 予めhttps://github.com/itamarcaspi/experimentdatar/blob/master/data/vouchers.rdaからrdaファイルをダウンロードしておく
parsed = rdata.parser.parse_file('../data/vouchers.rda')
converted = rdata.conversion.convert(parsed)
vouchers = converted['vouchers']
```

## (3) Angrist(2002)のTable 3. bogota 1995の再現


```python
formula_x_base = ['VOUCH0']
formula_x_covariate = ['SVY',  'HSVISIT', 'AGE', 'STRATA1', 'STRATA2', 'STRATA3', 'STRATA4', 
                       'STRATA5', 'STRATA6', 'STRATAMS', 'D1993', 'D1995', 'D1997',
                       'DMONTH1', 'DMONTH2', 'DMONTH3', 'DMONTH4', 'DMONTH5', 'DMONTH6', 'DMONTH7', 'DMONTH8',
                       'DMONTH9', 'DMONTH10', 'DMONTH11', 'DMONTH12', 'SEX2']
formula_ys = ['TOTSCYRS','INSCHL','PRSCH_C','USNGSCH','PRSCHA_1','FINISH6','FINISH7','FINISH8','REPT6','REPT','NREPT',
             'MARRIED','HASCHILD','HOURSUM','WORKING3']
```


```python
def get_VOUCH0_regression_summary(df, formula_x_base=None, formula_x_covariate=None, formula_y=None):
    y = df[formula_y]
    if formula_x_covariate is None:
        X = df[formula_x_base]
    else:
        X = df[formula_x_base + formula_x_covariate]
    X = sm.add_constant(X)
    results = sm.OLS(y, X).fit()
    summary = results.summary().tables[1]
    summary = pd.read_html(summary.as_html(), header=0, index_col=0)[0]
    VOUCH0_summary = summary.loc['VOUCH0']
    if formula_x_covariate is None:
        VOUCH0_summary.name = formula_y + '_base'
    else:
        VOUCH0_summary.name = formula_y + '_covariate'
    return VOUCH0_summary
```


```python
### bogota 1995のデータを抽出する
regression_data = vouchers[(vouchers.TAB3SMPL == 1) & (vouchers.BOG95SMP == 1)]

### まとめて回帰分析を実行
regression_results = []
for formula_y in formula_ys:
    #　共変量を含まない回帰
    regression_results.append(get_VOUCH0_regression_summary(
        regression_data,
        formula_x_base=formula_x_base,
        formula_x_covariate=None,
        formula_y=formula_y)
        )
    # 共変量を含む回帰
    regression_results.append(get_VOUCH0_regression_summary(
        regression_data,
        formula_x_base=formula_x_base,
        formula_x_covariate=formula_x_covariate,
        formula_y=formula_y)
        )
```


```python
regression_results = pd.concat(regression_results, axis=1).T
```

## 通学率と奨学金の利用傾向の可視化(ch2_plot2.html)


```python
### PRSCHA_1, USNGSCHに対するVOUCH0の効果を取り出す
using_voucher_results = regression_results.loc[regression_results.index.str.contains('PRSCHA_1|USNGSCH', regex=True)]
using_voucher_results
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
      <th>USNGSCH_base</th>
      <td>0.5089</td>
      <td>0.023</td>
      <td>22.107</td>
      <td>0.000</td>
      <td>0.464</td>
      <td>0.554</td>
    </tr>
    <tr>
      <th>USNGSCH_covariate</th>
      <td>0.5042</td>
      <td>0.023</td>
      <td>22.007</td>
      <td>0.000</td>
      <td>0.459</td>
      <td>0.549</td>
    </tr>
    <tr>
      <th>PRSCHA_1_base</th>
      <td>0.0629</td>
      <td>0.017</td>
      <td>3.731</td>
      <td>0.000</td>
      <td>0.030</td>
      <td>0.096</td>
    </tr>
    <tr>
      <th>PRSCHA_1_covariate</th>
      <td>0.0574</td>
      <td>0.017</td>
      <td>3.385</td>
      <td>0.001</td>
      <td>0.024</td>
      <td>0.091</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 取り出した効果をplotly expressで可視化
fig = px.scatter(using_voucher_results, x=using_voucher_results.index, y='coef', error_y='std err',
                title='2.3.3 通学と割引券の利用傾向')
fig.show()
```




```python
fig.write_html('../images/ch2_plot2-1.html', auto_open=False)
```

## 留年の傾向を可視化


```python
### PRSCH_C,INSCHL,FINISH6-8,REPTに対するVOUCH0の効果を取り出す
going_private_results = regression_results.loc[
    ['FINISH6_covariate', 'FINISH7_covariate', 'FINISH8_covariate', 'INSCHL_covariate', 'NREPT_covariate', 'PRSCH_C_covariate',
    'REPT_covariate', 'REPT6_covariate']
]
going_private_results
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
      <th>FINISH6_covariate</th>
      <td>0.0229</td>
      <td>0.012</td>
      <td>1.910</td>
      <td>0.056</td>
      <td>-0.001</td>
      <td>0.047</td>
    </tr>
    <tr>
      <th>FINISH7_covariate</th>
      <td>0.0307</td>
      <td>0.020</td>
      <td>1.557</td>
      <td>0.120</td>
      <td>-0.008</td>
      <td>0.070</td>
    </tr>
    <tr>
      <th>FINISH8_covariate</th>
      <td>0.1002</td>
      <td>0.027</td>
      <td>3.715</td>
      <td>0.000</td>
      <td>0.047</td>
      <td>0.153</td>
    </tr>
    <tr>
      <th>INSCHL_covariate</th>
      <td>0.0069</td>
      <td>0.020</td>
      <td>0.340</td>
      <td>0.734</td>
      <td>-0.033</td>
      <td>0.047</td>
    </tr>
    <tr>
      <th>NREPT_covariate</th>
      <td>-0.0667</td>
      <td>0.028</td>
      <td>-2.386</td>
      <td>0.017</td>
      <td>-0.122</td>
      <td>-0.012</td>
    </tr>
    <tr>
      <th>PRSCH_C_covariate</th>
      <td>0.1533</td>
      <td>0.028</td>
      <td>5.520</td>
      <td>0.000</td>
      <td>0.099</td>
      <td>0.208</td>
    </tr>
    <tr>
      <th>REPT_covariate</th>
      <td>-0.0548</td>
      <td>0.024</td>
      <td>-2.328</td>
      <td>0.020</td>
      <td>-0.101</td>
      <td>-0.009</td>
    </tr>
    <tr>
      <th>REPT6_covariate</th>
      <td>-0.0594</td>
      <td>0.025</td>
      <td>-2.417</td>
      <td>0.016</td>
      <td>-0.108</td>
      <td>-0.011</td>
    </tr>
  </tbody>
</table>
</div>




```python
### 取り出した効果をggplotで可視化
fig = px.scatter(going_private_results, x=going_private_results.index, y='coef', error_y='std err',
                title='2.4 留年と進級の傾向')
fig.show()
```





```python
fig.write_html('../images/ch2_plot2-2.html', auto_open=False)
```

## (4) Angrist(2002)のTable.4 & 6 bogota 1995の再現


```python
## table4に使うデータを抜き出す
data_tbl4_bog95 = vouchers[(vouchers.BOG95SMP == 1) & (vouchers.TAB3SMPL == 1) & (~vouchers.SCYFNSH.isna())
         & (~vouchers.FINISH6.isna()) & (~vouchers.PRSCHA_1.isna()) & (~vouchers.REPT6.isna())
         & (~vouchers.NREPT.isna()) & (~vouchers.INSCHL.isna()) & (~vouchers.FINISH7.isna())
         & (~vouchers.PRSCH_C.isna()) & (~vouchers.FINISH8.isna()) & (~vouchers.PRSCHA_2.isna())
         & (~vouchers.TOTSCYRS.isna()) & (~vouchers.REPT.isna())][['VOUCH0', 'SVY', 'HSVISIT', 'DJAMUNDI', 'PHONE', 'AGE',
         'STRATA1', 'STRATA2', 'STRATA3', 'STRATA4', 'STRATA5', 'STRATA6', 'STRATAMS', 'DBOGOTA', 'D1993', 'D1995', 'D1997',
         'DMONTH1', 'DMONTH2', 'DMONTH3', 'DMONTH4', 'DMONTH5', 'DMONTH6', 'DMONTH7', 'DMONTH8', 'DMONTH9',
         'DMONTH10', 'DMONTH11', 'DMONTH12', 'SEX_MISS', 'FINISH6', 'FINISH7', 'FINISH8',
         'REPT6', 'REPT', 'NREPT', 'SEX2', 'TOTSCYRS', 'MARRIED', 'HASCHILD',
         'HOURSUM','WORKING3', 'INSCHL','PRSCH_C','USNGSCH','PRSCHA_1']]
```

### 女子生徒のみのデータでの回帰分析


```python
regression_data = data_tbl4_bog95[data_tbl4_bog95.SEX2 == 0]
### まとめて回帰分析を実行
regression_results = []
for formula_y in formula_ys:
    #　共変量を含まない回帰
    regression_results.append(get_VOUCH0_regression_summary(
        regression_data,
        formula_x_base=formula_x_base,
        formula_x_covariate=None,
        formula_y=formula_y)
        )
    # 共変量を含む回帰
    regression_results.append(get_VOUCH0_regression_summary(
        regression_data,
        formula_x_base=formula_x_base,
        formula_x_covariate=formula_x_covariate,
        formula_y=formula_y)
        )
```


```python
df_results_female = pd.concat(regression_results, axis=1).T
df_results_female
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
      <th>TOTSCYRS_base</th>
      <td>0.1478</td>
      <td>0.067</td>
      <td>2.197</td>
      <td>0.028</td>
      <td>0.016</td>
      <td>0.280</td>
    </tr>
    <tr>
      <th>TOTSCYRS_covariate</th>
      <td>0.0909</td>
      <td>0.066</td>
      <td>1.381</td>
      <td>0.168</td>
      <td>-0.038</td>
      <td>0.220</td>
    </tr>
    <tr>
      <th>INSCHL_base</th>
      <td>0.0636</td>
      <td>0.030</td>
      <td>2.143</td>
      <td>0.033</td>
      <td>0.005</td>
      <td>0.122</td>
    </tr>
    <tr>
      <th>INSCHL_covariate</th>
      <td>0.0347</td>
      <td>0.028</td>
      <td>1.237</td>
      <td>0.217</td>
      <td>-0.020</td>
      <td>0.090</td>
    </tr>
    <tr>
      <th>PRSCH_C_base</th>
      <td>0.1852</td>
      <td>0.040</td>
      <td>4.664</td>
      <td>0.000</td>
      <td>0.107</td>
      <td>0.263</td>
    </tr>
    <tr>
      <th>PRSCH_C_covariate</th>
      <td>0.1711</td>
      <td>0.039</td>
      <td>4.337</td>
      <td>0.000</td>
      <td>0.094</td>
      <td>0.249</td>
    </tr>
    <tr>
      <th>USNGSCH_base</th>
      <td>0.5505</td>
      <td>0.032</td>
      <td>17.332</td>
      <td>0.000</td>
      <td>0.488</td>
      <td>0.613</td>
    </tr>
    <tr>
      <th>USNGSCH_covariate</th>
      <td>0.5436</td>
      <td>0.032</td>
      <td>16.992</td>
      <td>0.000</td>
      <td>0.481</td>
      <td>0.606</td>
    </tr>
    <tr>
      <th>PRSCHA_1_base</th>
      <td>0.0408</td>
      <td>0.023</td>
      <td>1.777</td>
      <td>0.076</td>
      <td>-0.004</td>
      <td>0.086</td>
    </tr>
    <tr>
      <th>PRSCHA_1_covariate</th>
      <td>0.0229</td>
      <td>0.023</td>
      <td>1.011</td>
      <td>0.312</td>
      <td>-0.022</td>
      <td>0.067</td>
    </tr>
    <tr>
      <th>FINISH6_base</th>
      <td>0.0358</td>
      <td>0.014</td>
      <td>2.604</td>
      <td>0.009</td>
      <td>0.009</td>
      <td>0.063</td>
    </tr>
    <tr>
      <th>FINISH6_covariate</th>
      <td>0.0317</td>
      <td>0.014</td>
      <td>2.281</td>
      <td>0.023</td>
      <td>0.004</td>
      <td>0.059</td>
    </tr>
    <tr>
      <th>FINISH7_base</th>
      <td>0.0553</td>
      <td>0.025</td>
      <td>2.181</td>
      <td>0.030</td>
      <td>0.006</td>
      <td>0.105</td>
    </tr>
    <tr>
      <th>FINISH7_covariate</th>
      <td>0.0411</td>
      <td>0.025</td>
      <td>1.626</td>
      <td>0.105</td>
      <td>-0.009</td>
      <td>0.091</td>
    </tr>
    <tr>
      <th>FINISH8_base</th>
      <td>0.1228</td>
      <td>0.037</td>
      <td>3.358</td>
      <td>0.001</td>
      <td>0.051</td>
      <td>0.195</td>
    </tr>
    <tr>
      <th>FINISH8_covariate</th>
      <td>0.1047</td>
      <td>0.037</td>
      <td>2.865</td>
      <td>0.004</td>
      <td>0.033</td>
      <td>0.177</td>
    </tr>
    <tr>
      <th>REPT6_base</th>
      <td>-0.0458</td>
      <td>0.031</td>
      <td>-1.489</td>
      <td>0.137</td>
      <td>-0.106</td>
      <td>0.015</td>
    </tr>
    <tr>
      <th>REPT6_covariate</th>
      <td>-0.0362</td>
      <td>0.031</td>
      <td>-1.155</td>
      <td>0.249</td>
      <td>-0.098</td>
      <td>0.025</td>
    </tr>
    <tr>
      <th>REPT_base</th>
      <td>-0.0399</td>
      <td>0.032</td>
      <td>-1.254</td>
      <td>0.210</td>
      <td>-0.102</td>
      <td>0.023</td>
    </tr>
    <tr>
      <th>REPT_covariate</th>
      <td>-0.0290</td>
      <td>0.032</td>
      <td>-0.901</td>
      <td>0.368</td>
      <td>-0.092</td>
      <td>0.034</td>
    </tr>
    <tr>
      <th>NREPT_base</th>
      <td>-0.0507</td>
      <td>0.035</td>
      <td>-1.429</td>
      <td>0.154</td>
      <td>-0.120</td>
      <td>0.019</td>
    </tr>
    <tr>
      <th>NREPT_covariate</th>
      <td>-0.0313</td>
      <td>0.035</td>
      <td>-0.905</td>
      <td>0.366</td>
      <td>-0.099</td>
      <td>0.037</td>
    </tr>
    <tr>
      <th>MARRIED_base</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>MARRIED_covariate</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>HASCHILD_base</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>HASCHILD_covariate</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>HOURSUM_base</th>
      <td>-2.3821</td>
      <td>0.680</td>
      <td>-3.502</td>
      <td>0.000</td>
      <td>-3.718</td>
      <td>-1.046</td>
    </tr>
    <tr>
      <th>HOURSUM_covariate</th>
      <td>-2.1158</td>
      <td>0.685</td>
      <td>-3.089</td>
      <td>0.002</td>
      <td>-3.461</td>
      <td>-0.770</td>
    </tr>
    <tr>
      <th>WORKING3_base</th>
      <td>-0.0409</td>
      <td>0.023</td>
      <td>-1.748</td>
      <td>0.081</td>
      <td>-0.087</td>
      <td>0.005</td>
    </tr>
    <tr>
      <th>WORKING3_covariate</th>
      <td>-0.0314</td>
      <td>0.024</td>
      <td>-1.331</td>
      <td>0.184</td>
      <td>-0.078</td>
      <td>0.015</td>
    </tr>
  </tbody>
</table>
</div>



### 男子生徒のみのデータでの回帰分析


```python
regression_data = data_tbl4_bog95[data_tbl4_bog95.SEX2 == 1]
### まとめて回帰分析を実行
regression_results = []
for formula_y in formula_ys:
    #　共変量を含まない回帰
    regression_results.append(get_VOUCH0_regression_summary(
        regression_data,
        formula_x_base=formula_x_base,
        formula_x_covariate=None,
        formula_y=formula_y)
        )
    # 共変量を含む回帰
    regression_results.append(get_VOUCH0_regression_summary(
        regression_data,
        formula_x_base=formula_x_base,
        formula_x_covariate=formula_x_covariate,
        formula_y=formula_y)
        )
```


```python
df_results_male = pd.concat(regression_results, axis=1).T
df_results_male
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
      <th>TOTSCYRS_base</th>
      <td>-0.0304</td>
      <td>0.080</td>
      <td>-0.380</td>
      <td>0.704</td>
      <td>-0.188</td>
      <td>0.127</td>
    </tr>
    <tr>
      <th>TOTSCYRS_covariate</th>
      <td>-0.0286</td>
      <td>0.078</td>
      <td>-0.366</td>
      <td>0.714</td>
      <td>-0.182</td>
      <td>0.125</td>
    </tr>
    <tr>
      <th>INSCHL_base</th>
      <td>-0.0259</td>
      <td>0.031</td>
      <td>-0.825</td>
      <td>0.410</td>
      <td>-0.088</td>
      <td>0.036</td>
    </tr>
    <tr>
      <th>INSCHL_covariate</th>
      <td>-0.0195</td>
      <td>0.030</td>
      <td>-0.658</td>
      <td>0.511</td>
      <td>-0.078</td>
      <td>0.039</td>
    </tr>
    <tr>
      <th>PRSCH_C_base</th>
      <td>0.1351</td>
      <td>0.040</td>
      <td>3.350</td>
      <td>0.001</td>
      <td>0.056</td>
      <td>0.214</td>
    </tr>
    <tr>
      <th>PRSCH_C_covariate</th>
      <td>0.1363</td>
      <td>0.040</td>
      <td>3.433</td>
      <td>0.001</td>
      <td>0.058</td>
      <td>0.214</td>
    </tr>
    <tr>
      <th>USNGSCH_base</th>
      <td>0.4677</td>
      <td>0.033</td>
      <td>14.061</td>
      <td>0.000</td>
      <td>0.402</td>
      <td>0.533</td>
    </tr>
    <tr>
      <th>USNGSCH_covariate</th>
      <td>0.4677</td>
      <td>0.033</td>
      <td>14.159</td>
      <td>0.000</td>
      <td>0.403</td>
      <td>0.533</td>
    </tr>
    <tr>
      <th>PRSCHA_1_base</th>
      <td>0.0852</td>
      <td>0.025</td>
      <td>3.448</td>
      <td>0.001</td>
      <td>0.037</td>
      <td>0.134</td>
    </tr>
    <tr>
      <th>PRSCHA_1_covariate</th>
      <td>0.0902</td>
      <td>0.025</td>
      <td>3.555</td>
      <td>0.000</td>
      <td>0.040</td>
      <td>0.140</td>
    </tr>
    <tr>
      <th>FINISH6_base</th>
      <td>0.0170</td>
      <td>0.020</td>
      <td>0.863</td>
      <td>0.388</td>
      <td>-0.022</td>
      <td>0.056</td>
    </tr>
    <tr>
      <th>FINISH6_covariate</th>
      <td>0.0144</td>
      <td>0.020</td>
      <td>0.734</td>
      <td>0.463</td>
      <td>-0.024</td>
      <td>0.053</td>
    </tr>
    <tr>
      <th>FINISH7_base</th>
      <td>0.0258</td>
      <td>0.031</td>
      <td>0.840</td>
      <td>0.401</td>
      <td>-0.035</td>
      <td>0.086</td>
    </tr>
    <tr>
      <th>FINISH7_covariate</th>
      <td>0.0264</td>
      <td>0.031</td>
      <td>0.866</td>
      <td>0.387</td>
      <td>-0.034</td>
      <td>0.086</td>
    </tr>
    <tr>
      <th>FINISH8_base</th>
      <td>0.1022</td>
      <td>0.040</td>
      <td>2.566</td>
      <td>0.011</td>
      <td>0.024</td>
      <td>0.181</td>
    </tr>
    <tr>
      <th>FINISH8_covariate</th>
      <td>0.0950</td>
      <td>0.040</td>
      <td>2.368</td>
      <td>0.018</td>
      <td>0.016</td>
      <td>0.174</td>
    </tr>
    <tr>
      <th>REPT6_base</th>
      <td>-0.0862</td>
      <td>0.037</td>
      <td>-2.302</td>
      <td>0.022</td>
      <td>-0.160</td>
      <td>-0.013</td>
    </tr>
    <tr>
      <th>REPT6_covariate</th>
      <td>-0.0866</td>
      <td>0.038</td>
      <td>-2.266</td>
      <td>0.024</td>
      <td>-0.162</td>
      <td>-0.012</td>
    </tr>
    <tr>
      <th>REPT_base</th>
      <td>-0.0807</td>
      <td>0.034</td>
      <td>-2.373</td>
      <td>0.018</td>
      <td>-0.147</td>
      <td>-0.014</td>
    </tr>
    <tr>
      <th>REPT_covariate</th>
      <td>-0.0830</td>
      <td>0.035</td>
      <td>-2.406</td>
      <td>0.016</td>
      <td>-0.151</td>
      <td>-0.015</td>
    </tr>
    <tr>
      <th>NREPT_base</th>
      <td>-0.0964</td>
      <td>0.043</td>
      <td>-2.262</td>
      <td>0.024</td>
      <td>-0.180</td>
      <td>-0.013</td>
    </tr>
    <tr>
      <th>NREPT_covariate</th>
      <td>-0.1015</td>
      <td>0.043</td>
      <td>-2.349</td>
      <td>0.019</td>
      <td>-0.186</td>
      <td>-0.017</td>
    </tr>
    <tr>
      <th>MARRIED_base</th>
      <td>-0.0036</td>
      <td>0.003</td>
      <td>-1.026</td>
      <td>0.305</td>
      <td>-0.010</td>
      <td>0.003</td>
    </tr>
    <tr>
      <th>MARRIED_covariate</th>
      <td>-0.0039</td>
      <td>0.004</td>
      <td>-1.067</td>
      <td>0.286</td>
      <td>-0.011</td>
      <td>0.003</td>
    </tr>
    <tr>
      <th>HASCHILD_base</th>
      <td>-0.0004</td>
      <td>0.007</td>
      <td>-0.052</td>
      <td>0.958</td>
      <td>-0.014</td>
      <td>0.013</td>
    </tr>
    <tr>
      <th>HASCHILD_covariate</th>
      <td>-0.0008</td>
      <td>0.007</td>
      <td>-0.114</td>
      <td>0.909</td>
      <td>-0.015</td>
      <td>0.013</td>
    </tr>
    <tr>
      <th>HOURSUM_base</th>
      <td>-0.5096</td>
      <td>1.115</td>
      <td>-0.457</td>
      <td>0.648</td>
      <td>-2.700</td>
      <td>1.681</td>
    </tr>
    <tr>
      <th>HOURSUM_covariate</th>
      <td>-0.6376</td>
      <td>1.068</td>
      <td>-0.597</td>
      <td>0.551</td>
      <td>-2.736</td>
      <td>1.461</td>
    </tr>
    <tr>
      <th>WORKING3_base</th>
      <td>-0.0254</td>
      <td>0.035</td>
      <td>-0.734</td>
      <td>0.463</td>
      <td>-0.093</td>
      <td>0.043</td>
    </tr>
    <tr>
      <th>WORKING3_covariate</th>
      <td>-0.0366</td>
      <td>0.033</td>
      <td>-1.097</td>
      <td>0.273</td>
      <td>-0.102</td>
      <td>0.029</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 結果を整形
df_results_female['gender'] = 'female'
df_results_male['gender'] = 'male'
```

## 通学傾向への分析結果の可視化(ch2_plot3.html)


```python
using_voucher_results_gender = pd.concat([df_results_female, df_results_male], axis=0)
using_voucher_results_gender = using_voucher_results_gender.loc[
    using_voucher_results_gender.index.str.contains('PRSCHA_1_covariate|USNGSCH_covariate', regex=True)]
```


```python
fig = px.scatter(using_voucher_results_gender, x=using_voucher_results_gender.index, y='coef', facet_row='gender', error_y='std err',
                title='2.5 私立学校への入学と奨学金の利用')
fig.show()
```





```python
fig.write_html('../images/ch2_plot3.html', auto_open=False)
```

## 留年と通学年数への分析結果の可視化(ch2_plot4.html)


```python
### PRSCH_C,INSCHL,REPT,TOTSCYRS,FINISHに対する分析結果を抜き出す
going_private_results_gender = pd.concat([df_results_female, df_results_male], axis=0)
going_private_results_gender = going_private_results_gender.loc[
    going_private_results_gender.index.str.contains(
        'FINISH.*covariate|INSCHL_covariate|NREPT_covariate|PRSCH_C_covariate|REPT_covariate|REPT6_covariate|TOTSCYRS_covariate',
        regex=True)]
```


```python
fig = px.scatter(going_private_results_gender, x=going_private_results_gender.index, y='coef', facet_row='gender', error_y='std err',
                title='2.6 留年と進級の傾向')
fig.show()
```




```python
fig.write_html('../images/ch2_plot4.html', auto_open=False)
```

## 労働時間に対する分析結果の可視化(ch2_plot5.html)


```python
### HOURに対する分析結果を抜き出す
working_hour_results_gender = pd.concat([df_results_female, df_results_male], axis=0)
working_hour_results_gender = working_hour_results_gender.loc[
    working_hour_results_gender.index.str.contains(
        'HOURSUM_covariate',
        regex=True)]
```


```python
fig = px.scatter(working_hour_results_gender, x=working_hour_results_gender.index, y='coef', facet_col='gender', error_y='std err',
                title='2.7 労働時間の傾向')
fig.show()
```






```python
fig.write_html('../images/ch2_plot5.html', auto_open=False)
```
