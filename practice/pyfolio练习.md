```python
import pandas as pd
import tushare as ts
import pyfolio as pf
```

    c:\users\13631\appdata\local\programs\python\python38\lib\site-packages\pyfolio\pos.py:26: UserWarning: Module "zipline.assets" not found; mutltipliers will not be applied to position notionals.
      warnings.warn(



```python
# load data
def get_return(code):
    df = ts.get_k_data(code, start='2010-01-01')
    df.index = pd.to_datetime(df.date)
    return df.close.pct_change().fillna(0).tz_localize("UTC")
```


```python
ret = get_return("600519")
```

    本接口即将停止更新，请尽快使用Pro版接口：https://tushare.pro/document/2



```python
ret
```




    date
    2010-01-04 00:00:00+00:00    0.000000
    2010-01-05 00:00:00+00:00   -0.002942
    2010-01-06 00:00:00+00:00   -0.015815
    2010-01-07 00:00:00+00:00   -0.018230
    2010-01-08 00:00:00+00:00   -0.010509
                                   ...   
    2021-06-22 00:00:00+00:00   -0.003204
    2021-06-23 00:00:00+00:00   -0.017817
    2021-06-24 00:00:00+00:00    0.014745
    2021-06-25 00:00:00+00:00    0.011581
    2021-06-28 00:00:00+00:00    0.005263
    Name: close, Length: 2784, dtype: float64




```python
benchmark_ret=get_return('sh')

benchmark_ret_sz=get_return('sz')
```

    本接口即将停止更新，请尽快使用Pro版接口：https://tushare.pro/document/2
    本接口即将停止更新，请尽快使用Pro版接口：https://tushare.pro/document/2



```python
benchmark_ret
```




    date
    2010-01-04 00:00:00+00:00    0.000000
    2010-01-05 00:00:00+00:00    0.011844
    2010-01-06 00:00:00+00:00   -0.008520
    2010-01-07 00:00:00+00:00   -0.018880
    2010-01-08 00:00:00+00:00    0.001009
                                   ...   
    2021-06-22 00:00:00+00:00    0.007999
    2021-06-23 00:00:00+00:00    0.002477
    2021-06-24 00:00:00+00:00    0.000121
    2021-06-25 00:00:00+00:00    0.011470
    2021-06-28 00:00:00+00:00   -0.000330
    Name: close, Length: 2790, dtype: float64




```python
(ret+1).cumprod().plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x245ec82c340>




![png](pyfolio%E7%BB%83%E4%B9%A0_files/pyfolio%E7%BB%83%E4%B9%A0_6_1.png)



```python
(benchmark_ret+1).cumprod().plot()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x245ea6f9fa0>




![png](pyfolio%E7%BB%83%E4%B9%A0_files/pyfolio%E7%BB%83%E4%B9%A0_7_1.png)



```python
date='2021-01-03'
```


```python
pf.create_full_tear_sheet(returns=ret,benchmark_rets=benchmark_ret,live_start_date='2017-01-03')
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;"><th>Start date</th><td colspan=4>2010-01-04</td></tr>
    <tr style="text-align: right;"><th>End date</th><td colspan=4>2021-06-28</td></tr>
    <tr style="text-align: right;"><th>In-sample months</th><td colspan=4>80</td></tr>
    <tr style="text-align: right;"><th>Out-of-sample months</th><td colspan=4>51</td></tr>
    <tr style="text-align: right;">
      <th></th>
      <th>In-sample</th>
      <th>Out-of-sample</th>
      <th>All</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Annual return</th>
      <td>17.7%</td>
      <td>54.0%</td>
      <td>30.8%</td>
    </tr>
    <tr>
      <th>Cumulative returns</th>
      <td>199.3%</td>
      <td>548.0%</td>
      <td>1839.2%</td>
    </tr>
    <tr>
      <th>Annual volatility</th>
      <td>30.9%</td>
      <td>31.5%</td>
      <td>31.2%</td>
    </tr>
    <tr>
      <th>Sharpe ratio</th>
      <td>0.68</td>
      <td>1.53</td>
      <td>1.02</td>
    </tr>
    <tr>
      <th>Calmar ratio</th>
      <td>0.33</td>
      <td>1.61</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>Stability</th>
      <td>0.58</td>
      <td>0.94</td>
      <td>0.88</td>
    </tr>
    <tr>
      <th>Max drawdown</th>
      <td>-53.3%</td>
      <td>-33.5%</td>
      <td>-53.3%</td>
    </tr>
    <tr>
      <th>Omega ratio</th>
      <td>1.13</td>
      <td>1.30</td>
      <td>1.19</td>
    </tr>
    <tr>
      <th>Sortino ratio</th>
      <td>1.02</td>
      <td>2.39</td>
      <td>1.55</td>
    </tr>
    <tr>
      <th>Skew</th>
      <td>0.19</td>
      <td>0.05</td>
      <td>0.14</td>
    </tr>
    <tr>
      <th>Kurtosis</th>
      <td>2.66</td>
      <td>1.89</td>
      <td>2.34</td>
    </tr>
    <tr>
      <th>Tail ratio</th>
      <td>1.11</td>
      <td>1.37</td>
      <td>1.21</td>
    </tr>
    <tr>
      <th>Daily value at risk</th>
      <td>-3.8%</td>
      <td>-3.8%</td>
      <td>-3.8%</td>
    </tr>
    <tr>
      <th>Alpha</th>
      <td>0.22</td>
      <td>0.54</td>
      <td>0.34</td>
    </tr>
    <tr>
      <th>Beta</th>
      <td>0.59</td>
      <td>1.05</td>
      <td>0.71</td>
    </tr>
  </tbody>
</table>



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Worst drawdown periods</th>
      <th>Net drawdown in %</th>
      <th>Peak date</th>
      <th>Valley date</th>
      <th>Recovery date</th>
      <th>Duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>53.31</td>
      <td>2012-07-13</td>
      <td>2014-01-15</td>
      <td>2015-04-16</td>
      <td>720</td>
    </tr>
    <tr>
      <th>1</th>
      <td>33.79</td>
      <td>2015-05-25</td>
      <td>2015-08-24</td>
      <td>2016-04-06</td>
      <td>228</td>
    </tr>
    <tr>
      <th>2</th>
      <td>33.50</td>
      <td>2018-06-12</td>
      <td>2018-10-30</td>
      <td>2019-03-01</td>
      <td>189</td>
    </tr>
    <tr>
      <th>3</th>
      <td>27.76</td>
      <td>2021-02-10</td>
      <td>2021-05-10</td>
      <td>NaT</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27.17</td>
      <td>2010-02-11</td>
      <td>2010-06-29</td>
      <td>2010-10-08</td>
      <td>172</td>
    </tr>
  </tbody>
</table>


    c:\users\13631\appdata\local\programs\python\python38\lib\site-packages\pandas\core\indexes\base.py:5277: FutureWarning: Indexing a timezone-aware DatetimeIndex with a timezone-naive datetime is deprecated and will raise KeyError in a future version.  Use a timezone-aware object instead.
      start_slice, end_slice = self.slice_locs(start, end, step=step, kind=kind)



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Stress Events</th>
      <th>mean</th>
      <th>min</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>US downgrade/European Debt Crisis</th>
      <td>0.06%</td>
      <td>-2.66%</td>
      <td>4.38%</td>
    </tr>
    <tr>
      <th>Fukushima</th>
      <td>-0.18%</td>
      <td>-2.10%</td>
      <td>3.95%</td>
    </tr>
    <tr>
      <th>EZB IR Event</th>
      <td>0.06%</td>
      <td>-3.65%</td>
      <td>2.65%</td>
    </tr>
    <tr>
      <th>Flash Crash</th>
      <td>0.96%</td>
      <td>-2.63%</td>
      <td>2.72%</td>
    </tr>
    <tr>
      <th>Apr14</th>
      <td>0.30%</td>
      <td>-6.30%</td>
      <td>5.04%</td>
    </tr>
    <tr>
      <th>Oct14</th>
      <td>-0.19%</td>
      <td>-1.84%</td>
      <td>1.56%</td>
    </tr>
    <tr>
      <th>Fall2015</th>
      <td>-0.27%</td>
      <td>-8.96%</td>
      <td>7.17%</td>
    </tr>
    <tr>
      <th>Recovery</th>
      <td>0.06%</td>
      <td>-7.32%</td>
      <td>8.36%</td>
    </tr>
    <tr>
      <th>New Normal</th>
      <td>0.15%</td>
      <td>-10.00%</td>
      <td>10.00%</td>
    </tr>
  </tbody>
</table>


    c:\users\13631\appdata\local\programs\python\python38\lib\site-packages\pandas\core\indexes\base.py:5277: FutureWarning: Indexing a timezone-aware DatetimeIndex with a timezone-naive datetime is deprecated and will raise KeyError in a future version.  Use a timezone-aware object instead.
      start_slice, end_slice = self.slice_locs(start, end, step=step, kind=kind)



![png](pyfolio%E7%BB%83%E4%B9%A0_files/pyfolio%E7%BB%83%E4%B9%A0_9_5.png)



![png](pyfolio%E7%BB%83%E4%B9%A0_files/pyfolio%E7%BB%83%E4%B9%A0_9_6.png)



```python
pf.create_full_tear_sheet(returns=ret,benchmark_rets=benchmark_ret,live_start_date='2020-01-03')
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;"><th>Start date</th><td colspan=4>2010-01-04</td></tr>
    <tr style="text-align: right;"><th>End date</th><td colspan=4>2021-06-28</td></tr>
    <tr style="text-align: right;"><th>In-sample months</th><td colspan=4>115</td></tr>
    <tr style="text-align: right;"><th>Out-of-sample months</th><td colspan=4>17</td></tr>
    <tr style="text-align: right;">
      <th></th>
      <th>In-sample</th>
      <th>Out-of-sample</th>
      <th>All</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Annual return</th>
      <td>27.6%</td>
      <td>54.8%</td>
      <td>30.8%</td>
    </tr>
    <tr>
      <th>Cumulative returns</th>
      <td>942.0%</td>
      <td>86.1%</td>
      <td>1839.2%</td>
    </tr>
    <tr>
      <th>Annual volatility</th>
      <td>31.1%</td>
      <td>32.0%</td>
      <td>31.2%</td>
    </tr>
    <tr>
      <th>Sharpe ratio</th>
      <td>0.94</td>
      <td>1.53</td>
      <td>1.02</td>
    </tr>
    <tr>
      <th>Calmar ratio</th>
      <td>0.52</td>
      <td>1.98</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>Stability</th>
      <td>0.83</td>
      <td>0.88</td>
      <td>0.88</td>
    </tr>
    <tr>
      <th>Max drawdown</th>
      <td>-53.3%</td>
      <td>-27.8%</td>
      <td>-53.3%</td>
    </tr>
    <tr>
      <th>Omega ratio</th>
      <td>1.18</td>
      <td>1.29</td>
      <td>1.19</td>
    </tr>
    <tr>
      <th>Sortino ratio</th>
      <td>1.43</td>
      <td>2.28</td>
      <td>1.55</td>
    </tr>
    <tr>
      <th>Skew</th>
      <td>0.19</td>
      <td>-0.22</td>
      <td>0.14</td>
    </tr>
    <tr>
      <th>Kurtosis</th>
      <td>2.52</td>
      <td>1.26</td>
      <td>2.34</td>
    </tr>
    <tr>
      <th>Tail ratio</th>
      <td>1.19</td>
      <td>1.27</td>
      <td>1.21</td>
    </tr>
    <tr>
      <th>Daily value at risk</th>
      <td>-3.8%</td>
      <td>-3.8%</td>
      <td>-3.8%</td>
    </tr>
    <tr>
      <th>Alpha</th>
      <td>0.33</td>
      <td>0.42</td>
      <td>0.34</td>
    </tr>
    <tr>
      <th>Beta</th>
      <td>0.67</td>
      <td>1.06</td>
      <td>0.71</td>
    </tr>
  </tbody>
</table>



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Worst drawdown periods</th>
      <th>Net drawdown in %</th>
      <th>Peak date</th>
      <th>Valley date</th>
      <th>Recovery date</th>
      <th>Duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>53.31</td>
      <td>2012-07-13</td>
      <td>2014-01-15</td>
      <td>2015-04-16</td>
      <td>720</td>
    </tr>
    <tr>
      <th>1</th>
      <td>33.79</td>
      <td>2015-05-25</td>
      <td>2015-08-24</td>
      <td>2016-04-06</td>
      <td>228</td>
    </tr>
    <tr>
      <th>2</th>
      <td>33.50</td>
      <td>2018-06-12</td>
      <td>2018-10-30</td>
      <td>2019-03-01</td>
      <td>189</td>
    </tr>
    <tr>
      <th>3</th>
      <td>27.76</td>
      <td>2021-02-10</td>
      <td>2021-05-10</td>
      <td>NaT</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27.17</td>
      <td>2010-02-11</td>
      <td>2010-06-29</td>
      <td>2010-10-08</td>
      <td>172</td>
    </tr>
  </tbody>
</table>


    c:\users\13631\appdata\local\programs\python\python38\lib\site-packages\pandas\core\indexes\base.py:5277: FutureWarning: Indexing a timezone-aware DatetimeIndex with a timezone-naive datetime is deprecated and will raise KeyError in a future version.  Use a timezone-aware object instead.
      start_slice, end_slice = self.slice_locs(start, end, step=step, kind=kind)



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Stress Events</th>
      <th>mean</th>
      <th>min</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>US downgrade/European Debt Crisis</th>
      <td>0.06%</td>
      <td>-2.66%</td>
      <td>4.38%</td>
    </tr>
    <tr>
      <th>Fukushima</th>
      <td>-0.18%</td>
      <td>-2.10%</td>
      <td>3.95%</td>
    </tr>
    <tr>
      <th>EZB IR Event</th>
      <td>0.06%</td>
      <td>-3.65%</td>
      <td>2.65%</td>
    </tr>
    <tr>
      <th>Flash Crash</th>
      <td>0.96%</td>
      <td>-2.63%</td>
      <td>2.72%</td>
    </tr>
    <tr>
      <th>Apr14</th>
      <td>0.30%</td>
      <td>-6.30%</td>
      <td>5.04%</td>
    </tr>
    <tr>
      <th>Oct14</th>
      <td>-0.19%</td>
      <td>-1.84%</td>
      <td>1.56%</td>
    </tr>
    <tr>
      <th>Fall2015</th>
      <td>-0.27%</td>
      <td>-8.96%</td>
      <td>7.17%</td>
    </tr>
    <tr>
      <th>Recovery</th>
      <td>0.06%</td>
      <td>-7.32%</td>
      <td>8.36%</td>
    </tr>
    <tr>
      <th>New Normal</th>
      <td>0.15%</td>
      <td>-10.00%</td>
      <td>10.00%</td>
    </tr>
  </tbody>
</table>


    c:\users\13631\appdata\local\programs\python\python38\lib\site-packages\pandas\core\indexes\base.py:5277: FutureWarning: Indexing a timezone-aware DatetimeIndex with a timezone-naive datetime is deprecated and will raise KeyError in a future version.  Use a timezone-aware object instead.
      start_slice, end_slice = self.slice_locs(start, end, step=step, kind=kind)



![png](pyfolio%E7%BB%83%E4%B9%A0_files/pyfolio%E7%BB%83%E4%B9%A0_10_5.png)



![png](pyfolio%E7%BB%83%E4%B9%A0_files/pyfolio%E7%BB%83%E4%B9%A0_10_6.png)



```python
pf.create_full_tear_sheet(returns=ret,benchmark_rets=benchmark_ret_sz,live_start_date='2020-01-03')
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;"><th>Start date</th><td colspan=4>2010-01-04</td></tr>
    <tr style="text-align: right;"><th>End date</th><td colspan=4>2021-06-28</td></tr>
    <tr style="text-align: right;"><th>In-sample months</th><td colspan=4>115</td></tr>
    <tr style="text-align: right;"><th>Out-of-sample months</th><td colspan=4>17</td></tr>
    <tr style="text-align: right;">
      <th></th>
      <th>In-sample</th>
      <th>Out-of-sample</th>
      <th>All</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Annual return</th>
      <td>27.6%</td>
      <td>54.8%</td>
      <td>30.8%</td>
    </tr>
    <tr>
      <th>Cumulative returns</th>
      <td>942.0%</td>
      <td>86.1%</td>
      <td>1839.2%</td>
    </tr>
    <tr>
      <th>Annual volatility</th>
      <td>31.1%</td>
      <td>32.0%</td>
      <td>31.2%</td>
    </tr>
    <tr>
      <th>Sharpe ratio</th>
      <td>0.94</td>
      <td>1.53</td>
      <td>1.02</td>
    </tr>
    <tr>
      <th>Calmar ratio</th>
      <td>0.52</td>
      <td>1.98</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>Stability</th>
      <td>0.83</td>
      <td>0.88</td>
      <td>0.88</td>
    </tr>
    <tr>
      <th>Max drawdown</th>
      <td>-53.3%</td>
      <td>-27.8%</td>
      <td>-53.3%</td>
    </tr>
    <tr>
      <th>Omega ratio</th>
      <td>1.18</td>
      <td>1.29</td>
      <td>1.19</td>
    </tr>
    <tr>
      <th>Sortino ratio</th>
      <td>1.43</td>
      <td>2.28</td>
      <td>1.55</td>
    </tr>
    <tr>
      <th>Skew</th>
      <td>0.19</td>
      <td>-0.22</td>
      <td>0.14</td>
    </tr>
    <tr>
      <th>Kurtosis</th>
      <td>2.52</td>
      <td>1.26</td>
      <td>2.34</td>
    </tr>
    <tr>
      <th>Tail ratio</th>
      <td>1.19</td>
      <td>1.27</td>
      <td>1.21</td>
    </tr>
    <tr>
      <th>Daily value at risk</th>
      <td>-3.8%</td>
      <td>-3.8%</td>
      <td>-3.8%</td>
    </tr>
    <tr>
      <th>Alpha</th>
      <td>0.34</td>
      <td>0.30</td>
      <td>0.34</td>
    </tr>
    <tr>
      <th>Beta</th>
      <td>0.56</td>
      <td>0.80</td>
      <td>0.59</td>
    </tr>
  </tbody>
</table>



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Worst drawdown periods</th>
      <th>Net drawdown in %</th>
      <th>Peak date</th>
      <th>Valley date</th>
      <th>Recovery date</th>
      <th>Duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>53.31</td>
      <td>2012-07-13</td>
      <td>2014-01-15</td>
      <td>2015-04-16</td>
      <td>720</td>
    </tr>
    <tr>
      <th>1</th>
      <td>33.79</td>
      <td>2015-05-25</td>
      <td>2015-08-24</td>
      <td>2016-04-06</td>
      <td>228</td>
    </tr>
    <tr>
      <th>2</th>
      <td>33.50</td>
      <td>2018-06-12</td>
      <td>2018-10-30</td>
      <td>2019-03-01</td>
      <td>189</td>
    </tr>
    <tr>
      <th>3</th>
      <td>27.76</td>
      <td>2021-02-10</td>
      <td>2021-05-10</td>
      <td>NaT</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>27.17</td>
      <td>2010-02-11</td>
      <td>2010-06-29</td>
      <td>2010-10-08</td>
      <td>172</td>
    </tr>
  </tbody>
</table>


    c:\users\13631\appdata\local\programs\python\python38\lib\site-packages\pandas\core\indexes\base.py:5277: FutureWarning: Indexing a timezone-aware DatetimeIndex with a timezone-naive datetime is deprecated and will raise KeyError in a future version.  Use a timezone-aware object instead.
      start_slice, end_slice = self.slice_locs(start, end, step=step, kind=kind)



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Stress Events</th>
      <th>mean</th>
      <th>min</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>US downgrade/European Debt Crisis</th>
      <td>0.06%</td>
      <td>-2.66%</td>
      <td>4.38%</td>
    </tr>
    <tr>
      <th>Fukushima</th>
      <td>-0.18%</td>
      <td>-2.10%</td>
      <td>3.95%</td>
    </tr>
    <tr>
      <th>EZB IR Event</th>
      <td>0.06%</td>
      <td>-3.65%</td>
      <td>2.65%</td>
    </tr>
    <tr>
      <th>Flash Crash</th>
      <td>0.96%</td>
      <td>-2.63%</td>
      <td>2.72%</td>
    </tr>
    <tr>
      <th>Apr14</th>
      <td>0.30%</td>
      <td>-6.30%</td>
      <td>5.04%</td>
    </tr>
    <tr>
      <th>Oct14</th>
      <td>-0.19%</td>
      <td>-1.84%</td>
      <td>1.56%</td>
    </tr>
    <tr>
      <th>Fall2015</th>
      <td>-0.27%</td>
      <td>-8.96%</td>
      <td>7.17%</td>
    </tr>
    <tr>
      <th>Recovery</th>
      <td>0.06%</td>
      <td>-7.32%</td>
      <td>8.36%</td>
    </tr>
    <tr>
      <th>New Normal</th>
      <td>0.15%</td>
      <td>-10.00%</td>
      <td>10.00%</td>
    </tr>
  </tbody>
</table>


    c:\users\13631\appdata\local\programs\python\python38\lib\site-packages\pandas\core\indexes\base.py:5277: FutureWarning: Indexing a timezone-aware DatetimeIndex with a timezone-naive datetime is deprecated and will raise KeyError in a future version.  Use a timezone-aware object instead.
      start_slice, end_slice = self.slice_locs(start, end, step=step, kind=kind)



![png](pyfolio%E7%BB%83%E4%B9%A0_files/pyfolio%E7%BB%83%E4%B9%A0_11_5.png)



![png](pyfolio%E7%BB%83%E4%B9%A0_files/pyfolio%E7%BB%83%E4%B9%A0_11_6.png)



```python

```
