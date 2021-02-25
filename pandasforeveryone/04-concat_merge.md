```python
import pandas as pd
```


```python
df1 = pd.read_csv('../data/concat_1.csv')
df2 = pd.read_csv('../data/concat_2.csv')
df3 = pd.read_csv('../data/concat_3.csv')
```


```python
df1
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>b1</td>
      <td>c1</td>
      <td>d1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a2</td>
      <td>b2</td>
      <td>c2</td>
      <td>d2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a3</td>
      <td>b3</td>
      <td>c3</td>
      <td>d3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a4</td>
      <td>b4</td>
      <td>c4</td>
      <td>d4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a5</td>
      <td>b5</td>
      <td>c5</td>
      <td>d5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a6</td>
      <td>b6</td>
      <td>c6</td>
      <td>d6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a7</td>
      <td>b7</td>
      <td>c7</td>
      <td>d7</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a8</td>
      <td>b8</td>
      <td>c8</td>
      <td>d8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a9</td>
      <td>b9</td>
      <td>c9</td>
      <td>d9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a10</td>
      <td>b10</td>
      <td>c10</td>
      <td>d10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a11</td>
      <td>b11</td>
      <td>c11</td>
      <td>d11</td>
    </tr>
  </tbody>
</table>
</div>




```python
row_concat = pd.concat([df1, df2, df3])
row_concat
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>b1</td>
      <td>c1</td>
      <td>d1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a2</td>
      <td>b2</td>
      <td>c2</td>
      <td>d2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a3</td>
      <td>b3</td>
      <td>c3</td>
      <td>d3</td>
    </tr>
    <tr>
      <th>0</th>
      <td>a4</td>
      <td>b4</td>
      <td>c4</td>
      <td>d4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a5</td>
      <td>b5</td>
      <td>c5</td>
      <td>d5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a6</td>
      <td>b6</td>
      <td>c6</td>
      <td>d6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a7</td>
      <td>b7</td>
      <td>c7</td>
      <td>d7</td>
    </tr>
    <tr>
      <th>0</th>
      <td>a8</td>
      <td>b8</td>
      <td>c8</td>
      <td>d8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a9</td>
      <td>b9</td>
      <td>c9</td>
      <td>d9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a10</td>
      <td>b10</td>
      <td>c10</td>
      <td>d10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a11</td>
      <td>b11</td>
      <td>c11</td>
      <td>d11</td>
    </tr>
  </tbody>
</table>
</div>




```python
row_concat.loc[0]
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>a4</td>
      <td>b4</td>
      <td>c4</td>
      <td>d4</td>
    </tr>
    <tr>
      <th>0</th>
      <td>a8</td>
      <td>b8</td>
      <td>c8</td>
      <td>d8</td>
    </tr>
  </tbody>
</table>
</div>




```python
row_concat.iloc[0]
```




    A    a0
    B    b0
    C    c0
    D    d0
    Name: 0, dtype: object




```python
row_concat.ix[0]
```

    C:\Users\Danie\Anaconda3\lib\site-packages\ipykernel_launcher.py:1: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
      """Entry point for launching an IPython kernel.
    




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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>a4</td>
      <td>b4</td>
      <td>c4</td>
      <td>d4</td>
    </tr>
    <tr>
      <th>0</th>
      <td>a8</td>
      <td>b8</td>
      <td>c8</td>
      <td>d8</td>
    </tr>
  </tbody>
</table>
</div>




```python
row_concat_reset = pd.concat([df1, df2, df3], ignore_index=True)
row_concat_reset
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>b1</td>
      <td>c1</td>
      <td>d1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a2</td>
      <td>b2</td>
      <td>c2</td>
      <td>d2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a3</td>
      <td>b3</td>
      <td>c3</td>
      <td>d3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a4</td>
      <td>b4</td>
      <td>c4</td>
      <td>d4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>a5</td>
      <td>b5</td>
      <td>c5</td>
      <td>d5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>a6</td>
      <td>b6</td>
      <td>c6</td>
      <td>d6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>a7</td>
      <td>b7</td>
      <td>c7</td>
      <td>d7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>a8</td>
      <td>b8</td>
      <td>c8</td>
      <td>d8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>a9</td>
      <td>b9</td>
      <td>c9</td>
      <td>d9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>a10</td>
      <td>b10</td>
      <td>c10</td>
      <td>d10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>a11</td>
      <td>b11</td>
      <td>c11</td>
      <td>d11</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_row_series = pd.Series(['n1', 'n2', 'n3', 'n4'])
