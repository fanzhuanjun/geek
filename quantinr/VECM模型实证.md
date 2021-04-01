```R
dat <- read.csv("C:/kenkyu/经济与金融计量方法/物价水平与房地产价格数据.csv")
```


```R
library(urca)
```


```R
head(dat)
```


<table class="dataframe">
<caption>A data.frame: 6 × 7</caption>
<thead>
	<tr><th></th><th scope=col>锘縟ate</th><th scope=col>CPI</th><th scope=col>ASPH</th><th scope=col>lnCPI</th><th scope=col>lnASPH</th><th scope=col>difflnCPI</th><th scope=col>difflnASPH</th></tr>
	<tr><th></th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>2000/2/1</td><td>101.90000</td><td>2269.93</td><td>4.623992</td><td>7.727504</td><td> 0.018821754</td><td> 0.000000000</td></tr>
	<tr><th scope=row>2</th><td>2000/3/1</td><td>100.26960</td><td>2126.83</td><td>4.607863</td><td>7.662388</td><td>-0.016129382</td><td>-0.065116386</td></tr>
	<tr><th scope=row>3</th><td>2000/4/1</td><td> 99.36717</td><td>2090.67</td><td>4.598822</td><td>7.645240</td><td>-0.009040745</td><td>-0.017148019</td></tr>
	<tr><th scope=row>4</th><td>2000/5/1</td><td> 98.37350</td><td>2108.28</td><td>4.588771</td><td>7.653628</td><td>-0.010050336</td><td> 0.008387860</td></tr>
	<tr><th scope=row>5</th><td>2000/6/1</td><td> 96.89790</td><td>2074.36</td><td>4.573658</td><td>7.637408</td><td>-0.015113638</td><td>-0.016219777</td></tr>
	<tr><th scope=row>6</th><td>2000/7/1</td><td> 96.12272</td><td>2059.01</td><td>4.565626</td><td>7.629981</td><td>-0.008032172</td><td>-0.007427388</td></tr>
</tbody>
</table>



# 单位根检验


```R
library(tseries)
for ( i in seq(from=2, to=7, by=1)) {
  print(i)
  print(adf.test(df[,i]))
}
```

    [1] 2
    
    	Augmented Dickey-Fuller Test
    
    data:  df[, i]
    Dickey-Fuller = -2.3343, Lag order = 5, p-value = 0.4357
    alternative hypothesis: stationary
    
    [1] 3
    
    	Augmented Dickey-Fuller Test
    
    data:  df[, i]
    Dickey-Fuller = -3.3074, Lag order = 5, p-value = 0.07118
    alternative hypothesis: stationary
    
    [1] 4
    
    	Augmented Dickey-Fuller Test
    
    data:  df[, i]
    Dickey-Fuller = -2.0145, Lag order = 5, p-value = 0.5699
    alternative hypothesis: stationary
    
    [1] 5
    
    	Augmented Dickey-Fuller Test
    
    data:  df[, i]
    Dickey-Fuller = -2.579, Lag order = 5, p-value = 0.3331
    alternative hypothesis: stationary
    
    [1] 6
    

    Warning message in adf.test(df[, i]):
    "p-value smaller than printed p-value"
    

    
    	Augmented Dickey-Fuller Test
    
    data:  df[, i]
    Dickey-Fuller = -7.2901, Lag order = 5, p-value = 0.01
    alternative hypothesis: stationary
    
    [1] 7
    

    Warning message in adf.test(df[, i]):
    "p-value smaller than printed p-value"
    

    
    	Augmented Dickey-Fuller Test
    
    data:  df[, i]
    Dickey-Fuller = -8.1121, Lag order = 5, p-value = 0.01
    alternative hypothesis: stationary
    
    


```R
# y.df = ur.df(dat[,6], type=c("trend"), selectlags='AIC')
# summary(y.df)
```


```R
dat_ln = dat[, 4:5]
dat_d = dat[, 6:7]
```

# 协整检验

## 确定最优VAR 滞后


```R
lags <- vars::VARselect(dat_d, lag.max=25)$selection
lags
```


