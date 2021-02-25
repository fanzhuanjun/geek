```python
import pandas as pd
from scipy import stats
import joblib
```

## データの読み込み


```python
mail_df = pd.read_csv('http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv')
```

## (4) データの準備
### 女性向けメールが配信されたデータを削除したデータを作成


```python
male_df = mail_df[mail_df.segment != 'Womens E-Mail'].copy() # 女性向けメールが配信されたデータを削除
male_df['treatment'] = male_df.segment.apply(lambda x: 1 if x == 'Mens E-Mail' else 0) #介入を表すtreatment変数を追加
```

## (5) 集計による比較
### group_byとsummairseを使って集計


```python
male_df.groupby('treatment').agg( # データのグループ化
    conversion_rate=('conversion', 'mean'), # グループごとのconversionの平均
    spend_mean=('spend', 'mean'), # グループごとのspendの平均
    count=('treatment', 'count') # グループごとのデータ数
)
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
      <th>conversion_rate</th>
      <th>spend_mean</th>
      <th>count</th>
    </tr>
    <tr>
      <th>treatment</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.005726</td>
      <td>0.652789</td>
      <td>21306</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.012531</td>
      <td>1.422617</td>
      <td>21307</td>
    </tr>
  </tbody>
</table>
</div>



## (6) t検定を行う


```python
### (a)男性向けメールが配信されたグループの購買データを得る
mens_mail = male_df[male_df.treatment==1].spend.values

### (b)メールが配信されなかったグループの購買データを得る
no_mail = male_df[male_df.treatment==0].spend.values

### (a)(b)の平均の差に対して有意差検定を実行する
stats.ttest_ind(mens_mail, no_mail)
```




    Ttest_indResult(statistic=5.300090294465472, pvalue=1.163200872605869e-07)



## (7) セレクションバイアスのあるデータの作成
### バイアスのあるデータの作成


```python
sample_rules = (male_df.history > 300) | (male_df.recency < 6) | (male_df.channel=='Multichannel')
biased_df = pd.concat([
    male_df[(sample_rules) & (male_df.treatment == 0)].sample(frac=0.5, random_state=1),
    male_df[(sample_rules) & (male_df.treatment == 1)],
    male_df[(~sample_rules) & (male_df.treatment == 0)],
    male_df[(~sample_rules) & (male_df.treatment == 1)].sample(frac=0.5, random_state=1)
], axis=0, ignore_index=True)
```

## (8) セレクションバイアスのあるデータで平均を比較
### groupbyを使って集計(Biased)


```python
biased_df.groupby('treatment').agg( # データのグループ化
    conversion_rate=('conversion', 'mean'), # グループごとのconversionの平均
    spend_mean=('spend', 'mean'), # グループごとのspendの平均
    count=('treatment', 'count') # グループごとのデータ数
)
# 乱数でbiased_dfのデータを作成しているので数値は書籍とは異なる。（結論は変わらない）
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
      <th>conversion_rate</th>
      <th>spend_mean</th>
      <th>count</th>
    </tr>
    <tr>
      <th>treatment</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.004540</td>
      <td>0.557954</td>
      <td>14757</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.013572</td>
      <td>1.541704</td>
      <td>17168</td>
    </tr>
  </tbody>
</table>
</div>



## (9) scipy.statsのttest_indを使ってt検定を行う(Biased)


```python
## (a)男性向けメールが配信されたグループの購買データを得る
mens_mail_biased = biased_df[biased_df.treatment == 1].spend.values

## (b)メールが配信されなかったグループの購買データを得る
no_mail_biased = biased_df[biased_df.treatment == 0].spend.values

## (a)(b)の平均の差に対して有意差検定を実行
stats.ttest_ind(mens_mail_biased, no_mail_biased)
```




    Ttest_indResult(statistic=5.595867225527975, pvalue=2.21319841336543e-08)




```python
#ch2で利用するmale_df, biased_dfを保存する
joblib.dump(male_df, '../data/male_df.joblib')
joblib.dump(biased_df, '../data/biased_df.joblib')
```




    ['../data/biased_df.joblib']