new_row_series
```




    0    n1
    1    n2
    2    n3
    3    n4
    dtype: object




```python
pd.concat([df1, new_row_series])
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>b1</td>
      <td>c1</td>
      <td>d1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a2</td>
      <td>b2</td>
      <td>c2</td>
      <td>d2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a3</td>
      <td>b3</td>
      <td>c3</td>
      <td>d3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>n1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>n2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>n3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>n4</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_row_data = pd.DataFrame([['n1', 'n2', 'n3', 'n4']],
                            columns=['A', 'B', 'C', 'D'])
new_row_data
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>n1</td>
      <td>n2</td>
      <td>n3</td>
      <td>n4</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df1, new_row_data])
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>b1</td>
      <td>c1</td>
      <td>d1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a2</td>
      <td>b2</td>
      <td>c2</td>
      <td>d2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a3</td>
      <td>b3</td>
      <td>c3</td>
      <td>d3</td>
    </tr>
    <tr>
      <th>0</th>
      <td>n1</td>
      <td>n2</td>
      <td>n3</td>
      <td>n4</td>
    </tr>
  </tbody>
</table>
</div>




```python
col_concat = pd.concat([df1, df2, df3], axis=1)
col_concat
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
      <td>a4</td>
      <td>b4</td>
      <td>c4</td>
      <td>d4</td>
      <td>a8</td>
      <td>b8</td>
      <td>c8</td>
      <td>d8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>b1</td>
      <td>c1</td>
      <td>d1</td>
      <td>a5</td>
      <td>b5</td>
      <td>c5</td>
      <td>d5</td>
      <td>a9</td>
      <td>b9</td>
      <td>c9</td>
      <td>d9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a2</td>
      <td>b2</td>
      <td>c2</td>
      <td>d2</td>
      <td>a6</td>
      <td>b6</td>
      <td>c6</td>
      <td>d6</td>
      <td>a10</td>
      <td>b10</td>
      <td>c10</td>
      <td>d10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a3</td>
      <td>b3</td>
      <td>c3</td>
      <td>d3</td>
      <td>a7</td>
      <td>b7</td>
      <td>c7</td>
      <td>d7</td>
      <td>a11</td>
      <td>b11</td>
      <td>c11</td>
      <td>d11</td>
    </tr>
  </tbody>
</table>
</div>




```python
col_concat['A']
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
      <th>A</th>
      <th>A</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>a4</td>
      <td>a8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>a5</td>
      <td>a9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a2</td>
      <td>a6</td>
      <td>a10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a3</td>
      <td>a7</td>
      <td>a11</td>
    </tr>
  </tbody>
</table>
</div>




```python
col_concat_ignore = pd.concat([df1, df2, df3], axis=1, ignore_index=True)
col_concat_ignore
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
      <td>a4</td>
      <td>b4</td>
      <td>c4</td>
      <td>d4</td>
      <td>a8</td>
      <td>b8</td>
      <td>c8</td>
      <td>d8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>b1</td>
      <td>c1</td>
      <td>d1</td>
      <td>a5</td>
      <td>b5</td>
      <td>c5</td>
      <td>d5</td>
      <td>a9</td>
      <td>b9</td>
      <td>c9</td>
      <td>d9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a2</td>
      <td>b2</td>
      <td>c2</td>
      <td>d2</td>
      <td>a6</td>
      <td>b6</td>
      <td>c6</td>
      <td>d6</td>
      <td>a10</td>
      <td>b10</td>
      <td>c10</td>
      <td>d10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a3</td>
      <td>b3</td>
      <td>c3</td>
      <td>d3</td>
      <td>a7</td>
      <td>b7</td>
      <td>c7</td>
      <td>d7</td>
      <td>a11</td>
      <td>b11</td>
      <td>c11</td>
      <td>d11</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.columns=['A','B','C','D']
df2.columns=['E','F','G','H']
df3.columns=['A','H','F','C']
```