<style>
.dl-inline {width: auto; margin:0; padding: 0}
.dl-inline>dt, .dl-inline>dd {float: none; width: auto; display: inline-block}
.dl-inline>dt::after {content: ":\0020"; padding-right: .5ex}
.dl-inline>dt:not(:first-of-type) {padding-left: .5ex}
</style><dl class=dl-inline><dt>AIC(n)</dt><dd>24</dd><dt>HQ(n)</dt><dd>12</dd><dt>SC(n)</dt><dd>12</dd><dt>FPE(n)</dt><dd>13</dd></dl>




```R
cointest_eigen = ca.jo(dat_ln, K=lags[3]-1, type="eigen", ecdet="const", spec="transitory")
summary(cointest_eigen)
```


    
    ###################### 
    # Johansen-Procedure # 
    ###################### 
    
    Test type: maximal eigenvalue statistic (lambda max) , without linear trend and constant in cointegration 
    
    Eigenvalues (lambda):
    [1]  2.806306e-01  7.055445e-02 -3.938329e-17
    
    Values of teststatistic and critical values of test:
    
              test 10pct  5pct  1pct
    r <= 1 | 15.07  7.52  9.24 12.97
    r = 0  | 67.85 13.75 15.67 20.20
    
    Eigenvectors, normalised to first column:
    (These are the cointegration relations)
    
                lnCPI.l1  lnASPH.l1   constant
    lnCPI.l1   1.0000000  1.0000000  1.0000000
    lnASPH.l1 -0.3490439 -0.3579479 -0.1283196
    constant  -1.9515741 -1.8101040 -3.7269390
    
    Weights W:
    (This is the loading matrix)
    
                lnCPI.l1   lnASPH.l1      constant
    lnCPI.d  -0.06452267 -0.03817509 -4.457900e-14
    lnASPH.d -0.42090623  0.32852664 -3.175929e-14
    



```R
cointest_trace = ca.jo(dat_ln, K=lags[3]-1, type="trace", ecdet="const", spec="transitory")
summary(cointest_trace)
```


    
    ###################### 
    # Johansen-Procedure # 
    ###################### 
    
    Test type: trace statistic , without linear trend and constant in cointegration 
    
    Eigenvalues (lambda):
    [1]  2.806306e-01  7.055445e-02 -3.938329e-17
    
    Values of teststatistic and critical values of test:
    
              test 10pct  5pct  1pct
    r <= 1 | 15.07  7.52  9.24 12.97
    r = 0  | 82.92 17.85 19.96 24.60
    
    Eigenvectors, normalised to first column:
    (These are the cointegration relations)
    
                lnCPI.l1  lnASPH.l1   constant
    lnCPI.l1   1.0000000  1.0000000  1.0000000
    lnASPH.l1 -0.3490439 -0.3579479 -0.1283196
    constant  -1.9515741 -1.8101040 -3.7269390
    
    Weights W:
    (This is the loading matrix)
    
                lnCPI.l1   lnASPH.l1      constant
    lnCPI.d  -0.06452267 -0.03817509 -4.457900e-14
    lnASPH.d -0.42090623  0.32852664 -3.175929e-14
    


使用 cajorls 来估计系数矩阵


```R
cajorls(cointest_eigen)$rlm
```


    
    Call:
    lm(formula = substitute(form1), data = data.mat)
    
    Coefficients:
                 lnCPI.d    lnASPH.d 
    ect1         -0.064523  -0.420906
    lnCPI.dl1     0.198054   0.765529
    lnASPH.dl1   -0.001993  -0.408952
    lnCPI.dl2     0.064375   0.380941
    lnASPH.dl2   -0.076850  -0.565920
    lnCPI.dl3    -0.059065  -1.020150
    lnASPH.dl3   -0.033611  -0.318790
    lnCPI.dl4     0.108670   1.361429
    lnASPH.dl4   -0.067028  -0.338285
    lnCPI.dl5     0.040270   0.233441
    lnASPH.dl5   -0.055151  -0.436296
    lnCPI.dl6    -0.049294   0.320827
    lnASPH.dl6   -0.023002  -0.162796
    lnCPI.dl7    -0.084384  -0.782936
    lnASPH.dl7   -0.018513  -0.271093
    lnCPI.dl8     0.048223  -1.578847
    lnASPH.dl8   -0.005700  -0.122878
    lnCPI.dl9    -0.063184   0.754415
    lnASPH.dl9   -0.027260  -0.113640
    lnCPI.dl10   -0.155141  -2.258249
    lnASPH.dl10  -0.015100  -0.283385
    



