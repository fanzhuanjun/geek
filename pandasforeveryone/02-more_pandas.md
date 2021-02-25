```python
import pandas as pd
```


```python
s = pd.Series(['banana', 42])
```


```python
s
```




    0    banana
    1        42
    dtype: object




```python
s = pd.Series(['Wes', 'Creater'], index=['person', 'who'])
```


```python
s
```




    person        Wes
    who       Creater
    dtype: object




```python
s.loc['person']
```




    'Wes'




```python
s.iloc[0]
```




    'Wes'




```python
scientists=pd.DataFrame(
data={'Occupation':['Chemist','Statistician'],
'Born':['1920-07-25', '1876-06-13'],
'Died':['1958-04-16', '1937-10-16'],
'Age':[37,61]},
index=['Rosaline Franklin','William Gosset'],
columns=['Occupation', 'Born','Died','Age'])
```


```python
scientists
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
      <th>Occupation</th>
      <th>Born</th>
      <th>Died</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rosaline Franklin</th>
      <td>Chemist</td>
      <td>1920-07-25</td>
      <td>1958-04-16</td>
      <td>37</td>
    </tr>
    <tr>
      <th>William Gosset</th>
      <td>Statistician</td>
      <td>1876-06-13</td>
      <td>1937-10-16</td>
      <td>61</td>
    </tr>
  </tbody>
</table>
</div>




```python
scientists = pd.read_csv('../data/scientists.csv')
```


```python
scientists
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
      <th>Name</th>
      <th>Born</th>
      <th>Died</th>
      <th>Age</th>
      <th>Occupation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rosaline Franklin</td>
      <td>1920-07-25</td>
      <td>1958-04-16</td>
      <td>37</td>
      <td>Chemist</td>
    </tr>
    <tr>
      <th>1</th>
      <td>William Gosset</td>
      <td>1876-06-13</td>
      <td>1937-10-16</td>
      <td>61</td>
      <td>Statistician</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florence Nightingale</td>
      <td>1820-05-12</td>
      <td>1910-08-13</td>
      <td>90</td>
      <td>Nurse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Marie Curie</td>
      <td>1867-11-07</td>
      <td>1934-07-04</td>
      <td>66</td>
      <td>Chemist</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rachel Carson</td>
      <td>1907-05-27</td>
      <td>1964-04-14</td>
      <td>56</td>
      <td>Biologist</td>
    </tr>
    <tr>
      <th>5</th>
      <td>John Snow</td>
      <td>1813-03-15</td>
      <td>1858-06-16</td>
      <td>45</td>
      <td>Physician</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Alan Turing</td>
      <td>1912-06-23</td>
      <td>1954-06-07</td>
      <td>41</td>
      <td>Computer Scientist</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Johann Gauss</td>
      <td>1777-04-30</td>
      <td>1855-02-23</td>
      <td>77</td>
      <td>Mathematician</td>
    </tr>
  </tbody>
</table>
</div>




```python
ages = scientists['Age']
```


```python
ages
```




    0    37
    1    61
    2    90
    3    66
    4    56
    5    45
    6    41
    7    77
    Name: Age, dtype: int64




```python
ages = scientists.Age
ages
```




    0    37
    1    61
    2    90
    3    66
    4    56
    5    45
    6    41
    7    77
    Name: Age, dtype: int64




```python
# if shape is a column name you *have* to use square brackets
# scientists['shape']
```




    (8, 5)




```python
type(ages)
```




    pandas.core.series.Series




```python
ages.mean()
```




    59.125




```python
ages.shape
```




    (8,)




```python
ages.min()
```




    37




```python
ages.describe()
```




    count     8.000000
    mean     59.125000
    std      18.325918
    min      37.000000
    25%      44.000000
    50%      58.500000
    75%      68.750000
    max      90.000000
    Name: Age, dtype: float64




```python
ages[ages > ages.mean()]
```




    1    61
    2    90
    3    66
    7    77
    Name: Age, dtype: int64




```python
ages[(ages > ages.mean()) & (ages > 75)]
```




    2    90
    7    77
    Name: Age, dtype: int64




