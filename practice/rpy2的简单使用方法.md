# rpy2 的简单使用方法

欢迎转载，不过请注明来源，不然我顺着网线去打你的头。



## 0. 写在最前

先放一下官方文档：https://rpy2.github.io/doc/latest/html/pandas.html

经济学科用 python 的同学，经常会碰到一个烦人的问题，就是 python 中缺少太多计量经济学和时间序列分析的包，做起来很不方便。对于有很多统计包 R 语言，我也心向往之，但是无奈限于时间关系，没有好好学习 R，但是又想有时候运用 R，那么你们的福音来啦。python 的 rpy2 库就能完美解决你的问题。

这篇文章不会讲很多关于 rpy2 的方法，而是用最经济使用的方法，尽量用 python 来导入数据，只在模型处才使用 R 语言的包。

首先，需要先下载 rpy2，下载方式很简单，与其他库没差（在这里要注意，R语言要预先下载好，同时你所将要使用的包也要事先在 R 中 install）

```
pip install rpy2
```

然后，在 python 的编程环境中尝试如下语句：

```python
import rpy2
print(rpy2.__version__)
```

如果没有出错，那么恭喜你，可以开始我们的旅途了！这次，我们将尝试在 python 中导入 R 包构建 arima-garch 模型。



## 1. 导入 R 包

在 python 中导入 R 包前一定要确保已经在 R 语言中安装该包。在 python 导入 R 包的语句如下

```python
from rpy2.robjects.packages import importr
# import R's "base" package
base = importr('base')

# import R's "utils" package
utils = importr('utils')
```

由于我们构建 Arima-Garch 模型，所以也要导入相关的包，代码如下（谨记：请一定在 R 中先 `install.packages('fGarch')`）

```python
from rpy2.robjects.packages import importr
importr('fGarch')
```



## 2. 数据转换

- 导入数据

这部当然玩 python 的朋友很清楚啦，这里尝试一个全球股票指数的数据，代码如下

```python
import pandas as pd

df = pd.read_csv('c:\\pwork\\全球指数删减.csv')
df.head()
```

<img src="https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/image-20210224193838751.png" alt="image-20210224193838751" style="zoom:50%;" />

- `pd.DataFrame` 转为 R 的 `data.frame`

在使用 R 包之前，需要先把数据转化为 R 的格式，才能在 rpy2 中使用该数据。代码如下

```python
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
import rpy2.robjects as robjects

with localconverter(ro.default_converter + pandas2ri.converter):
    r_df = ro.conversion.py2rpy(df)

r_df

# out: 
# R/rpy2 DataFrame (5356 x 7)
# date	000001.SH	FTSE.GI	N225.GI	SPX.GI	HSI.HI	KS11.GI
# ...	...	...	...	...	...	...
```

通过以上代码，我们就构建了 `r_df` 的 R 数据了，但是要使用该数据，还需要下面的一步。

```python
import rpy2.robjects as robjects

robjects.globalenv['r_df'] = r_df
```

至此，R 环境中就可以使用  `r_df` 了。接下来就可以运用该数据来拟合 arima-garch 模型。



## 3. 在 R 中拟合 Arima-Garch 模型

首先，在这里先要简单说一下，模型在 r 中实现的语句是什么样的

```R
library(fGarch)
df <- read.csv("c:\\pwork\\全球指数删减.csv", encoding="UTF-8")
fit <-garchFit(formula = ~arma(1, 1) + garch(1, 1), df$FTSE.GI, trace = F)
summary(fit)
```



那么如何在 python 的环境中实现呢？在这里先要简单说一句，在 python 中运行 R 代码的方法

```python
robjects.r("""
	c <- 1 + 2
""")
```

其实很简单，就是用 `robjects.r` 来实现。

那么接下来就是本番です。

```python
fit = robjects.r("""
    fit <-garchFit(formula = ~arma(0, 0) + garch(1, 1), r_df$FTSE.GI, include.mean = F, trace = F)
    summary(fit)
""")
```