```R
cajorls(cointest_eigen)$beta
```


<table class="dataframe">
<caption>A matrix: 3 × 1 of type dbl</caption>
<thead>
	<tr><th></th><th scope=col>ect1</th></tr>
</thead>
<tbody>
	<tr><th scope=row>lnCPI.l1</th><td> 1.0000000</td></tr>
	<tr><th scope=row>lnASPH.l1</th><td>-0.3490439</td></tr>
	<tr><th scope=row>constant</th><td>-1.9515741</td></tr>
</tbody>
</table>



估计的误差修正模型为：


$$

\left[ \begin{matrix}\Delta Y_{1,t} \\ \Delta Y_{2,t} \\\end{matrix} \right] = 

\left[ \begin{matrix} 0.198054 & -0.001993   \\ 0.765529& -0.408952  \\ \end{matrix} \right]
\left[ \begin{matrix}\Delta Y_{1,t-1} \\ \Delta Y_{2,t-1} \\\end{matrix} \right]
+ ... + 

\left[ \begin{matrix}-0.064523 \\ -0.420906 \\\end{matrix} \right]
\left[ \begin{matrix}1 & -0.3490439
 \\\end{matrix} \right]
\left[ \begin{matrix}  Y_{1,t-1} \\  Y_{2,t-1} \\\end{matrix} \right]
$$

协整方程式如下：


$$
lnCPI - 0.3490439 \times lnASPH -1.9515741 = 0
$$


```R
cajorls(cointest_trace)$beta
```


<table class="dataframe">
<caption>A matrix: 3 × 1 of type dbl</caption>
<thead>
	<tr><th></th><th scope=col>ect1</th></tr>
</thead>
<tbody>
	<tr><th scope=row>lnCPI.l1</th><td> 1.0000000</td></tr>
	<tr><th scope=row>lnASPH.l1</th><td>-0.3490439</td></tr>
	<tr><th scope=row>constant</th><td>-1.9515741</td></tr>
</tbody>
</table>




```R
library(xts)
```

    Loading required package: zoo
    
    
    Attaching package: 'zoo'
    
    
    The following objects are masked from 'package:base':
    
        as.Date, as.Date.numeric
    
    
    


```R
BETA = cajorls(cointest_eigen)$beta
EC0 = as.matrix(dat_ln)%*%BETA[1:2]+BETA[3]
plot(EC0, main='Cointegrating relation', type='l')
```


![png](VECM%E6%A8%A1%E5%9E%8B%E5%AE%9E%E8%AF%81_files/VECM%E6%A8%A1%E5%9E%8B%E5%AE%9E%E8%AF%81_20_0.png)



```R
adf.test(EC0)
```


    
    	Augmented Dickey-Fuller Test
    
    data:  EC0
    Dickey-Fuller = -2.8445, Lag order = 5, p-value = 0.2217
    alternative hypothesis: stationary
    


# 格兰杰因果检验


```R
library(vars)
out.var = VAR(dat_d, p=13, type='const', season=NULL, exogen=NULL,
             lag.max=NULL)
```


```R
causality(out.var, cause="difflnASPH", boot=TRUE, boot.runs=5000)
```


    $Granger
    
    	Granger causality H0: difflnASPH do not Granger-cause difflnCPI
    
    data:  VAR object out.var
    F-Test = 4.8938, boot.runs = 5000, p-value = 8e-04
    
    
    $Instant
    
    	H0: No instantaneous causality between: difflnASPH and difflnCPI
    
    data:  VAR object out.var
    Chi-squared = 1.5406, df = 1, p-value = 0.2145
    
    



```R
causality(out.var, cause="difflnCPI", boot=TRUE, boot.runs=5000)
```


    $Granger
    
    	Granger causality H0: difflnCPI do not Granger-cause difflnASPH
    
    data:  VAR object out.var
    F-Test = 1.3019, boot.runs = 5000, p-value = 0.1314
    
    
    $Instant
    
    	H0: No instantaneous causality between: difflnCPI and difflnASPH
    
    data:  VAR object out.var
    Chi-squared = 1.5406, df = 1, p-value = 0.2145
    
    


房屋价格是引起CPI波动的原因，CPI不是房屋价格波动的原因。


```R
irf.out <-irf(out.var, boot=TRUE, boot.runs=1000)
```


```R
plot(irf.out)
```


