```python
import pandas as pd
```


```python
df = pd.read_csv('../data/gapminder.tsv', sep='\t')
```


```python
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>country</th>
      <th>continent</th>
      <th>year</th>
      <th>lifeExp</th>
      <th>pop</th>
      <th>gdpPercap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1952</td>
      <td>28.801</td>
      <td>8425333</td>
      <td>779.445314</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1957</td>
      <td>30.332</td>
      <td>9240934</td>
      <td>820.853030</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1962</td>
      <td>31.997</td>
      <td>10267083</td>
      <td>853.100710</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1967</td>
      <td>34.020</td>
      <td>11537966</td>
      <td>836.197138</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Afghanistan</td>
      <td>Asia</td>
      <td>1972</td>
      <td>36.088</td>
      <td>13079460</td>
      <td>739.981106</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby('year')['lifeExp'].mean()
```




    year
    1952    49.057620
    1957    51.507401
    1962    53.609249
    1967    55.678290
    1972    57.647386
    1977    59.570157
    1982    61.533197
    1987    63.212613
    1992    64.160338
    1997    65.014676
    2002    65.694923
    2007    67.007423
    Name: lifeExp, dtype: float64




```python
df.groupby(['year', 'continent'])['lifeExp'].mean()
```




    year  continent
    1952  Africa       39.135500
          Americas     53.279840
          Asia         46.314394
          Europe       64.408500
          Oceania      69.255000
    1957  Africa       41.266346
          Americas     55.960280
          Asia         49.318544
          Europe       66.703067
          Oceania      70.295000
    1962  Africa       43.319442
          Americas     58.398760
          Asia         51.563223
          Europe       68.539233
          Oceania      71.085000
    1967  Africa       45.334538
          Americas     60.410920
          Asia         54.663640
          Europe       69.737600
          Oceania      71.310000
    1972  Africa       47.450942
          Americas     62.394920
          Asia         57.319269
          Europe       70.775033
          Oceania      71.910000
    1977  Africa       49.580423
          Americas     64.391560
          Asia         59.610556
          Europe       71.937767
          Oceania      72.855000
    1982  Africa       51.592865
          Americas     66.228840
          Asia         62.617939
          Europe       72.806400
          Oceania      74.290000
    1987  Africa       53.344788
          Americas     68.090720
          Asia         64.851182
          Europe       73.642167
          Oceania      75.320000
    1992  Africa       53.629577
          Americas     69.568360
          Asia         66.537212
          Europe       74.440100
          Oceania      76.945000
    1997  Africa       53.598269
          Americas     71.150480
          Asia         68.020515
          Europe       75.505167
          Oceania      78.190000
    2002  Africa       53.325231
          Americas     72.422040
          Asia         69.233879
          Europe       76.700600
          Oceania      79.740000
    2007  Africa       54.806038
          Americas     73.608120
          Asia         70.728485
          Europe       77.648600
          Oceania      80.719500
    Name: lifeExp, dtype: float64




```python

```