```python
ages[ages > ages.mean() & ages > 75]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~\Anaconda3\lib\site-packages\pandas\core\ops.py in na_op(x, y)
        882         try:
    --> 883             result = op(x, y)
        884         except TypeError:
    

    ~\Anaconda3\lib\site-packages\pandas\core\ops.py in <lambda>(x, y)
        128                  xor=bool_method(operator.xor, names('xor'), op('^')),
    --> 129                  rand_=bool_method(lambda x, y: operator.and_(y, x),
        130                                    names('rand_'), op('&')),
    

    TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

    
    During handling of the above exception, another exception occurred:
    

    ValueError                                Traceback (most recent call last)

    ~\Anaconda3\lib\site-packages\pandas\core\ops.py in na_op(x, y)
        900                         y = bool(y)
    --> 901                     result = lib.scalar_binop(x, y, op)
        902                 except:
    

    pandas\_libs\lib.pyx in pandas._libs.lib.scalar_binop()
    

    ValueError: Buffer dtype mismatch, expected 'Python object' but got 'long long'

    
    During handling of the above exception, another exception occurred:
    

    TypeError                                 Traceback (most recent call last)

    <ipython-input-30-38ee68db636b> in <module>()
    ----> 1 ages[ages > ages.mean() & ages > 75]
    

    ~\Anaconda3\lib\site-packages\pandas\core\ops.py in wrapper(self, other)
        933                       is_integer_dtype(np.asarray(other)) else fill_bool)
        934             return filler(self._constructor(
    --> 935                 na_op(self.values, other),
        936                 index=self.index)).__finalize__(self)
        937 
    

    ~\Anaconda3\lib\site-packages\pandas\core\ops.py in na_op(x, y)
        903                     raise TypeError("cannot compare a dtyped [{0}] array with "
        904                                     "a scalar of type [{1}]".format(
    --> 905                                         x.dtype, type(y).__name__))
        906 
        907         return result
    

    TypeError: cannot compare a dtyped [int64] array with a scalar of type [bool]



```python
ages[(ages > ages.mean()) & ~(ages > 75)]
```




    1    61
    3    66
    Name: Age, dtype: int64




```python
ages.describe()
```




    count     8.000000
    mean     59.125000
    std      18.325918
    min      37.000000
    25%      44.000000
    50%      58.500000
    75%      68.750000
    max      90.000000
    Name: Age, dtype: float64




```python
ages + 100
```




    0    137
    1    161
    2    190
    3    166
    4    156
    5    145
    6    141
    7    177
    Name: Age, dtype: int64




```python
scientists
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
      <th>Name</th>
      <th>Born</th>
      <th>Died</th>
      <th>Age</th>
      <th>Occupation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rosaline Franklin</td>
      <td>1920-07-25</td>
      <td>1958-04-16</td>
      <td>37</td>
      <td>Chemist</td>
    </tr>
    <tr>
      <th>1</th>
      <td>William Gosset</td>
      <td>1876-06-13</td>
      <td>1937-10-16</td>
      <td>61</td>
      <td>Statistician</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florence Nightingale</td>
      <td>1820-05-12</td>
      <td>1910-08-13</td>
      <td>90</td>
      <td>Nurse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Marie Curie</td>
      <td>1867-11-07</td>
      <td>1934-07-04</td>
      <td>66</td>
      <td>Chemist</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rachel Carson</td>
      <td>1907-05-27</td>
      <td>1964-04-14</td>
      <td>56</td>
      <td>Biologist</td>
    </tr>
    <tr>
      <th>5</th>
      <td>John Snow</td>
      <td>1813-03-15</td>
      <td>1858-06-16</td>
      <td>45</td>
      <td>Physician</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Alan Turing</td>
      <td>1912-06-23</td>
      <td>1954-06-07</td>
      <td>41</td>
      <td>Computer Scientist</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Johann Gauss</td>
      <td>1777-04-30</td>
      <td>1855-02-23</td>
      <td>77</td>
      <td>Mathematician</td>
    </tr>
  </tbody>
</table>
</div>