```python
df1
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>b1</td>
      <td>c1</td>
      <td>d1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a2</td>
      <td>b2</td>
      <td>c2</td>
      <td>d2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a3</td>
      <td>b3</td>
      <td>c3</td>
      <td>d3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2
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
      <th>E</th>
      <th>F</th>
      <th>G</th>
      <th>H</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a4</td>
      <td>b4</td>
      <td>c4</td>
      <td>d4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a5</td>
      <td>b5</td>
      <td>c5</td>
      <td>d5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a6</td>
      <td>b6</td>
      <td>c6</td>
      <td>d6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a7</td>
      <td>b7</td>
      <td>c7</td>
      <td>d7</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3
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
      <th>A</th>
      <th>H</th>
      <th>F</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a8</td>
      <td>b8</td>
      <td>c8</td>
      <td>d8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a9</td>
      <td>b9</td>
      <td>c9</td>
      <td>d9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a10</td>
      <td>b10</td>
      <td>c10</td>
      <td>d10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a11</td>
      <td>b11</td>
      <td>c11</td>
      <td>d11</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df1, df2, df3])
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
      <th>G</th>
      <th>H</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a0</td>
      <td>b0</td>
      <td>c0</td>
      <td>d0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>b1</td>
      <td>c1</td>
      <td>d1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a2</td>
      <td>b2</td>
      <td>c2</td>
      <td>d2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a3</td>
      <td>b3</td>
      <td>c3</td>
      <td>d3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>a4</td>
      <td>b4</td>
      <td>c4</td>
      <td>d4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>a5</td>
      <td>b5</td>
      <td>c5</td>
      <td>d5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>a6</td>
      <td>b6</td>
      <td>c6</td>
      <td>d6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>a7</td>
      <td>b7</td>
      <td>c7</td>
      <td>d7</td>
    </tr>
    <tr>
      <th>0</th>
      <td>a8</td>
      <td>NaN</td>
      <td>d8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>c8</td>
      <td>NaN</td>
      <td>b8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a9</td>
      <td>NaN</td>
      <td>d9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>c9</td>
      <td>NaN</td>
      <td>b9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a10</td>
      <td>NaN</td>
      <td>d10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>c10</td>
      <td>NaN</td>
      <td>b10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a11</td>
      <td>NaN</td>
      <td>d11</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>c11</td>
      <td>NaN</td>
      <td>b11</td>
    </tr>
  </tbody>
</table>
</div>



# merging


```python
person=pd.read_csv('../data/survey_person.csv')
site=pd.read_csv('../data/survey_site.csv')
survey=pd.read_csv('../data/survey_survey.csv')
visited=pd.read_csv('../data/survey_visited.csv')
```


```python
person
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
      <th>ident</th>
      <th>personal</th>
      <th>family</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>dyer</td>
      <td>William</td>
      <td>Dyer</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pb</td>
      <td>Frank</td>
      <td>Pabodie</td>
    </tr>
    <tr>
      <th>2</th>
      <td>lake</td>
      <td>Anderson</td>
      <td>Lake</td>
    </tr>
    <tr>
      <th>3</th>
      <td>roe</td>
      <td>Valentina</td>
      <td>Roerich</td>
    </tr>
    <tr>
      <th>4</th>
      <td>danforth</td>
      <td>Frank</td>
      <td>Danforth</td>
    </tr>
  </tbody>
</table>
</div>




