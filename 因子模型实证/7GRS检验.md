```python
from grs import GRS_test
import pandas as pd
import numpy as np
import os
```


```python
help(GRS_test)
```

    Help on function GRS_test in module grs:
    
    GRS_test(factor, resid, alpha)
    
    


```python
# # -*- coding: utf-8 -*-
# """
# Created on Tue Aug 10 22:33:59 2021

# @author: Administrator
# """
# import numpy as np
# from scipy.stats import f
# import scipy.stats as stats                                   #factor纵轴为时间，横轴为各因子溢价/因子收益率
# def GRS_test(factor, resid, alpha):                           #resid纵轴为时间，横轴为各投资组合的残差
#     N = resid.shape[1]                                        #alpha为定价误差的列向量
#     T = resid.shape[0]                            
#     L = factor.shape[1]      

#     if (T-N-L) < 0:
#         print('can not conduct GRS test because T-N-L<0')
#         return
#     factor = np.asmatrix(factor)                   # factor matrix (T, L)     T = 月份数
#     resid = np.asmatrix(resid)                     # residual matrix (T, N)   N = 资产组合数
#     alpha = np.asmatrix(alpha).reshape(N, 1)       # alpha matrix (N, 1)  L = 因子个数
#     mean_return_factor = (factor.mean(axis=0))#求因子T期的平均收益率
#     # covariance matrix of residuals
#     cov_resid = (resid.T * resid) / (T-L-1)
#     # covariance matrix of factors
#     cov_factor = ((factor - mean_return_factor).T * (factor - mean_return_factor)) / (T-1)
#     mean_return_factor = mean_return_factor.reshape(L, 1)
#     # GRS statistic
#     f_grs = float((T/N) * ((T-N-L)/(T-L-1)) * ((alpha.T * np.linalg.inv(cov_resid) * alpha) / (1 + mean_return_factor.T * np.linalg.inv(cov_factor) * mean_return_factor)))
#     # p-value
#     p_grs = 1 - stats.f.cdf(f_grs, N, (T-N-L))
#     return f_grs, p_grs

```

# factor数据


```python
factor_model1 = pd.read_excel("模型1facotr.xlsx")
factor_model2 = pd.read_excel("模型2facotr.xlsx")
factor_model3 = pd.read_excel("模型3facotr.xlsx")
```

# alpha、t值、残差数据


```python
ai_df = pd.read_excel('alpha表格.xlsx')
ai_t_values_df = pd.read_excel('t_values表格.xlsx')
resid_df = pd.read_excel('残差表格.xlsx')
```

# 模型1 GRS检验


```python
resid_df.columns
```




    Index(['模型1_groupby_总资产增幅年', '模型1_groupby_销售费用/总资产', '模型1_groupby_EP',
           '模型1_groupby_毛利润资产比', '模型1_groupby_应计利润', '模型2_groupby_总资产增幅年',
           '模型2_groupby_销售费用/总资产', '模型2_groupby_EP', '模型2_groupby_毛利润资产比',
           '模型2_groupby_应计利润', '模型3_groupby_总资产增幅年', '模型3_groupby_销售费用/总资产',
           '模型3_groupby_EP', '模型3_groupby_毛利润资产比', '模型3_groupby_应计利润'],
          dtype='object')




```python
factor01 = factor_model1.values
resid01 = resid_df[['模型1_groupby_总资产增幅年', '模型1_groupby_销售费用/总资产', '模型1_groupby_EP',
       '模型1_groupby_毛利润资产比', '模型1_groupby_应计利润']].values
alpha01 = ai_df[ai_df.模型号 == '模型1'].const.values
```


```python
GRS_test(factor01, resid01, alpha01)
```




    (2.5832418398243027, 0.02723448247614324)



# 模型2 GRS检验


```python
factor01 = factor_model2.values
resid01 = resid_df[['模型2_groupby_总资产增幅年', '模型2_groupby_销售费用/总资产', '模型2_groupby_EP',
       '模型2_groupby_毛利润资产比', '模型2_groupby_应计利润']].values
alpha01 = ai_df[ai_df.模型号 == '模型2'].const.values
```


```python
GRS_test(factor01, resid01, alpha01)
```




    (7.9095763365853164, 7.722714047142532e-07)



# 模型3 GRS检验


```python
factor01 = factor_model3.values
resid01 = resid_df[['模型3_groupby_总资产增幅年', '模型3_groupby_销售费用/总资产', '模型3_groupby_EP',
       '模型3_groupby_毛利润资产比', '模型3_groupby_应计利润']].values
alpha01 = ai_df[ai_df.模型号 == '模型3'].const.values
```


```python
GRS_test(factor01, resid01, alpha01)
```




    (7.9981092183672855, 6.54038734060336e-07)