![png](VECM%E6%A8%A1%E5%9E%8B%E5%AE%9E%E8%AF%81_files/VECM%E6%A8%A1%E5%9E%8B%E5%AE%9E%E8%AF%81_28_0.png)



![png](VECM%E6%A8%A1%E5%9E%8B%E5%AE%9E%E8%AF%81_files/VECM%E6%A8%A1%E5%9E%8B%E5%AE%9E%E8%AF%81_28_1.png)


# 附录 多阶之后的格兰杰因果检验


```R
library(lmtest)
```


```R
grangertest(y=dat_d[,1], x=dat_d[,2], order = 1)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>213</td><td>NA</td><td>      NA</td><td>         NA</td></tr>
	<tr><th scope=row>2</th><td>214</td><td>-1</td><td>10.49146</td><td>0.001391261</td></tr>
</tbody>
</table>




```R
grangertest(y=dat_d[,1], x=dat_d[,2], order = 2)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>210</td><td>NA</td><td>      NA</td><td>          NA</td></tr>
	<tr><th scope=row>2</th><td>212</td><td>-2</td><td>14.11861</td><td>1.766106e-06</td></tr>
</tbody>
</table>




```R
grangertest(y=dat_d[,1], x=dat_d[,2], order = 3)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>207</td><td>NA</td><td>      NA</td><td>          NA</td></tr>
	<tr><th scope=row>2</th><td>210</td><td>-3</td><td>10.76242</td><td>1.330651e-06</td></tr>
</tbody>
</table>




```R
grangertest(y=dat_d[,1], x=dat_d[,2], order = 4)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>204</td><td>NA</td><td>      NA</td><td>          NA</td></tr>
	<tr><th scope=row>2</th><td>208</td><td>-4</td><td>11.35763</td><td>2.427647e-08</td></tr>
</tbody>
</table>




```R
grangertest(y=dat_d[,1], x=dat_d[,2], order = 5)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>201</td><td>NA</td><td>     NA</td><td>          NA</td></tr>
	<tr><th scope=row>2</th><td>206</td><td>-5</td><td>12.5844</td><td>1.221489e-10</td></tr>
</tbody>
</table>




```R
grangertest(y=dat_d[,1], x=dat_d[,2], order = 6)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>198</td><td>NA</td><td>      NA</td><td>          NA</td></tr>
	<tr><th scope=row>2</th><td>204</td><td>-6</td><td>10.68365</td><td>2.806784e-10</td></tr>
</tbody>
</table>




```R
grangertest(x=dat_d[,1], y=dat_d[,2], order = 1)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>213</td><td>NA</td><td>       NA</td><td>       NA</td></tr>
	<tr><th scope=row>2</th><td>214</td><td>-1</td><td>0.7570435</td><td>0.3852348</td></tr>
</tbody>
</table>




```R
grangertest(x=dat_d[,1], y=dat_d[,2], order = 2)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>210</td><td>NA</td><td>      NA</td><td>        NA</td></tr>
	<tr><th scope=row>2</th><td>212</td><td>-2</td><td>4.489625</td><td>0.01232295</td></tr>
</tbody>
</table>




```R
grangertest(x=dat_d[,1], y=dat_d[,2], order = 3)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>207</td><td>NA</td><td>      NA</td><td>        NA</td></tr>
	<tr><th scope=row>2</th><td>210</td><td>-3</td><td>3.650277</td><td>0.01348483</td></tr>
</tbody>
</table>




```R
grangertest(x=dat_d[,1], y=dat_d[,2], order = 4)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>204</td><td>NA</td><td>      NA</td><td>         NA</td></tr>
	<tr><th scope=row>2</th><td>208</td><td>-4</td><td>4.406739</td><td>0.001942727</td></tr>
</tbody>
</table>




```R
grangertest(x=dat_d[,1], y=dat_d[,2], order = 5)
```


<table class="dataframe">
<caption>A anova: 2 × 4</caption>
<thead>
	<tr><th></th><th scope=col>Res.Df</th><th scope=col>Df</th><th scope=col>F</th><th scope=col>Pr(&gt;F)</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>201</td><td>NA</td><td>      NA</td><td>          NA</td></tr>
	<tr><th scope=row>2</th><td>206</td><td>-5</td><td>4.851041</td><td>0.0003275336</td></tr>
</tbody>
</table>




```R

```