```python
site
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
      <th>name</th>
      <th>lat</th>
      <th>long</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSK-4</td>
      <td>-48.87</td>
      <td>-123.40</td>
    </tr>
  </tbody>
</table>
</div>




```python
survey
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
      <th>taken</th>
      <th>person</th>
      <th>quant</th>
      <th>reading</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>619</td>
      <td>dyer</td>
      <td>rad</td>
      <td>9.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>619</td>
      <td>dyer</td>
      <td>sal</td>
      <td>0.13</td>
    </tr>
    <tr>
      <th>2</th>
      <td>622</td>
      <td>dyer</td>
      <td>rad</td>
      <td>7.80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>622</td>
      <td>dyer</td>
      <td>sal</td>
      <td>0.09</td>
    </tr>
    <tr>
      <th>4</th>
      <td>734</td>
      <td>pb</td>
      <td>rad</td>
      <td>8.41</td>
    </tr>
    <tr>
      <th>5</th>
      <td>734</td>
      <td>lake</td>
      <td>sal</td>
      <td>0.05</td>
    </tr>
    <tr>
      <th>6</th>
      <td>734</td>
      <td>pb</td>
      <td>temp</td>
      <td>-21.50</td>
    </tr>
    <tr>
      <th>7</th>
      <td>735</td>
      <td>pb</td>
      <td>rad</td>
      <td>7.22</td>
    </tr>
    <tr>
      <th>8</th>
      <td>735</td>
      <td>NaN</td>
      <td>sal</td>
      <td>0.06</td>
    </tr>
    <tr>
      <th>9</th>
      <td>735</td>
      <td>NaN</td>
      <td>temp</td>
      <td>-26.00</td>
    </tr>
    <tr>
      <th>10</th>
      <td>751</td>
      <td>pb</td>
      <td>rad</td>
      <td>4.35</td>
    </tr>
    <tr>
      <th>11</th>
      <td>751</td>
      <td>pb</td>
      <td>temp</td>
      <td>-18.50</td>
    </tr>
    <tr>
      <th>12</th>
      <td>751</td>
      <td>lake</td>
      <td>sal</td>
      <td>0.10</td>
    </tr>
    <tr>
      <th>13</th>
      <td>752</td>
      <td>lake</td>
      <td>rad</td>
      <td>2.19</td>
    </tr>
    <tr>
      <th>14</th>
      <td>752</td>
      <td>lake</td>
      <td>sal</td>
      <td>0.09</td>
    </tr>
    <tr>
      <th>15</th>
      <td>752</td>
      <td>lake</td>
      <td>temp</td>
      <td>-16.00</td>
    </tr>
    <tr>
      <th>16</th>
      <td>752</td>
      <td>roe</td>
      <td>sal</td>
      <td>41.60</td>
    </tr>
    <tr>
      <th>17</th>
      <td>837</td>
      <td>lake</td>
      <td>rad</td>
      <td>1.46</td>
    </tr>
    <tr>
      <th>18</th>
      <td>837</td>
      <td>lake</td>
      <td>sal</td>
      <td>0.21</td>
    </tr>
    <tr>
      <th>19</th>
      <td>837</td>
      <td>roe</td>
      <td>sal</td>
      <td>22.50</td>
    </tr>
    <tr>
      <th>20</th>
      <td>844</td>
      <td>roe</td>
      <td>rad</td>
      <td>11.25</td>
    </tr>
  </tbody>
</table>
</div>