```python
scientists[scientists['Age'] > scientists['Age'].mean()]
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
      <th>Name</th>
      <th>Born</th>
      <th>Died</th>
      <th>Age</th>
      <th>Occupation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>William Gosset</td>
      <td>1876-06-13</td>
      <td>1937-10-16</td>
      <td>61</td>
      <td>Statistician</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florence Nightingale</td>
      <td>1820-05-12</td>
      <td>1910-08-13</td>
      <td>90</td>
      <td>Nurse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Marie Curie</td>
      <td>1867-11-07</td>
      <td>1934-07-04</td>
      <td>66</td>
      <td>Chemist</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Johann Gauss</td>
      <td>1777-04-30</td>
      <td>1855-02-23</td>
      <td>77</td>
      <td>Mathematician</td>
    </tr>
  </tbody>
</table>
</div>




```python
scientists['Age'] > scientists['Age'].mean()
```




    0    False
    1     True
    2     True
    3     True
    4    False
    5    False
    6    False
    7     True
    Name: Age, dtype: bool




```python
scientists
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
      <th>Name</th>
      <th>Born</th>
      <th>Died</th>
      <th>Age</th>
      <th>Occupation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rosaline Franklin</td>
      <td>1920-07-25</td>
      <td>1958-04-16</td>
      <td>37</td>
      <td>Chemist</td>
    </tr>
    <tr>
      <th>1</th>
      <td>William Gosset</td>
      <td>1876-06-13</td>
      <td>1937-10-16</td>
      <td>61</td>
      <td>Statistician</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florence Nightingale</td>
      <td>1820-05-12</td>
      <td>1910-08-13</td>
      <td>90</td>
      <td>Nurse</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Marie Curie</td>
      <td>1867-11-07</td>
      <td>1934-07-04</td>
      <td>66</td>
      <td>Chemist</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rachel Carson</td>
      <td>1907-05-27</td>
      <td>1964-04-14</td>
      <td>56</td>
      <td>Biologist</td>
    </tr>
    <tr>
      <th>5</th>
      <td>John Snow</td>
      <td>1813-03-15</td>
      <td>1858-06-16</td>
      <td>45</td>
      <td>Physician</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Alan Turing</td>
      <td>1912-06-23</td>
      <td>1954-06-07</td>
      <td>41</td>
      <td>Computer Scientist</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Johann Gauss</td>
      <td>1777-04-30</td>
      <td>1855-02-23</td>
      <td>77</td>
      <td>Mathematician</td>
    </tr>
  </tbody>
</table>
</div>




```python
scientists.dtypes
```




    Name          object
    Born          object
    Died          object
    Age            int64
    Occupation    object
    dtype: object




```python
# strftime
born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
```


```python
pd.to_datetime?
```


```python
born_datetime
```




    0   1920-07-25
    1   1876-06-13
    2   1820-05-12
    3   1867-11-07
    4   1907-05-27
    5   1813-03-15
    6   1912-06-23
    7   1777-04-30
    Name: Born, dtype: datetime64[ns]




```python
scientists['born_dt'] = born_datetime
```


```python
# same as above
scientists['born_dt'] = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
```


```python
scientists
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
      <th>Name</th>
      <th>Born</th>
      <th>Died</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>born_dt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rosaline Franklin</td>
      <td>1920-07-25</td>
      <td>1958-04-16</td>
      <td>37</td>
      <td>Chemist</td>
      <td>1920-07-25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>William Gosset</td>
      <td>1876-06-13</td>
      <td>1937-10-16</td>
      <td>61</td>
      <td>Statistician</td>
      <td>1876-06-13</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florence Nightingale</td>
      <td>1820-05-12</td>
      <td>1910-08-13</td>
      <td>90</td>
      <td>Nurse</td>
      <td>1820-05-12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Marie Curie</td>
      <td>1867-11-07</td>
      <td>1934-07-04</td>
      <td>66</td>
      <td>Chemist</td>
      <td>1867-11-07</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rachel Carson</td>
      <td>1907-05-27</td>
      <td>1964-04-14</td>
      <td>56</td>
      <td>Biologist</td>
      <td>1907-05-27</td>
    </tr>
    <tr>
      <th>5</th>
      <td>John Snow</td>
      <td>1813-03-15</td>
      <td>1858-06-16</td>
      <td>45</td>
      <td>Physician</td>
      <td>1813-03-15</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Alan Turing</td>
      <td>1912-06-23</td>
      <td>1954-06-07</td>
      <td>41</td>
      <td>Computer Scientist</td>
      <td>1912-06-23</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Johann Gauss</td>
      <td>1777-04-30</td>
      <td>1855-02-23</td>
      <td>77</td>
      <td>Mathematician</td>
      <td>1777-04-30</td>
    </tr>
  </tbody>
</table>
</div>




```python
scientists.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 8 entries, 0 to 7
    Data columns (total 6 columns):
    Name          8 non-null object
    Born          8 non-null object
    Died          8 non-null object
    Age           8 non-null int64
    Occupation    8 non-null object
    born_dt       8 non-null datetime64[ns]
    dtypes: datetime64[ns](1), int64(1), object(4)
    memory usage: 464.0+ bytes
    


