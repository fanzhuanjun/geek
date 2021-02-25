```python
import pandas as pd
```


```python
import seaborn as sns
```


```python
tips = sns.load_dataset('tips')
```


```python
tips.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
import statsmodels.formula.api as smf
```


```python
model = smf.ols('tip ~ total_bill', data=tips)
```


```python
results = model.fit()
```


```python
results.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>           <td>tip</td>       <th>  R-squared:         </th> <td>   0.457</td>
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.454</td>
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   203.4</td>
</tr>
<tr>
  <th>Date:</th>             <td>Fri, 11 May 2018</td> <th>  Prob (F-statistic):</th> <td>6.69e-34</td>
</tr>
<tr>
  <th>Time:</th>                 <td>18:19:28</td>     <th>  Log-Likelihood:    </th> <td> -350.54</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>   244</td>      <th>  AIC:               </th> <td>   705.1</td>
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   242</td>      <th>  BIC:               </th> <td>   712.1</td>
</tr>
<tr>
  <th>Df Model:</th>              <td>     1</td>      <th>                     </th>     <td> </td>   
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   
</tr>
</table>
<table class="simpletable">
<tr>
       <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>Intercept</th>  <td>    0.9203</td> <td>    0.160</td> <td>    5.761</td> <td> 0.000</td> <td>    0.606</td> <td>    1.235</td>
</tr>
<tr>
  <th>total_bill</th> <td>    0.1050</td> <td>    0.007</td> <td>   14.260</td> <td> 0.000</td> <td>    0.091</td> <td>    0.120</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>20.185</td> <th>  Durbin-Watson:     </th> <td>   2.151</td>
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  37.750</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 0.443</td> <th>  Prob(JB):          </th> <td>6.35e-09</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 4.711</td> <th>  Cond. No.          </th> <td>    53.0</td>
</tr>
</table>




```python
results.params
```




    Intercept     0.920270
    total_bill    0.105025
    dtype: float64




```python
from sklearn import linear_model
```


```python
lr = linear_model.LinearRegression()
```


```python
predicted = lr.fit(X=tips['total_bill'], y=tips['tip'])
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-17-3a4caf5accd0> in <module>()
    ----> 1 predicted = lr.fit(X=tips['total_bill'], y=tips['tip'])
    

    ~\Anaconda3\lib\site-packages\sklearn\linear_model\base.py in fit(self, X, y, sample_weight)
        480         n_jobs_ = self.n_jobs
        481         X, y = check_X_y(X, y, accept_sparse=['csr', 'csc', 'coo'],
    --> 482                          y_numeric=True, multi_output=True)
        483 
        484         if sample_weight is not None and np.atleast_1d(sample_weight).ndim > 1:
    

    ~\Anaconda3\lib\site-packages\sklearn\utils\validation.py in check_X_y(X, y, accept_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, multi_output, ensure_min_samples, ensure_min_features, y_numeric, warn_on_dtype, estimator)
        571     X = check_array(X, accept_sparse, dtype, order, copy, force_all_finite,
        572                     ensure_2d, allow_nd, ensure_min_samples,
    --> 573                     ensure_min_features, warn_on_dtype, estimator)
        574     if multi_output:
        575         y = check_array(y, 'csr', force_all_finite=True, ensure_2d=False,
    

    ~\Anaconda3\lib\site-packages\sklearn\utils\validation.py in check_array(array, accept_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, warn_on_dtype, estimator)
        439                     "Reshape your data either using array.reshape(-1, 1) if "
        440                     "your data has a single feature or array.reshape(1, -1) "
    --> 441                     "if it contains a single sample.".format(array))
        442             array = np.atleast_2d(array)
        443             # To ensure that array flags are maintained
    

    ValueError: Expected 2D array, got 1D array instead:
    array=[ 16.99  10.34  21.01  23.68  24.59  25.29   8.77  26.88  15.04  14.78
      10.27  35.26  15.42  18.43  14.83  21.58  10.33  16.29  16.97  20.65
      17.92  20.29  15.77  39.42  19.82  17.81  13.37  12.69  21.7   19.65
       9.55  18.35  15.06  20.69  17.78  24.06  16.31  16.93  18.69  31.27
      16.04  17.46  13.94   9.68  30.4   18.29  22.23  32.4   28.55  18.04
      12.54  10.29  34.81   9.94  25.56  19.49  38.01  26.41  11.24  48.27
      20.29  13.81  11.02  18.29  17.59  20.08  16.45   3.07  20.23  15.01
      12.02  17.07  26.86  25.28  14.73  10.51  17.92  27.2   22.76  17.29
      19.44  16.66  10.07  32.68  15.98  34.83  13.03  18.28  24.71  21.16
      28.97  22.49   5.75  16.32  22.75  40.17  27.28  12.03  21.01  12.46
      11.35  15.38  44.3   22.42  20.92  15.36  20.49  25.21  18.24  14.31  14.
       7.25  38.07  23.95  25.71  17.31  29.93  10.65  12.43  24.08  11.69
      13.42  14.26  15.95  12.48  29.8    8.52  14.52  11.38  22.82  19.08
      20.27  11.17  12.26  18.26   8.51  10.33  14.15  16.    13.16  17.47
      34.3   41.19  27.05  16.43   8.35  18.64  11.87   9.78   7.51  14.07
      13.13  17.26  24.55  19.77  29.85  48.17  25.    13.39  16.49  21.5
      12.66  16.21  13.81  17.51  24.52  20.76  31.71  10.59  10.63  50.81
      15.81   7.25  31.85  16.82  32.9   17.89  14.48   9.6   34.63  34.65
      23.33  45.35  23.17  40.55  20.69  20.9   30.46  18.15  23.1   15.69
      19.81  28.44  15.48  16.58   7.56  10.34  43.11  13.    13.51  18.71
      12.74  13.    16.4   20.53  16.47  26.59  38.73  24.27  12.76  30.06
      25.89  48.33  13.27  28.17  12.9   28.15  11.59   7.74  30.14  12.16
      13.42   8.58  15.98  13.42  16.27  10.09  20.45  13.28  22.12  24.01
      15.69  11.61  10.77  15.53  10.07  12.6   32.83  35.83  29.03  27.18
      22.67  17.82  18.78].
    Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.



