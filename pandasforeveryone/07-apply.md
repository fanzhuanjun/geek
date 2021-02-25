```python
def my_function():
    pass
```


```python
def my_sq(x):
    return x ** 2
```


```python
my_sq(4)
```




    16




```python
def avg_2(x, y):
    return (x + y) / 2
```


```python
avg_2(10, 20)
```




    15.0




```python
assert avg_2(10, 20) == 15.0
```


```python
import pandas as pd
```


```python
df=pd.DataFrame({'a':[10,20,30],
                 'b':[20,30,40]})
df
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
      <td>10</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['a'] ** 2
```




    0    100
    1    400
    2    900
    Name: a, dtype: int64




```python
type(df['a'])
```




    pandas.core.series.Series




```python
def my_sq(x):
    # assert isinstance(x, int)
    return x ** 2
```


```python
df['a'].apply(my_sq)
```




    0    100
    1    400
    2    900
    Name: a, dtype: int64




```python
def my_exp(x, e):
    return x ** e
```


```python
my_exp(2, 2)
```




    4




```python
my_exp(2, 10)
```




    1024




```python
df['a'].apply(my_exp, e=10)
```




    0        10000000000
    1     10240000000000
    2    590490000000000
    Name: a, dtype: int64




```python
def print_me(x):
    print(x)
```


```python
df
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
      <td>10</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.apply(print_me, axis=0)
```

    0    10
    1    20
    2    30
    Name: a, dtype: int64
    0    20
    1    30
    2    40
    Name: b, dtype: int64
    




    a    None
    b    None
    dtype: object




```python
def avg_3(x, y, z):
    return (x + y + z) / 3
```


```python
df.apply(avg_3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-49-218f9a31a3fb> in <module>()
    ----> 1 df.apply(avg_3)
    

    ~\Anaconda3\lib\site-packages\pandas\core\frame.py in apply(self, func, axis, broadcast, raw, reduce, args, **kwds)
       4260                         f, axis,
       4261                         reduce=reduce,
    -> 4262                         ignore_failures=ignore_failures)
       4263             else:
       4264                 return self._apply_broadcast(f, axis)
    

    ~\Anaconda3\lib\site-packages\pandas\core\frame.py in _apply_standard(self, func, axis, ignore_failures, reduce)
       4356             try:
       4357                 for i, v in enumerate(series_gen):
    -> 4358                     results[i] = func(v)
       4359                     keys.append(v.name)
       4360             except Exception as e:
    

    TypeError: ("avg_3() missing 2 required positional arguments: 'y' and 'z'", 'occurred at index a')



```python
def avg_3_apply(col):
    x = col[0]
    y = col[1]
    z = col[2]
    return (x + y + z) / 3
```


```python
df.apply(avg_3_apply)
```




    a    20.0
    b    30.0
    dtype: float64




```python
import numpy as np
```


```python
df.apply(np.mean)
```




    a    20.0
    b    30.0
    dtype: float64




```python
df.apply(avg_3_apply, axis=1)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    ~\Anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_value(self, series, key)
       2476             return self._engine.get_value(s, k,
    -> 2477                                           tz=getattr(series.dtype, 'tz', None))
       2478         except KeyError as e1:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_value()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_value()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 2

    
    During handling of the above exception, another exception occurred:
    

    IndexError                                Traceback (most recent call last)

    <ipython-input-55-494ba3a8068d> in <module>()
    ----> 1 df.apply(avg_3_apply, axis=1)
    

    ~\Anaconda3\lib\site-packages\pandas\core\frame.py in apply(self, func, axis, broadcast, raw, reduce, args, **kwds)
       4260                         f, axis,
       4261                         reduce=reduce,
    -> 4262                         ignore_failures=ignore_failures)
       4263             else:
       4264                 return self._apply_broadcast(f, axis)
    

    ~\Anaconda3\lib\site-packages\pandas\core\frame.py in _apply_standard(self, func, axis, ignore_failures, reduce)
       4356             try:
       4357                 for i, v in enumerate(series_gen):
    -> 4358                     results[i] = func(v)
       4359                     keys.append(v.name)
       4360             except Exception as e:
    

    <ipython-input-50-197939405228> in avg_3_apply(col)
          2     x = col[0]
          3     y = col[1]
    ----> 4     z = col[2]
          5     return (x + y + z) / 3
    

    ~\Anaconda3\lib\site-packages\pandas\core\series.py in __getitem__(self, key)
        599         key = com._apply_if_callable(key, self)
        600         try:
    --> 601             result = self.index.get_value(self, key)
        602 
        603             if not is_scalar(result):
    

    ~\Anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_value(self, series, key)
       2481 
       2482             try:
    -> 2483                 return libts.get_value_box(s, key)
       2484             except IndexError:
       2485                 raise
    

    pandas/_libs/tslib.pyx in pandas._libs.tslib.get_value_box (pandas\_libs\tslib.c:18843)()
    

    pandas/_libs/tslib.pyx in pandas._libs.tslib.get_value_box (pandas\_libs\tslib.c:18560)()
    

    IndexError: ('index out of bounds', 'occurred at index 0')