```python
visited
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
      <th>ident</th>
      <th>site</th>
      <th>dated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>619</td>
      <td>DR-1</td>
      <td>1927-02-08</td>
    </tr>
    <tr>
      <th>1</th>
      <td>622</td>
      <td>DR-1</td>
      <td>1927-02-10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>734</td>
      <td>DR-3</td>
      <td>1939-01-07</td>
    </tr>
    <tr>
      <th>3</th>
      <td>735</td>
      <td>DR-3</td>
      <td>1930-01-12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>751</td>
      <td>DR-3</td>
      <td>1930-02-26</td>
    </tr>
    <tr>
      <th>5</th>
      <td>752</td>
      <td>DR-3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>837</td>
      <td>MSK-4</td>
      <td>1932-01-14</td>
    </tr>
    <tr>
      <th>7</th>
      <td>844</td>
      <td>DR-1</td>
      <td>1932-03-22</td>
    </tr>
  </tbody>
</table>
</div>




```python
visited_sub = visited.loc[[0, 2, 6]]
visited_sub
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
      <th>ident</th>
      <th>site</th>
      <th>dated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>619</td>
      <td>DR-1</td>
      <td>1927-02-08</td>
    </tr>
    <tr>
      <th>2</th>
      <td>734</td>
      <td>DR-3</td>
      <td>1939-01-07</td>
    </tr>
    <tr>
      <th>6</th>
      <td>837</td>
      <td>MSK-4</td>
      <td>1932-01-14</td>
    </tr>
  </tbody>
</table>
</div>




```python
site
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
      <th>name</th>
      <th>lat</th>
      <th>long</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSK-4</td>
      <td>-48.87</td>
      <td>-123.40</td>
    </tr>
  </tbody>
</table>
</div>




```python
o2o = site.merge(visited_sub, left_on=['name'], right_on='site')
```


```python
o2o
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
      <th>name</th>
      <th>lat</th>
      <th>long</th>
      <th>ident</th>
      <th>site</th>
      <th>dated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
      <td>619</td>
      <td>DR-1</td>
      <td>1927-02-08</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
      <td>734</td>
      <td>DR-3</td>
      <td>1939-01-07</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSK-4</td>
      <td>-48.87</td>
      <td>-123.40</td>
      <td>837</td>
      <td>MSK-4</td>
      <td>1932-01-14</td>
    </tr>
  </tbody>
</table>
</div>




```python
o2o.shape
```




    (3, 6)




```python
visited
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
      <th>ident</th>
      <th>site</th>
      <th>dated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>619</td>
      <td>DR-1</td>
      <td>1927-02-08</td>
    </tr>
    <tr>
      <th>1</th>
      <td>622</td>
      <td>DR-1</td>
      <td>1927-02-10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>734</td>
      <td>DR-3</td>
      <td>1939-01-07</td>
    </tr>
    <tr>
      <th>3</th>
      <td>735</td>
      <td>DR-3</td>
      <td>1930-01-12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>751</td>
      <td>DR-3</td>
      <td>1930-02-26</td>
    </tr>
    <tr>
      <th>5</th>
      <td>752</td>
      <td>DR-3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>837</td>
      <td>MSK-4</td>
      <td>1932-01-14</td>
    </tr>
    <tr>
      <th>7</th>
      <td>844</td>
      <td>DR-1</td>
      <td>1932-03-22</td>
    </tr>
  </tbody>
</table>
</div>




```python
site
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
      <th>name</th>
      <th>lat</th>
      <th>long</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSK-4</td>
      <td>-48.87</td>
      <td>-123.40</td>
    </tr>
  </tbody>
</table>
</div>




```python
m2o = site.merge(visited, left_on='name', right_on='site')
```