```python
predicted = lr.fit(X=tips['total_bill'].values.reshape(-1, 1),
                   y=tips['tip'])
```


```python
predicted.coef_
```




    array([ 0.10502452])




```python
predicted.intercept_
```




    0.92026961355467352




```python
tips.columns
```




    Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='object')




```python
model = smf.ols('tip ~ total_bill + sex', data=tips).fit()
```


```python
model.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>           <td>tip</td>       <th>  R-squared:         </th> <td>   0.457</td>
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.452</td>
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   101.3</td>
</tr>
<tr>
  <th>Date:</th>             <td>Fri, 11 May 2018</td> <th>  Prob (F-statistic):</th> <td>1.18e-32</td>
</tr>
<tr>
  <th>Time:</th>                 <td>18:20:35</td>     <th>  Log-Likelihood:    </th> <td> -350.52</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>   244</td>      <th>  AIC:               </th> <td>   707.0</td>
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   241</td>      <th>  BIC:               </th> <td>   717.5</td>
</tr>
<tr>
  <th>Df Model:</th>              <td>     2</td>      <th>                     </th>     <td> </td>   
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   
</tr>
</table>
<table class="simpletable">
<tr>
        <td></td>           <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>Intercept</th>     <td>    0.9067</td> <td>    0.175</td> <td>    5.182</td> <td> 0.000</td> <td>    0.562</td> <td>    1.251</td>
</tr>
<tr>
  <th>sex[T.Female]</th> <td>    0.0266</td> <td>    0.138</td> <td>    0.192</td> <td> 0.848</td> <td>   -0.246</td> <td>    0.299</td>
</tr>
<tr>
  <th>total_bill</th>    <td>    0.1052</td> <td>    0.007</td> <td>   14.110</td> <td> 0.000</td> <td>    0.091</td> <td>    0.120</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>20.499</td> <th>  Durbin-Watson:     </th> <td>   2.149</td>
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  38.652</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 0.447</td> <th>  Prob(JB):          </th> <td>4.05e-09</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 4.733</td> <th>  Cond. No.          </th> <td>    63.0</td>
</tr>
</table>




```python
lr = linear_model.LinearRegression()
```


```python
predicted = lr.fit(tips[['total_bill', 'sex']], tips['tip'])
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-25-1e0106ce31da> in <module>()
    ----> 1 predicted = lr.fit(tips[['total_bill', 'sex']], tips['tip'])
    

    ~\Anaconda3\lib\site-packages\sklearn\linear_model\base.py in fit(self, X, y, sample_weight)
        480         n_jobs_ = self.n_jobs
        481         X, y = check_X_y(X, y, accept_sparse=['csr', 'csc', 'coo'],
    --> 482                          y_numeric=True, multi_output=True)
        483 
        484         if sample_weight is not None and np.atleast_1d(sample_weight).ndim > 1:
    

    ~\Anaconda3\lib\site-packages\sklearn\utils\validation.py in check_X_y(X, y, accept_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, multi_output, ensure_min_samples, ensure_min_features, y_numeric, warn_on_dtype, estimator)
        571     X = check_array(X, accept_sparse, dtype, order, copy, force_all_finite,
        572                     ensure_2d, allow_nd, ensure_min_samples,
    --> 573                     ensure_min_features, warn_on_dtype, estimator)
        574     if multi_output:
        575         y = check_array(y, 'csr', force_all_finite=True, ensure_2d=False,
    

    ~\Anaconda3\lib\site-packages\sklearn\utils\validation.py in check_array(array, accept_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, warn_on_dtype, estimator)
        446         # make sure we actually converted to numeric:
        447         if dtype_numeric and array.dtype.kind == "O":
    --> 448             array = array.astype(np.float64)
        449         if not allow_nd and array.ndim >= 3:
        450             raise ValueError("Found array with dim %d. %s expected <= 2."
    

    ValueError: could not convert string to float: 'Female'



```python
tips_dummy = pd.get_dummies(tips[['total_bill', 'sex', 'tip']])
```


```python
tips_dummy.head()
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
      <th>total_bill</th>
      <th>tip</th>
      <th>sex_Male</th>
      <th>sex_Female</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
tips.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 244 entries, 0 to 243
    Data columns (total 7 columns):
    total_bill    244 non-null float64
    tip           244 non-null float64
    sex           244 non-null category
    smoker        244 non-null category
    day           244 non-null category
    time          244 non-null category
    size          244 non-null int64
    dtypes: category(4), float64(2), int64(1)
    memory usage: 7.2 KB
    


```python
tips_dummy = pd.get_dummies(tips[['tip', 'total_bill', 'sex']], drop_first=True)
tips_dummy.head()
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
      <th>tip</th>
      <th>total_bill</th>
      <th>sex_Female</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.01</td>
      <td>16.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.66</td>
      <td>10.34</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.50</td>
      <td>21.01</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.31</td>
      <td>23.68</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.61</td>
      <td>24.59</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
predicted = lr.fit(tips_dummy.iloc[:, 1:], tips_dummy['tip'])
```


```python
predicted.coef_
```




    array([ 0.10523236,  0.02660871])




```python
tips_dummy.head()
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
      <th>tip</th>
      <th>total_bill</th>
      <th>sex_Female</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.01</td>
      <td>16.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.66</td>
      <td>10.34</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.50</td>
      <td>21.01</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.31</td>
      <td>23.68</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.61</td>
      <td>24.59</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
from patsy import dmatrices
```


```python
response, predictors = dmatrices('tip ~ total_bill + sex', data = tips)
```


```python
#response
```


```python
#predictors
```


```python
predicted = lr.fit(predictors, response)
```


```python
predicted.coef_
```




    array([[ 0.        ,  0.02660871,  0.10523236]])




```python

```