```python
df
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
      <td>10</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
def avg_2_apply(row):
    x = row[0]
    y = row[1]
    return (x + y) / 2
```


```python
df.apply(avg_2_apply, axis=1)
```




    0    15.0
    1    25.0
    2    35.0
    dtype: float64




```python
import seaborn as sns
```


```python
titanic = sns.load_dataset('titanic')
```


```python
titanic.head()
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
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
def count_missing(vec):
    """Counts the number of missing values in a vector
    """
    null_vec = pd.isnull(vec)
    null_count = np.sum(null_vec)
    return null_count
```


```python
count_missing?
```


```python
cmis_col = titanic.apply(count_missing)
```


```python
cmis_col
```




    survived         0
    pclass           0
    sex              0
    age            177
    sibsp            0
    parch            0
    fare             0
    embarked         2
    class            0
    who              0
    adult_male       0
    deck           688
    embark_town      2
    alive            0
    alone            0
    dtype: int64




```python
titanic.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 15 columns):
    survived       891 non-null int64
    pclass         891 non-null int64
    sex            891 non-null object
    age            714 non-null float64
    sibsp          891 non-null int64
    parch          891 non-null int64
    fare           891 non-null float64
    embarked       889 non-null object
    class          891 non-null category
    who            891 non-null object
    adult_male     891 non-null bool
    deck           203 non-null category
    embark_town    889 non-null object
    alive          891 non-null object
    alone          891 non-null bool
    dtypes: bool(2), category(2), float64(2), int64(4), object(5)
    memory usage: 80.6+ KB
    


```python
cmis_row = titanic.apply(count_missing, axis=1)
```


```python
cmis_row
```




    0      1
    1      0
    2      1
    3      0
    4      1
    5      2
    6      0
    7      1
    8      1
    9      1
    10     0
    11     0
    12     1
    13     1
    14     1
    15     1
    16     1
    17     2
    18     1
    19     2
    20     1
    21     0
    22     1
    23     0
    24     1
    25     1
    26     2
    27     0
    28     2
    29     2
          ..
    861    1
    862    0
    863    2
    864    1
    865    1
    866    1
    867    0
    868    2
    869    1
    870    1
    871    0
    872    0
    873    1
    874    1
    875    1
    876    1
    877    1
    878    2
    879    0
    880    1
    881    1
    882    1
    883    1
    884    1
    885    1
    886    1
    887    0
    888    2
    889    0
    890    1
    Length: 891, dtype: int64




```python
def avg_2(x, y):
    return (x + y) / 2
```


```python
df
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
      <td>10</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
avg_2(df['a'], df['b'])
```




    0    15.0
    1    25.0
    2    35.0
    dtype: float64




```python
(df['a'] + df['b']) / 2
```




    0    15.0
    1    25.0
    2    35.0
    dtype: float64




```python
def avg_2_mod(x, y):
    if (x == 20):
        return np.NaN
    else:
        return (x + y) / 2
```


```python
avg_2_mod(df['a'], df['b'])
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-76-f505383ee5b3> in <module>()
    ----> 1 avg_2_mod(df['a'], df['b'])
    

    <ipython-input-75-3f3863d28509> in avg_2_mod(x, y)
          1 def avg_2_mod(x, y):
    ----> 2     if (x == 20):
          3         return np.NaN
          4     else:
          5         return (x + y) / 2
    

    ~\Anaconda3\lib\site-packages\pandas\core\generic.py in __nonzero__(self)
        953         raise ValueError("The truth value of a {0} is ambiguous. "
        954                          "Use a.empty, a.bool(), a.item(), a.any() or a.all()."
    --> 955                          .format(self.__class__.__name__))
        956 
        957     __bool__ = __nonzero__
    

    ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().



```python
avg_2_mod(10, 20)
```




    15.0




```python
avg_2_mod(20, 30)
```




    nan




```python
import numpy as np
```


```python
avg_2_mod_vec = np.vectorize(avg_2_mod)
```


```python
df
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
      <td>10</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
avg_2_mod_vec(df['a'], df['b'])
```




    array([ 15.,  nan,  35.])




```python
@np.vectorize
def v_avg_2_mod(x, y):
    if (x == 20):
        return np.NaN
    else:
        return (x + y) / 2
```


```python
v_avg_2_mod(df['a'], df['b'])
```




    array([ 15.,  nan,  35.])




```python
import numba
```


```python
@numba.vectorize
def v_avg_2_mod_numba(x, y):
    if (x == 20):
        return np.NaN
    else:
        return (x + y) / 2
```


```python
v_avg_2_mod_numba(df['a'].values, df['b'].values)
```




    array([ 15.,  nan,  35.])




```python
%%timeit
avg_2(df['a'], df['b'])
```

    528 µs ± 20.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    


```python
%%timeit
v_avg_2_mod(df['a'], df['b'])
```

    138 µs ± 1.55 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    


```python
%%timeit
v_avg_2_mod_numba(df['a'].values, df['b'].values)
```

    16.6 µs ± 288 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    


```python

```