```python
m2o
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
      <th>name</th>
      <th>lat</th>
      <th>long</th>
      <th>ident</th>
      <th>site</th>
      <th>dated</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
      <td>619</td>
      <td>DR-1</td>
      <td>1927-02-08</td>
    </tr>
    <tr>
      <th>1</th>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
      <td>622</td>
      <td>DR-1</td>
      <td>1927-02-10</td>
    </tr>
    <tr>
      <th>2</th>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
      <td>844</td>
      <td>DR-1</td>
      <td>1932-03-22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
      <td>734</td>
      <td>DR-3</td>
      <td>1939-01-07</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
      <td>735</td>
      <td>DR-3</td>
      <td>1930-01-12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
      <td>751</td>
      <td>DR-3</td>
      <td>1930-02-26</td>
    </tr>
    <tr>
      <th>6</th>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
      <td>752</td>
      <td>DR-3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>MSK-4</td>
      <td>-48.87</td>
      <td>-123.40</td>
      <td>837</td>
      <td>MSK-4</td>
      <td>1932-01-14</td>
    </tr>
  </tbody>
</table>
</div>



# many to many


```python
m2o.shape
```




    (8, 6)




```python
person.shape
```




    (5, 3)




```python
survey.shape
```




    (21, 4)




```python
visited.shape
```




    (8, 3)




```python
print(person.head())
print(survey.head())
print(visited.head())
print(site.head())
```

          ident   personal    family
    0      dyer    William      Dyer
    1        pb      Frank   Pabodie
    2      lake   Anderson      Lake
    3       roe  Valentina   Roerich
    4  danforth      Frank  Danforth
       taken person quant  reading
    0    619   dyer   rad     9.82
    1    619   dyer   sal     0.13
    2    622   dyer   rad     7.80
    3    622   dyer   sal     0.09
    4    734     pb   rad     8.41
       ident  site       dated
    0    619  DR-1  1927-02-08
    1    622  DR-1  1927-02-10
    2    734  DR-3  1939-01-07
    3    735  DR-3  1930-01-12
    4    751  DR-3  1930-02-26
        name    lat    long
    0   DR-1 -49.85 -128.57
    1   DR-3 -47.15 -126.72
    2  MSK-4 -48.87 -123.40
    


```python
ps = person.merge(survey, left_on='ident', right_on='person', how='outer')
vs = visited.merge(site, left_on='site', right_on='name', how='outer')
```


```python
ps.shape
```




    (22, 7)




```python
ps.head()
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
      <th>ident</th>
      <th>personal</th>
      <th>family</th>
      <th>taken</th>
      <th>person</th>
      <th>quant</th>
      <th>reading</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>dyer</td>
      <td>William</td>
      <td>Dyer</td>
      <td>619.0</td>
      <td>dyer</td>
      <td>rad</td>
      <td>9.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>dyer</td>
      <td>William</td>
      <td>Dyer</td>
      <td>619.0</td>
      <td>dyer</td>
      <td>sal</td>
      <td>0.13</td>
    </tr>
    <tr>
      <th>2</th>
      <td>dyer</td>
      <td>William</td>
      <td>Dyer</td>
      <td>622.0</td>
      <td>dyer</td>
      <td>rad</td>
      <td>7.80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>dyer</td>
      <td>William</td>
      <td>Dyer</td>
      <td>622.0</td>
      <td>dyer</td>
      <td>sal</td>
      <td>0.09</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pb</td>
      <td>Frank</td>
      <td>Pabodie</td>
      <td>734.0</td>
      <td>pb</td>
      <td>rad</td>
      <td>8.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
vs.shape
```




    (8, 6)




```python
vs.head()
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
      <th>ident</th>
      <th>site</th>
      <th>dated</th>
      <th>name</th>
      <th>lat</th>
      <th>long</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>619</td>
      <td>DR-1</td>
      <td>1927-02-08</td>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>1</th>
      <td>622</td>
      <td>DR-1</td>
      <td>1927-02-10</td>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>2</th>
      <td>844</td>
      <td>DR-1</td>
      <td>1932-03-22</td>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>734</td>
      <td>DR-3</td>
      <td>1939-01-07</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>4</th>
      <td>735</td>
      <td>DR-3</td>
      <td>1930-01-12</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
  </tbody>
</table>
</div>




```python
ps_vs = ps.merge(vs,
                 left_on=['taken'],
                 right_on=['ident'],
                how='outer')
```


```python
ps_vs.shape
```




    (22, 13)