```
Title:
 GARCH Modelling 

Call:
 garchFit(formula = ~arma(0, 0) + garch(1, 1), data = r_df$FTSE.GI, 
    include.mean = F, trace = F) 

Mean and Variance Equation:
 data ~ arma(0, 0) + garch(1, 1)
<environment: 0x00000247be52ecd0>
 [data = r_df$FTSE.GI]

Conditional Distribution:
 norm 

Coefficient(s):
   omega    alpha1     beta1  
0.015793  0.097171  0.890560  

Std. Errors:
 based on Hessian 

Error Analysis:
        Estimate  Std. Error  t value Pr(>|t|)    
omega   0.015793    0.003071    5.143  2.7e-07 ***
alpha1  0.097171    0.008782   11.065  < 2e-16 ***
beta1   0.890560    0.009698   91.830  < 2e-16 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Log Likelihood:
 -7265.23    normalized:  -1.356466 

Description:
 Wed Feb 24 19:54:12 2021 by user: 13631 


Standardised Residuals Tests:
                                Statistic p-Value   
 Jarque-Bera Test   R    Chi^2  199.5589  0         
 Shapiro-Wilk Test  R    W      NA        NA        
 Ljung-Box Test     R    Q(10)  13.584    0.1928261 
 Ljung-Box Test     R    Q(15)  14.11814  0.516589  
 Ljung-Box Test     R    Q(20)  15.72543  0.7335052 
 Ljung-Box Test     R^2  Q(10)  16.08341  0.09726945
 Ljung-Box Test     R^2  Q(15)  18.80962  0.2224909 
 Ljung-Box Test     R^2  Q(20)  23.63945  0.2584967 
 LM Arch Test       R    TR^2   16.96844  0.1507882 

Information Criterion Statistics:
     AIC      BIC      SIC     HQIC 
2.714051 2.717740 2.714051 2.715340 
```

撒花，这样就成功地使用 python 来运行 R 包啦。



## 番外. 如何使用 R 的结果

能在 python 使用 R 语言已经实现，接下来的一个小问题就是联动问题，我需要把R的结果拿回 python 来用该怎么办呢？这时候需要另外一条语句了：**R 的 data.frame 转化为 pd.DataFrame**。

语句如下

```python
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter

# r_df = ro.DataFrame({'int_values': ro.IntVector([1,2,3]),
#                      'str_values': ro.StrVector(['abc', 'def', 'ghi'])})
# r_df

with localconverter(ro.default_converter + pandas2ri.converter):
  pd_from_r_df = ro.conversion.rpy2py(r_df)

pd_from_r_df
```

以上是官方文档中给出的示例，那我们也来看看在我的例子中如何运用吧。那么，我在这里尝试提取 arima-garch 模型的残差和向后预测值，实现步骤如下代码

```python
res_py = robjects.r("""
    res_fit <- residuals(fit)
""")

res_py

# FloatVector with 5356 elements.
# -0.913400	0.264000	0.391900	...	2.482100	1.383700	0.017700
```

转为 `numpy.array` 方法如下：

```python
with localconverter(ro.default_converter + pandas2ri.converter):
    pd_from_res_py = ro.conversion.rpy2py(res_py)

pd_from_res_py

# array([-0.9134,  0.264 ,  0.3919, ...,  2.4821,  1.3837,  0.0177])
```

```python
type(pd_from_r_df)
# numpy.ndarray
```

- 预测值的转化

```python
pre_py = robjects.r("""
    pre_fit <- predict(fit)
""")
```

```python
with localconverter(ro.default_converter + pandas2ri.converter):
    pd_from_pre_py = ro.conversion.rpy2py(pre_py)

pd_from_pre_py
```

|      | meanForecast | meanError | standardDeviation |
| ---: | -----------: | --------: | ----------------: |
|    1 |          0.0 |  1.499357 |          1.499357 |
|    2 |          0.0 |  1.495420 |          1.495420 |
|    3 |          0.0 |  1.491522 |          1.491522 |
|    4 |          0.0 |  1.487661 |          1.487661 |
|    5 |          0.0 |  1.483838 |          1.483838 |
|    6 |          0.0 |  1.480052 |          1.480052 |
|    7 |          0.0 |  1.476303 |          1.476303 |
|    8 |          0.0 |  1.472591 |          1.472591 |
|    9 |          0.0 |  1.468915 |          1.468915 |
|   10 |          0.0 |  1.465275 |          1.465275 |

```python
type(pd_from_r_df)

# pandas.core.frame.DataFrame
```