```python
scientists['died_dt'] = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
scientists
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
      <th>Name</th>
      <th>Born</th>
      <th>Died</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>born_dt</th>
      <th>died_dt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rosaline Franklin</td>
      <td>1920-07-25</td>
      <td>1958-04-16</td>
      <td>37</td>
      <td>Chemist</td>
      <td>1920-07-25</td>
      <td>1958-04-16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>William Gosset</td>
      <td>1876-06-13</td>
      <td>1937-10-16</td>
      <td>61</td>
      <td>Statistician</td>
      <td>1876-06-13</td>
      <td>1937-10-16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florence Nightingale</td>
      <td>1820-05-12</td>
      <td>1910-08-13</td>
      <td>90</td>
      <td>Nurse</td>
      <td>1820-05-12</td>
      <td>1910-08-13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Marie Curie</td>
      <td>1867-11-07</td>
      <td>1934-07-04</td>
      <td>66</td>
      <td>Chemist</td>
      <td>1867-11-07</td>
      <td>1934-07-04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rachel Carson</td>
      <td>1907-05-27</td>
      <td>1964-04-14</td>
      <td>56</td>
      <td>Biologist</td>
      <td>1907-05-27</td>
      <td>1964-04-14</td>
    </tr>
    <tr>
      <th>5</th>
      <td>John Snow</td>
      <td>1813-03-15</td>
      <td>1858-06-16</td>
      <td>45</td>
      <td>Physician</td>
      <td>1813-03-15</td>
      <td>1858-06-16</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Alan Turing</td>
      <td>1912-06-23</td>
      <td>1954-06-07</td>
      <td>41</td>
      <td>Computer Scientist</td>
      <td>1912-06-23</td>
      <td>1954-06-07</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Johann Gauss</td>
      <td>1777-04-30</td>
      <td>1855-02-23</td>
      <td>77</td>
      <td>Mathematician</td>
      <td>1777-04-30</td>
      <td>1855-02-23</td>
    </tr>
  </tbody>
</table>
</div>




```python
scientists = scientists.drop(['Born', 'Died'], axis=1)
```


```python
scientists
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
      <th>Name</th>
      <th>Age</th>
      <th>Occupation</th>
      <th>born_dt</th>
      <th>died_dt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Rosaline Franklin</td>
      <td>37</td>
      <td>Chemist</td>
      <td>1920-07-25</td>
      <td>1958-04-16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>William Gosset</td>
      <td>61</td>
      <td>Statistician</td>
      <td>1876-06-13</td>
      <td>1937-10-16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Florence Nightingale</td>
      <td>90</td>
      <td>Nurse</td>
      <td>1820-05-12</td>
      <td>1910-08-13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Marie Curie</td>
      <td>66</td>
      <td>Chemist</td>
      <td>1867-11-07</td>
      <td>1934-07-04</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rachel Carson</td>
      <td>56</td>
      <td>Biologist</td>
      <td>1907-05-27</td>
      <td>1964-04-14</td>
    </tr>
    <tr>
      <th>5</th>
      <td>John Snow</td>
      <td>45</td>
      <td>Physician</td>
      <td>1813-03-15</td>
      <td>1858-06-16</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Alan Turing</td>
      <td>41</td>
      <td>Computer Scientist</td>
      <td>1912-06-23</td>
      <td>1954-06-07</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Johann Gauss</td>
      <td>77</td>
      <td>Mathematician</td>
      <td>1777-04-30</td>
      <td>1855-02-23</td>
    </tr>
  </tbody>
</table>
</div>




```python
scientists.to_csv('scientists_clean.csv', index=False)
```


```python
# drop column full example
scientists = pd.read_csv('../data/scientists.csv', sep=',') # sep=',' is the default
scientists = pd.read_csv('../data/scientists.csv')
scientists = pd.read_csv('../data/scientists.csv', ',') # using positional argument passing for sep
print(scientists.head())

# remember you need to re-assign the 'dropped' dataframe
scientists = scientists.drop(['Born', 'Died'], axis=1)
print(scientists.head())
```

                       Name        Born        Died  Age    Occupation
    0     Rosaline Franklin  1920-07-25  1958-04-16   37       Chemist
    1        William Gosset  1876-06-13  1937-10-16   61  Statistician
    2  Florence Nightingale  1820-05-12  1910-08-13   90         Nurse
    3           Marie Curie  1867-11-07  1934-07-04   66       Chemist
    4         Rachel Carson  1907-05-27  1964-04-14   56     Biologist
                       Name  Age    Occupation
    0     Rosaline Franklin   37       Chemist
    1        William Gosset   61  Statistician
    2  Florence Nightingale   90         Nurse
    3           Marie Curie   66       Chemist
    4         Rachel Carson   56     Biologist
    


```python

```