```python
ps_vs
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
      <th>ident_x</th>
      <th>personal</th>
      <th>family</th>
      <th>taken</th>
      <th>person</th>
      <th>quant</th>
      <th>reading</th>
      <th>ident_y</th>
      <th>site</th>
      <th>dated</th>
      <th>name</th>
      <th>lat</th>
      <th>long</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>dyer</td>
      <td>William</td>
      <td>Dyer</td>
      <td>619</td>
      <td>dyer</td>
      <td>rad</td>
      <td>9.82</td>
      <td>619.0</td>
      <td>DR-1</td>
      <td>1927-02-08</td>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>1</th>
      <td>dyer</td>
      <td>William</td>
      <td>Dyer</td>
      <td>619</td>
      <td>dyer</td>
      <td>sal</td>
      <td>0.13</td>
      <td>619.0</td>
      <td>DR-1</td>
      <td>1927-02-08</td>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>2</th>
      <td>dyer</td>
      <td>William</td>
      <td>Dyer</td>
      <td>622</td>
      <td>dyer</td>
      <td>rad</td>
      <td>7.80</td>
      <td>622.0</td>
      <td>DR-1</td>
      <td>1927-02-10</td>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>3</th>
      <td>dyer</td>
      <td>William</td>
      <td>Dyer</td>
      <td>622</td>
      <td>dyer</td>
      <td>sal</td>
      <td>0.09</td>
      <td>622.0</td>
      <td>DR-1</td>
      <td>1927-02-10</td>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pb</td>
      <td>Frank</td>
      <td>Pabodie</td>
      <td>734</td>
      <td>pb</td>
      <td>rad</td>
      <td>8.41</td>
      <td>734.0</td>
      <td>DR-3</td>
      <td>1939-01-07</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>5</th>
      <td>pb</td>
      <td>Frank</td>
      <td>Pabodie</td>
      <td>734</td>
      <td>pb</td>
      <td>temp</td>
      <td>-21.50</td>
      <td>734.0</td>
      <td>DR-3</td>
      <td>1939-01-07</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>6</th>
      <td>lake</td>
      <td>Anderson</td>
      <td>Lake</td>
      <td>734</td>
      <td>lake</td>
      <td>sal</td>
      <td>0.05</td>
      <td>734.0</td>
      <td>DR-3</td>
      <td>1939-01-07</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>7</th>
      <td>pb</td>
      <td>Frank</td>
      <td>Pabodie</td>
      <td>735</td>
      <td>pb</td>
      <td>rad</td>
      <td>7.22</td>
      <td>735.0</td>
      <td>DR-3</td>
      <td>1930-01-12</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>735</td>
      <td>NaN</td>
      <td>sal</td>
      <td>0.06</td>
      <td>735.0</td>
      <td>DR-3</td>
      <td>1930-01-12</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>735</td>
      <td>NaN</td>
      <td>temp</td>
      <td>-26.00</td>
      <td>735.0</td>
      <td>DR-3</td>
      <td>1930-01-12</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>10</th>
      <td>pb</td>
      <td>Frank</td>
      <td>Pabodie</td>
      <td>751</td>
      <td>pb</td>
      <td>rad</td>
      <td>4.35</td>
      <td>751.0</td>
      <td>DR-3</td>
      <td>1930-02-26</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>11</th>
      <td>pb</td>
      <td>Frank</td>
      <td>Pabodie</td>
      <td>751</td>
      <td>pb</td>
      <td>temp</td>
      <td>-18.50</td>
      <td>751.0</td>
      <td>DR-3</td>
      <td>1930-02-26</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>12</th>
      <td>lake</td>
      <td>Anderson</td>
      <td>Lake</td>
      <td>751</td>
      <td>lake</td>
      <td>sal</td>
      <td>0.10</td>
      <td>751.0</td>
      <td>DR-3</td>
      <td>1930-02-26</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>13</th>
      <td>lake</td>
      <td>Anderson</td>
      <td>Lake</td>
      <td>752</td>
      <td>lake</td>
      <td>rad</td>
      <td>2.19</td>
      <td>752.0</td>
      <td>DR-3</td>
      <td>NaN</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>14</th>
      <td>lake</td>
      <td>Anderson</td>
      <td>Lake</td>
      <td>752</td>
      <td>lake</td>
      <td>sal</td>
      <td>0.09</td>
      <td>752.0</td>
      <td>DR-3</td>
      <td>NaN</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>15</th>
      <td>lake</td>
      <td>Anderson</td>
      <td>Lake</td>
      <td>752</td>
      <td>lake</td>
      <td>temp</td>
      <td>-16.00</td>
      <td>752.0</td>
      <td>DR-3</td>
      <td>NaN</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>16</th>
      <td>roe</td>
      <td>Valentina</td>
      <td>Roerich</td>
      <td>752</td>
      <td>roe</td>
      <td>sal</td>
      <td>41.60</td>
      <td>752.0</td>
      <td>DR-3</td>
      <td>NaN</td>
      <td>DR-3</td>
      <td>-47.15</td>
      <td>-126.72</td>
    </tr>
    <tr>
      <th>17</th>
      <td>lake</td>
      <td>Anderson</td>
      <td>Lake</td>
      <td>837</td>
      <td>lake</td>
      <td>rad</td>
      <td>1.46</td>
      <td>837.0</td>
      <td>MSK-4</td>
      <td>1932-01-14</td>
      <td>MSK-4</td>
      <td>-48.87</td>
      <td>-123.40</td>
    </tr>
    <tr>
      <th>18</th>
      <td>lake</td>
      <td>Anderson</td>
      <td>Lake</td>
      <td>837</td>
      <td>lake</td>
      <td>sal</td>
      <td>0.21</td>
      <td>837.0</td>
      <td>MSK-4</td>
      <td>1932-01-14</td>
      <td>MSK-4</td>
      <td>-48.87</td>
      <td>-123.40</td>
    </tr>
    <tr>
      <th>19</th>
      <td>roe</td>
      <td>Valentina</td>
      <td>Roerich</td>
      <td>837</td>
      <td>roe</td>
      <td>sal</td>
      <td>22.50</td>
      <td>837.0</td>
      <td>MSK-4</td>
      <td>1932-01-14</td>
      <td>MSK-4</td>
      <td>-48.87</td>
      <td>-123.40</td>
    </tr>
    <tr>
      <th>20</th>
      <td>roe</td>
      <td>Valentina</td>
      <td>Roerich</td>
      <td>844</td>
      <td>roe</td>
      <td>rad</td>
      <td>11.25</td>
      <td>844.0</td>
      <td>DR-1</td>
      <td>1932-03-22</td>
      <td>DR-1</td>
      <td>-49.85</td>
      <td>-128.57</td>
    </tr>
    <tr>
      <th>21</th>
      <td>danforth</td>
      <td>Frank</td>
      <td>Danforth</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 = pd.DataFrame({
    'a': ['a1', 'a2', 'a3', 'a4', 'a5'],
    'b': [1, 1, 2, 2, 3]
})
df1
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
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a5</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({
    'a2': ['2a1', '2a2', '2a3', '2a4', '2a5'],
    'b2': [1, 1, 1, 2, 2]
})
df2
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
      <th>a2</th>
      <th>b2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2a1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2a2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2a3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2a4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2a5</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
m2m = pd.merge(df1, df2, left_on=['b'], right_on=['b2'])
m2m
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
      <th>a</th>
      <th>b</th>
      <th>a2</th>
      <th>b2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a1</td>
      <td>1</td>
      <td>2a1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>1</td>
      <td>2a2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a1</td>
      <td>1</td>
      <td>2a3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a2</td>
      <td>1</td>
      <td>2a1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a2</td>
      <td>1</td>
      <td>2a2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>a2</td>
      <td>1</td>
      <td>2a3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>a3</td>
      <td>2</td>
      <td>2a4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>a3</td>
      <td>2</td>
      <td>2a5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>a4</td>
      <td>2</td>
      <td>2a4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>a4</td>
      <td>2</td>
      <td>2a5</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
assert len(df1) == len(m2m)
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-94-3c656ec3a9a1> in <module>()
    ----> 1 assert len(df1) == len(m2m)
    

    AssertionError: 



```python

```
