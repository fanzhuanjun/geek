# Ch9.单变量GARCH模型

本书代码取自《经济与金融计量方法》何宗武


```R
load("data/index_stock.RData")
y = index_stock[,6] # 中国指数报酬率
```

    Loading required package: timeSeries
    
    Loading required package: timeDate
    
    


```R
fit.ar1 = arima(y, order=c(1, 0, 0))
```


```R
fit.ar1
```


    
    Call:
    arima(x = y, order = c(1, 0, 0))
    
    Coefficients:
             ar1  intercept
          0.0202     0.0289
    s.e.  0.0314     0.0341
    
    sigma^2 estimated as 1.135:  log likelihood = -1507.54,  aic = 3021.08



```R
library(MTS) # 载入MTS，该包内有检验ARCH效应的函数
archTest(fit.ar1$resid)
```

    Q(m) of squared series(LM test):  
    Test statistic:  682.1235  p-value:  0 
    Rank-based Test:  
    Test statistic:  219.8319  p-value:  0 
    


```R
detach(package:MTS) # 从内存中卸载MTS包
```

### 9.2.2 运用 tseries 包估计标准 GARCH


```R
library(tseries)
out = garch(y, order=c(2,1))
# 非常注意：order=c(q, p), p=ARCH order, q=GARCH order
summary(out)
```

    Registered S3 method overwritten by 'quantmod':
      method            from
      as.zoo.data.frame zoo 
    
    

    
     ***** ESTIMATION WITH ANALYTICAL GRADIENT ***** 
    
    
         I     INITIAL X(I)        D(I)
    
         1     9.662593e-01     1.000e+00
         2     5.000000e-02     1.000e+00
         3     5.000000e-02     1.000e+00
         4     5.000000e-02     1.000e+00
    
        IT   NF      F         RELDF    PRELDF    RELDX   STPPAR   D*STEP   NPRELDF
         0    1  5.443e+02
         1    3  5.334e+02  2.00e-02  2.72e-01  2.5e-01  6.7e+02  4.7e-01  9.11e+01
         2    5  5.297e+02  7.05e-03  7.63e-03  1.1e-02  2.0e+01  2.4e-02  2.08e+01
         3    7  5.125e+02  3.24e-02  3.84e-02  1.1e-01  2.8e+00  1.9e-01  5.09e+01
         4    9  4.576e+02  1.07e-01  1.15e-01  2.8e-01  2.0e+00  3.8e-01  3.53e+01
         5   11  4.504e+02  1.58e-02  2.28e-02  4.4e-02  1.3e+01  5.7e-02  3.68e+01
         6   13  4.408e+02  2.13e-02  2.38e-02  1.7e-01  2.0e+00  1.1e-01  5.57e+01
         7   14  4.029e+02  8.61e-02  9.02e-02  2.4e-01  2.0e+00  2.3e-01  4.63e+01
         8   16  4.004e+02  6.15e-03  6.34e-03  1.9e-02  4.1e+01  2.3e-02  7.70e+00
         9   18  3.962e+02  1.05e-02  1.11e-02  3.7e-02  2.9e+00  4.6e-02  8.36e+00
        10   20  3.949e+02  3.13e-03  3.94e-03  1.9e-02  7.8e+01  1.8e-02  9.73e-01
        11   21  3.936e+02  3.42e-03  3.94e-03  1.7e-02  2.0e+00  1.8e-02  1.35e+01
        12   23  3.881e+02  1.39e-02  1.77e-02  9.3e-02  2.0e+00  8.8e-02  1.05e+01
        13   24  3.864e+02  4.47e-03  1.87e-02  7.9e-02  2.0e+00  8.8e-02  1.08e+00
        14   26  3.849e+02  3.94e-03  1.20e-02  1.9e-02  2.0e+00  2.2e-02  2.02e-01
        15   27  3.835e+02  3.60e-03  6.08e-03  1.8e-02  1.9e+00  2.2e-02  1.89e-02
        16   29  3.831e+02  9.35e-04  1.85e-03  6.3e-02  1.8e+00  6.9e-02  2.74e-02
        17   32  3.831e+02  1.47e-04  6.27e-04  1.5e-03  4.7e+00  1.8e-03  3.98e-03
        18   33  3.830e+02  9.10e-05  9.36e-05  1.7e-03  2.0e+00  1.8e-03  1.20e-03
        19   34  3.830e+02  1.27e-05  1.80e-05  3.4e-03  2.0e+00  3.6e-03  1.08e-03
        20   35  3.830e+02  2.29e-05  2.77e-05  6.5e-03  2.0e+00  7.3e-03  9.04e-04
        21   40  3.821e+02  2.32e-03  7.49e-04  2.9e-01  0.0e+00  4.7e-01  8.54e-04
        22   42  3.818e+02  8.00e-04  7.64e-04  4.3e-02  2.0e+00  9.3e-02  1.67e-01
        23   44  3.817e+02  1.67e-04  1.66e-04  8.2e-03  2.0e+00  1.9e-02  1.15e+01
        24   46  3.816e+02  3.37e-04  3.35e-04  1.6e-02  2.0e+00  3.7e-02  6.81e+02
        25   49  3.816e+02  6.79e-06  6.78e-06  3.2e-04  2.0e+00  7.5e-04  6.53e+04
        26   51  3.816e+02  1.37e-05  1.36e-05  6.3e-04  2.0e+00  1.5e-03  1.04e+05
        27   53  3.816e+02  3.61e-06  3.16e-06  1.3e-04  2.0e+00  3.0e-04  1.41e+05
        28   54  3.816e+02  6.83e-06  1.19e-05  2.6e-04  7.4e+00  6.0e-04  1.41e+05
        29   56  3.816e+02  6.06e-06  6.12e-06  2.5e-04  2.0e+00  6.0e-04  1.43e+05
        30   59  3.816e+02  2.29e-07  2.32e-07  6.3e-06  6.8e+00  1.2e-05  1.43e+05
        31   61  3.816e+02  4.20e-08  4.22e-08  1.3e-06  3.9e+01  2.4e-06  1.43e+05
        32   63  3.816e+02  8.27e-09  8.31e-09  2.7e-07  2.1e+02  4.8e-07  1.43e+05
        33   65  3.816e+02  1.65e-09  1.66e-09  5.3e-08  1.1e+03  9.6e-08  1.43e+05
        34   67  3.816e+02  3.30e-09  3.31e-09  1.1e-07  1.3e+02  1.9e-07  1.43e+05
        35   69  3.816e+02  6.59e-10  6.61e-10  2.1e-08  2.7e+03  3.8e-08  1.43e+05
        36   71  3.816e+02  1.32e-09  1.32e-09  4.3e-08  3.3e+02  7.6e-08  1.43e+05
        37   73  3.816e+02  2.63e-10  2.64e-10  8.5e-09  6.7e+03  1.5e-08  1.43e+05
        38   75  3.816e+02  5.26e-10  5.28e-10  1.7e-08  8.4e+02  3.1e-08  1.43e+05
        39   77  3.816e+02  1.05e-10  1.06e-10  3.4e-09  1.7e+04  6.1e-09  1.43e+05
        40   79  3.816e+02  2.10e-11  2.11e-11  6.8e-10  2.0e+00  1.2e-09 -9.14e-03
        41   81  3.816e+02  4.21e-11  4.22e-11  1.4e-09  2.0e+00  2.4e-09 -9.14e-03
        42   83  3.816e+02  8.42e-12  8.45e-12  2.7e-10  2.0e+00  4.9e-10 -9.14e-03
        43   85  3.816e+02  1.68e-11  1.69e-11  5.5e-10  2.0e+00  9.8e-10 -9.14e-03
        44   87  3.816e+02  3.37e-11  3.38e-11  1.1e-09  2.0e+00  2.0e-09 -9.14e-03
        45   90  3.816e+02  6.75e-13  6.76e-13  2.2e-11  2.0e+00  3.9e-11 -9.14e-03
        46   92  3.816e+02  1.35e-12  1.35e-12  4.4e-11  2.0e+00  7.8e-11 -9.14e-03
        47   94  3.816e+02  2.71e-13  2.70e-13  8.8e-12  2.0e+00  1.6e-11 -9.14e-03
        48   96  3.816e+02  5.39e-13  5.41e-13  1.8e-11  2.0e+00  3.1e-11 -9.14e-03
        49   98  3.816e+02  1.07e-12  1.08e-12  3.5e-11  2.0e+00  6.3e-11 -9.14e-03
        50  100  3.816e+02  2.16e-13  2.16e-13  7.0e-12  2.0e+00  1.3e-11 -9.14e-03
        51  102  3.816e+02  4.53e-14  4.32e-14  1.4e-12  2.0e+00  2.5e-12 -9.14e-03
        52  104  3.816e+02  8.04e-15  8.65e-15  2.8e-13  2.0e+00  5.0e-13 -9.14e-03
        53  106  3.816e+02  1.70e-14  1.73e-14  5.6e-13  2.0e+00  1.0e-12 -9.14e-03
        54  108  3.816e+02  3.22e-14  3.46e-14  1.1e-12  2.0e+00  2.0e-12 -9.14e-03
        55  110  3.816e+02  8.79e-15  6.92e-15  2.2e-13  2.0e+00  4.0e-13 -9.14e-03
        56  113  3.816e+02  2.98e-16  6.92e-16  2.2e-14  2.0e+00  4.0e-14 -9.14e-03
        57  114  3.816e+02  4.47e-16  1.38e-15  4.5e-14  2.0e+00  8.0e-14 -9.14e-03
        58  116  3.816e+02  4.17e-15  2.77e-15  9.0e-14  2.0e+00  1.6e-13 -9.14e-03
        59  118  3.816e+02 -1.49e-16  5.54e-16  1.8e-14  2.0e+00  3.2e-14 -9.14e-03
    
     ***** FALSE CONVERGENCE *****
    
     FUNCTION     3.816044e+02   RELDX        1.792e-14
     FUNC. EVALS     118         GRAD. EVALS      59
     PRELDF       5.536e-16      NPRELDF     -9.143e-03
    
         I      FINAL X(I)        D(I)          G(I)
    
         1    1.270959e-02     1.000e+00     5.752e-01
         2    1.149315e-01     1.000e+00    -4.804e-01
         3    8.761163e-01     1.000e+00     1.114e+00
         4    2.357758e-13     1.000e+00     6.446e+00
    
    


    
    Call:
    garch(x = y, order = c(2, 1))
    
    Model:
    GARCH(2,1)
    
    Residuals:
         Min       1Q   Median       3Q      Max 
    -3.41764 -0.51956  0.02855  0.63875  3.86647 
    
    Coefficient(s):
        Estimate  Std. Error  t value Pr(>|t|)    
    a0 1.271e-02   5.281e-03    2.407 0.016100 *  
    a1 1.149e-01   3.293e-02    3.490 0.000484 ***
    b1 8.761e-01   2.891e-01    3.031 0.002441 ** 
    b2 2.358e-13   2.579e-01    0.000 1.000000    
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    Diagnostic Tests:
    	Jarque Bera Test
    
    data:  Residuals
    X-squared = 39.931, df = 2, p-value = 2.134e-09
    
    
    	Box-Ljung test
    
    data:  Squared.Residuals
    X-squared = 0.79815, df = 1, p-value = 0.3716
    



```R
names(out)
```


<style>
.list-inline {list-style: none; margin:0; padding: 0}
.list-inline>li {display: inline-block}
.list-inline>li:not(:last-child)::after {content: "\00b7"; padding: 0 .5ex}
</style>
<ol class=list-inline><li>'order'</li><li>'coef'</li><li>'n.likeli'</li><li>'n.used'</li><li>'residuals'</li><li>'fitted.values'</li><li>'series'</li><li>'frequency'</li><li>'call'</li><li>'vcov'</li></ol>




```R
tail(out$fitted, 10)
```


<table class="dataframe">
<caption>A matrix: 10 × 2 of type dbl</caption>
<thead>
	<tr><th></th><th scope=col>sigt</th><th scope=col>-sigt</th></tr>
</thead>
<tbody>
	<tr><th scope=row>[1008,]</th><td>0.5870628</td><td>-0.5870628</td></tr>
	<tr><th scope=row>[1009,]</th><td>0.5763043</td><td>-0.5763043</td></tr>
	<tr><th scope=row>[1010,]</th><td>0.5605981</td><td>-0.5605981</td></tr>
	<tr><th scope=row>[1011,]</th><td>0.5369335</td><td>-0.5369335</td></tr>
	<tr><th scope=row>[1012,]</th><td>0.5150978</td><td>-0.5150978</td></tr>
	<tr><th scope=row>[1013,]</th><td>0.5575046</td><td>-0.5575046</td></tr>
	<tr><th scope=row>[1014,]</th><td>0.6455729</td><td>-0.6455729</td></tr>
	<tr><th scope=row>[1015,]</th><td>0.6524007</td><td>-0.6524007</td></tr>
	<tr><th scope=row>[1016,]</th><td>0.6224508</td><td>-0.6224508</td></tr>
	<tr><th scope=row>[1017,]</th><td>0.5957518</td><td>-0.5957518</td></tr>
</tbody>
</table>




```R
plot(out, which="all")
```


![png](Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_files/Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_11_0.png)



![png](Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_files/Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_11_1.png)



![png](Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_files/Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_11_2.png)



![png](Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_files/Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_11_3.png)


### 9.2.3 运用 fGarch 包估计标准GARCH

范例程序9 fGarch包中的标准GARCH(2,1)模型的估计


```R
library(fGarch)
```

    Loading required package: fBasics
    
    


```R
distriduction=c("std") #  选择残差的概率分布，此处 std 为 student t 分布
fit <- garchFit(~ garch(2, 1), data=y, cond.dist=distriduction)
# 将结果存入对象 fit。garch(p, q), p =ARCH order, q=GARCH order
summary(fit)
```

    
    Series Initialization:
     ARMA Model:                arma
     Formula Mean:              ~ arma(0, 0)
     GARCH Model:               garch
     Formula Variance:          ~ garch(2, 1)
     ARMA Order:                0 0
     Max ARMA Order:            0
     GARCH Order:               2 1
     Max GARCH Order:           2
     Maximum Order:             2
     Conditional Dist:          std
     h.start:                   3
     llh.start:                 1
     Length of Series:          1017
     Recursion Init:            mci
     Series Scale:              1.066197
    
    Parameter Initialization:
     Initial Parameters:          $params
     Limits of Transformations:   $U, $V
     Which Parameters are Fixed?  $includes
     Parameter Matrix:
                         U           V     params includes
        mu     -0.27115476   0.2711548 0.02711548     TRUE
        omega   0.00000100 100.0000000 0.10000000     TRUE
        alpha1  0.00000001   1.0000000 0.05000000     TRUE
        alpha2  0.00000001   1.0000000 0.05000000     TRUE
        gamma1 -0.99999999   1.0000000 0.10000000    FALSE
        gamma2 -0.99999999   1.0000000 0.10000000    FALSE
        beta1   0.00000001   1.0000000 0.80000000     TRUE
        delta   0.00000000   2.0000000 2.00000000    FALSE
        skew    0.10000000  10.0000000 1.00000000    FALSE
        shape   1.00000000  10.0000000 4.00000000     TRUE
     Index List of Parameters to be Optimized:
        mu  omega alpha1 alpha2  beta1  shape 
         1      2      3      4      7     10 
     Persistence:                  0.9 
    
    
    --- START OF TRACE ---
    Selected Algorithm: nlminb 
    
    R coded nlminb Solver: 
    
      0:     1267.8149: 0.0271155 0.100000 0.0500000 0.0500000 0.800000  4.00000
      1:     1245.4979: 0.0271346 0.0134400 0.118449 0.130654 0.793652  4.00100
      2:     1245.2561: 0.0271388 0.0299420 0.120744 0.133771 0.801799  4.00133
      3:     1243.4386: 0.0271463 0.0245954 0.115338 0.129633 0.798135  4.00149
      4:     1243.0928: 0.0271641 0.0205775 0.109181 0.126641 0.803074  4.00227
      5:     1242.4207: 0.0272067 0.0237640 0.0956907 0.120001 0.813650  4.00408
      6:     1241.7712: 0.0272533 0.0149939 0.0894868 0.120356 0.828811  4.00642
      7:     1241.7345: 0.0272569 0.0171520 0.0888612 0.120134 0.830450  4.00660
      8:     1241.6055: 0.0272663 0.0157442 0.0871779 0.118602 0.831018  4.00709
      9:     1241.4607: 0.0272875 0.0167891 0.0844824 0.116493 0.835098  4.00822
     10:     1240.6335: 0.0275601 0.00550605 0.0674119 0.0956335 0.872162  4.02342
     11:     1240.4486: 0.0277067 0.0128028 0.0584813 0.0845465 0.879571  4.03177
     12:     1240.2004: 0.0277624 0.00948649 0.0549998 0.0802533 0.879817  4.03503
     13:     1239.9138: 0.0278469 0.0100441 0.0583055 0.0844247 0.878554  4.03909
     14:     1239.8717: 0.0279601 0.00906897 0.0591969 0.0833907 0.878932  4.04509
     15:     1239.8095: 0.0280679 0.00954747 0.0591636 0.0814308 0.880411  4.05096
     16:     1239.6706: 0.0286140 0.00909848 0.0568712 0.0730606 0.885602  4.08052
     17:     1239.4097: 0.0291981 0.00945442 0.0569335 0.0761162 0.885506  4.11066
     18:     1239.1921: 0.0297855 0.00813968 0.0570266 0.0777199 0.884263  4.14077
     19:     1237.4065: 0.0378816 0.00916836 0.0611503 0.0962011 0.866311  4.53262
     20:     1236.0187: 0.0474862 0.0119057 0.0860149 0.0593442 0.861069  4.87306
     21:     1235.6602: 0.0514810 0.0148099 0.0389563 0.107756 0.853585  5.00478
     22:     1235.5177: 0.0514830 0.0140143 0.0414264 0.109731 0.856621  5.00490
     23:     1235.3908: 0.0515747 0.0120756 0.0411656 0.108898 0.856575  5.00688
     24:     1235.3464: 0.0516756 0.0123582 0.0415699 0.108667 0.857606  5.00904
     25:     1235.2923: 0.0518800 0.0113670 0.0417760 0.107618 0.858786  5.01342
     26:     1234.4489: 0.0628380 0.00456269 0.0454291 0.0570807 0.903085  5.24559
     27:     1233.7432: 0.0743003 0.00752352 0.0555153 0.0609294 0.887330  5.45231
     28:     1233.3396: 0.0715596 0.00759836 0.0606619 0.0619597 0.879891  5.91220
     29:     1233.1336: 0.0710276 0.00804537 0.0601194 0.0603468 0.879382  6.38275
     30:     1233.0794: 0.0723806 0.00751815 0.0607556 0.0611292 0.879334  6.75054
     31:     1233.0703: 0.0716884 0.00797577 0.0609077 0.0565111 0.879906  7.05544
     32:     1233.0569: 0.0710001 0.00793981 0.0602944 0.0590192 0.879605  6.93357
     33:     1233.0566: 0.0714659 0.00786189 0.0606153 0.0586174 0.879709  6.93720
     34:     1233.0566: 0.0713514 0.00787563 0.0605392 0.0585891 0.879760  6.94089
     35:     1233.0566: 0.0713483 0.00787270 0.0605330 0.0585862 0.879774  6.94068
     36:     1233.0566: 0.0713478 0.00787158 0.0605322 0.0585820 0.879781  6.94065
    
    Final Estimate of the Negative LLH:
     LLH:  1298.244    norm LLH:  1.276543 
            mu      omega     alpha1     alpha2      beta1      shape 
    0.07607082 0.00894822 0.06053217 0.05858196 0.87978050 6.94064829 
    
    R-optimhess Difference Approximated Hessian Matrix:
                     mu        omega       alpha1       alpha2        beta1
    mu     -2153.117662    -621.1951    -31.75947   -114.88385   -244.86081
    omega   -621.195057 -120232.3673 -33430.20140 -33493.36066 -49469.40182
    alpha1   -31.759470  -33430.2014 -18880.27948 -18629.79462 -22684.69539
    alpha2  -114.883854  -33493.3607 -18629.79462 -19095.10434 -23166.64902
    beta1   -244.860805  -49469.4018 -22684.69539 -23166.64902 -30514.84706
    shape     -2.308763     -89.5601    -52.54123    -54.24834    -67.65708
                 shape
    mu      -2.3087627
    omega  -89.5600983
    alpha1 -52.5412311
    alpha2 -54.2483416
    beta1  -67.6570774
    shape   -0.5514504
    attr(,"time")
    Time difference of 0.08078694 secs
    
    --- END OF TRACE ---
    
    
    Time to Estimate Parameters:
     Time difference of 0.4488659 secs
    

    Warning message:
    "Using formula(x) is deprecated when x is a character vector of length > 1.
      Consider formula(paste(x, collapse = " ")) instead."
    

    
    Title:
     GARCH Modelling 
    
    Call:
     garchFit(formula = ~garch(2, 1), data = y, cond.dist = distriduction) 
    
    Mean and Variance Equation:
     data ~ garch(2, 1)
    <environment: 0x0000000030dd0790>
     [data = y]
    
    Conditional Distribution:
     std 
    
    Coefficient(s):
           mu      omega     alpha1     alpha2      beta1      shape  
    0.0760708  0.0089482  0.0605322  0.0585820  0.8797805  6.9406483  
    
    Std. Errors:
     based on Hessian 
    
    Error Analysis:
            Estimate  Std. Error  t value Pr(>|t|)    
    mu      0.076071    0.021676    3.510 0.000449 ***
    omega   0.008948    0.005933    1.508 0.131471    
    alpha1  0.060532    0.038035    1.591 0.111499    
    alpha2  0.058582    0.047850    1.224 0.220847    
    beta1   0.879781    0.029877   29.447  < 2e-16 ***
    shape   6.940648    1.603493    4.328  1.5e-05 ***
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
    
    Log Likelihood:
     -1298.244    normalized:  -1.276543 
    
    Description:
     Wed Mar 31 10:04:42 2021 by user: 13631 
    
    
    Standardised Residuals Tests:
                                    Statistic p-Value     
     Jarque-Bera Test   R    Chi^2  45.61896  1.24156e-10 
     Shapiro-Wilk Test  R    W      0.9889919 6.495727e-07
     Ljung-Box Test     R    Q(10)  11.24491  0.3387581   
     Ljung-Box Test     R    Q(15)  29.43389  0.01413476  
     Ljung-Box Test     R    Q(20)  35.99697  0.01539372  
     Ljung-Box Test     R^2  Q(10)  13.81003  0.1818344   
     Ljung-Box Test     R^2  Q(15)  19.83774  0.1782458   
     Ljung-Box Test     R^2  Q(20)  24.33898  0.2278982   
     LM Arch Test       R    TR^2   13.49609  0.3340363   
    
    Information Criterion Statistics:
         AIC      BIC      SIC     HQIC 
    2.564885 2.593939 2.564816 2.575919 
    
    

Jarque-Bera Test(正态分布检验): h0:接受x服从正态分布的假设；h1:拒绝该假设。

Shapiro-Wilk Test(正态分布检验): 与Jarque-Bera Test完全相反。

关于分布的一些选择：

- "norm"——正态分布

- "snorm"——偏正态分布

- "ged"——广义误差分布

- "sged"——偏广义正态分布

- "std"——学生分布

- "sstd"——偏学生分布

- "nig"——正态逆高斯分布

- "QMLE"——准最大似然估计


```R
library(forecast)
```


```R
# 为什么用不同的R包估计的结果会很不一样？
```


```R
# 图片大小设置
options(repr.plot.width=12, repr.plot.height=10)
```


```R
par(mfrow=c(4, 4))
plot(fit, which='all')
par(mfrow=c(1, 1))
```


![png](Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_files/Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_21_0.png)



```R
par(mfrow=c(2, 2))
plot(fit, which=1:4)
par(mfrow=c(1, 1))
```


![png](Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_files/Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_22_0.png)



```R
predict(fit, n.ahead=50, mse="cond", plot=TRUE, crit_val=2)
```


<table class="dataframe">
<caption>A data.frame: 50 × 5</caption>
<thead>
	<tr><th scope=col>meanForecast</th><th scope=col>meanError</th><th scope=col>standardDeviation</th><th scope=col>lowerInterval</th><th scope=col>upperInterval</th></tr>
	<tr><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><td>0.07607082</td><td>0.5928249</td><td>0.5928249</td><td>-1.109579</td><td>1.261721</td></tr>
	<tr><td>0.07607082</td><td>0.5892155</td><td>0.5892155</td><td>-1.102360</td><td>1.254502</td></tr>
	<tr><td>0.07607082</td><td>0.5966484</td><td>0.5966484</td><td>-1.117226</td><td>1.269368</td></tr>
	<tr><td>0.07607082</td><td>0.6033471</td><td>0.6033471</td><td>-1.130623</td><td>1.282765</td></tr>
	<tr><td>0.07607082</td><td>0.6100022</td><td>0.6100022</td><td>-1.143933</td><td>1.296075</td></tr>
	<tr><td>0.07607082</td><td>0.6165764</td><td>0.6165764</td><td>-1.157082</td><td>1.309224</td></tr>
	<tr><td>0.07607082</td><td>0.6230747</td><td>0.6230747</td><td>-1.170079</td><td>1.322220</td></tr>
	<tr><td>0.07607082</td><td>0.6294992</td><td>0.6294992</td><td>-1.182928</td><td>1.335069</td></tr>
	<tr><td>0.07607082</td><td>0.6358522</td><td>0.6358522</td><td>-1.195634</td><td>1.347775</td></tr>
	<tr><td>0.07607082</td><td>0.6421358</td><td>0.6421358</td><td>-1.208201</td><td>1.360343</td></tr>
	<tr><td>0.07607082</td><td>0.6483521</td><td>0.6483521</td><td>-1.220633</td><td>1.372775</td></tr>
	<tr><td>0.07607082</td><td>0.6545029</td><td>0.6545029</td><td>-1.232935</td><td>1.385077</td></tr>
	<tr><td>0.07607082</td><td>0.6605901</td><td>0.6605901</td><td>-1.245109</td><td>1.397251</td></tr>
	<tr><td>0.07607082</td><td>0.6666155</td><td>0.6666155</td><td>-1.257160</td><td>1.409302</td></tr>
	<tr><td>0.07607082</td><td>0.6725807</td><td>0.6725807</td><td>-1.269091</td><td>1.421232</td></tr>
	<tr><td>0.07607082</td><td>0.6784873</td><td>0.6784873</td><td>-1.280904</td><td>1.433045</td></tr>
	<tr><td>0.07607082</td><td>0.6843368</td><td>0.6843368</td><td>-1.292603</td><td>1.444744</td></tr>
	<tr><td>0.07607082</td><td>0.6901307</td><td>0.6901307</td><td>-1.304191</td><td>1.456332</td></tr>
	<tr><td>0.07607082</td><td>0.6958704</td><td>0.6958704</td><td>-1.315670</td><td>1.467812</td></tr>
	<tr><td>0.07607082</td><td>0.7015572</td><td>0.7015572</td><td>-1.327044</td><td>1.479185</td></tr>
	<tr><td>0.07607082</td><td>0.7071925</td><td>0.7071925</td><td>-1.338314</td><td>1.490456</td></tr>
	<tr><td>0.07607082</td><td>0.7127773</td><td>0.7127773</td><td>-1.349484</td><td>1.501625</td></tr>
	<tr><td>0.07607082</td><td>0.7183130</td><td>0.7183130</td><td>-1.360555</td><td>1.512697</td></tr>
	<tr><td>0.07607082</td><td>0.7238006</td><td>0.7238006</td><td>-1.371530</td><td>1.523672</td></tr>
	<tr><td>0.07607082</td><td>0.7292413</td><td>0.7292413</td><td>-1.382412</td><td>1.534553</td></tr>
	<tr><td>0.07607082</td><td>0.7346361</td><td>0.7346361</td><td>-1.393201</td><td>1.545343</td></tr>
	<tr><td>0.07607082</td><td>0.7399859</td><td>0.7399859</td><td>-1.403901</td><td>1.556043</td></tr>
	<tr><td>0.07607082</td><td>0.7452919</td><td>0.7452919</td><td>-1.414513</td><td>1.566655</td></tr>
	<tr><td>0.07607082</td><td>0.7505548</td><td>0.7505548</td><td>-1.425039</td><td>1.577180</td></tr>
	<tr><td>0.07607082</td><td>0.7557757</td><td>0.7557757</td><td>-1.435481</td><td>1.587622</td></tr>
	<tr><td>0.07607082</td><td>0.7609553</td><td>0.7609553</td><td>-1.445840</td><td>1.597981</td></tr>
	<tr><td>0.07607082</td><td>0.7660946</td><td>0.7660946</td><td>-1.456118</td><td>1.608260</td></tr>
	<tr><td>0.07607082</td><td>0.7711943</td><td>0.7711943</td><td>-1.466318</td><td>1.618459</td></tr>
	<tr><td>0.07607082</td><td>0.7762552</td><td>0.7762552</td><td>-1.476440</td><td>1.628581</td></tr>
	<tr><td>0.07607082</td><td>0.7812782</td><td>0.7812782</td><td>-1.486486</td><td>1.638627</td></tr>
	<tr><td>0.07607082</td><td>0.7862638</td><td>0.7862638</td><td>-1.496457</td><td>1.648598</td></tr>
	<tr><td>0.07607082</td><td>0.7912129</td><td>0.7912129</td><td>-1.506355</td><td>1.658497</td></tr>
	<tr><td>0.07607082</td><td>0.7961261</td><td>0.7961261</td><td>-1.516181</td><td>1.668323</td></tr>
	<tr><td>0.07607082</td><td>0.8010040</td><td>0.8010040</td><td>-1.525937</td><td>1.678079</td></tr>
	<tr><td>0.07607082</td><td>0.8058474</td><td>0.8058474</td><td>-1.535624</td><td>1.687766</td></tr>
	<tr><td>0.07607082</td><td>0.8106569</td><td>0.8106569</td><td>-1.545243</td><td>1.697385</td></tr>
	<tr><td>0.07607082</td><td>0.8154330</td><td>0.8154330</td><td>-1.554795</td><td>1.706937</td></tr>
	<tr><td>0.07607082</td><td>0.8201763</td><td>0.8201763</td><td>-1.564282</td><td>1.716423</td></tr>
	<tr><td>0.07607082</td><td>0.8248875</td><td>0.8248875</td><td>-1.573704</td><td>1.725846</td></tr>
	<tr><td>0.07607082</td><td>0.8295670</td><td>0.8295670</td><td>-1.583063</td><td>1.735205</td></tr>
	<tr><td>0.07607082</td><td>0.8342154</td><td>0.8342154</td><td>-1.592360</td><td>1.744502</td></tr>
	<tr><td>0.07607082</td><td>0.8388333</td><td>0.8388333</td><td>-1.601596</td><td>1.753737</td></tr>
	<tr><td>0.07607082</td><td>0.8434211</td><td>0.8434211</td><td>-1.610771</td><td>1.762913</td></tr>
	<tr><td>0.07607082</td><td>0.8479793</td><td>0.8479793</td><td>-1.619888</td><td>1.772029</td></tr>
	<tr><td>0.07607082</td><td>0.8525084</td><td>0.8525084</td><td>-1.628946</td><td>1.781088</td></tr>
</tbody>
</table>




![png](Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_files/Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_23_1.png)



```R
# 为什么估计的是一根横线，未来估计的均值完全没有变化？
```

## 9.3 单变量GARCH的专业处理

### 9.3.1 rugarch 中GARCH 模型的基本设定

范例程序9-5: rugarch 包中对GARCH模型的处理


```R
library(rugarch)
```

    Loading required package: parallel
    
    
    Attaching package: 'rugarch'
    
    
    The following object is masked from 'package:stats':
    
        sigma
    
    
    


```R
# archm?
# archm 是否在均值方程中加入ARCH项。
# archpow 是否在均值回归的 ARCH 中使用 st.deviation (1)或 variance (2)
# (整数)是否将最后一个‘arcox’外部回归变量乘以条件标准差。

mean.spec = list(armaOrder=c(1, 1), include.mean=T, archm=F, archpow=1, arfima=F,
                external.regressors=NULL)
var.spec = list(model='sGARCH', garchOrder=c(2, 1), submodel=NULL, external.regressors=NULL,
               variance.targeting=F)
dist.spec = c("norm")
myspec = ugarchspec(mean.model=mean.spec, variance.model=var.spec, distribution.model=dist.spec)

out = ugarchfit(spec=myspec, data=y, solver.control=list(trace=0))
show(out)
```

    
    *---------------------------------*
    *          GARCH Model Fit        *
    *---------------------------------*
    
    Conditional Variance Dynamics 	
    -----------------------------------
    GARCH Model	: sGARCH(2,1)
    Mean Model	: ARFIMA(1,0,1)
    Distribution	: norm 
    
    Optimal Parameters
    ------------------------------------
            Estimate  Std. Error  t value Pr(>|t|)
    mu      0.068673    0.023641   2.9049 0.003674
    ar1    -0.804506    0.103194  -7.7961 0.000000
    ma1     0.855487    0.088666   9.6484 0.000000
    omega   0.018966    0.008448   2.2451 0.024759
    alpha1  0.078466    0.034636   2.2654 0.023486
    alpha2  0.068907    0.044623   1.5442 0.122539
    beta1   0.838607    0.034025  24.6468 0.000000
    
    Robust Standard Errors:
            Estimate  Std. Error  t value Pr(>|t|)
    mu      0.068673    0.023283   2.9495 0.003183
    ar1    -0.804506    0.083548  -9.6293 0.000000
    ma1     0.855487    0.069056  12.3883 0.000000
    omega   0.018966    0.012984   1.4607 0.144095
    alpha1  0.078466    0.050562   1.5519 0.120690
    alpha2  0.068907    0.056916   1.2107 0.226023
    beta1   0.838607    0.049702  16.8727 0.000000
    
    LogLikelihood : -1307.764 
    
    Information Criteria
    ------------------------------------
                       
    Akaike       2.5856
    Bayes        2.6195
    Shibata      2.5855
    Hannan-Quinn 2.5984
    
    Weighted Ljung-Box Test on Standardized Residuals
    ------------------------------------
                            statistic p-value
    Lag[1]                    0.04721  0.8280
    Lag[2*(p+q)+(p+q)-1][5]   1.62049  0.9950
    Lag[4*(p+q)+(p+q)-1][9]   3.17084  0.8631
    d.o.f=2
    H0 : No serial correlation
    
    Weighted Ljung-Box Test on Standardized Squared Residuals
    ------------------------------------
                             statistic p-value
    Lag[1]                     0.02388  0.8772
    Lag[2*(p+q)+(p+q)-1][8]    6.31488  0.2053
    Lag[4*(p+q)+(p+q)-1][14]   9.77208  0.2161
    d.o.f=3
    
    Weighted ARCH LM Tests
    ------------------------------------
                Statistic Shape Scale P-Value
    ARCH Lag[4]    0.6908 0.500 2.000  0.4059
    ARCH Lag[6]    0.9493 1.461 1.711  0.7623
    ARCH Lag[8]    3.3474 2.368 1.583  0.4806
    
    Nyblom stability test
    ------------------------------------
    Joint Statistic:  1.0894
    Individual Statistics:             
    mu     0.2935
    ar1    0.1578
    ma1    0.1472
    omega  0.3104
    alpha1 0.1916
    alpha2 0.2152
    beta1  0.2062
    
    Asymptotic Critical Values (10% 5% 1%)
    Joint Statistic:     	 1.69 1.9 2.35
    Individual Statistic:	 0.35 0.47 0.75
    
    Sign Bias Test
    ------------------------------------
                       t-value      prob sig
    Sign Bias           2.0317 4.244e-02  **
    Negative Sign Bias  0.4882 6.255e-01    
    Positive Sign Bias  1.7782 7.567e-02   *
    Joint Effect       21.7873 7.223e-05 ***
    
    
    Adjusted Pearson Goodness-of-Fit Test:
    ------------------------------------
      group statistic p-value(g-1)
    1    20     50.67    0.0001044
    2    30     58.72    0.0008881
    3    40     66.70    0.0037504
    4    50     73.41    0.0135355
    
    
    Elapsed time : 0.314296 
    
    

符号偏误检验（sign bias test)统计量检验了标准化残差的平方的常数，对于冲击是否有正负残差的差异，根据下面的检验结果可知正负收益率对冲击有不同的反应，建议使用非对称形式的模型。

调整皮尔森拟合优度检验 (adjust pearson gordness of-fit test) 的基础是比较标准化残差的数据所呈现的分布和理论分布的差异。此处是正态分布。这个检验是依照 Palm 和 Vlaar(l997)的分群做法计算出的，根据结果的 p 值，原假设被显著地拒绝了，也就是这个模型适配正态分布不是很好，应该选择其他分布。


```R
plot(out, which="all")
```

    
    please wait...calculating quantiles...
    


![png](Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_files/Ch9%E5%8D%95%E5%8F%98%E9%87%8FGARCH%E6%A8%A1%E5%9E%8B_32_1.png)


### 9.3.2 rugarch中 GARCH 模型的高级设定

本书作者开发了一个包 iClick，内有 iClick.GARCH 功能，可以将 8 种概率分布的组合，依照均值方程式和方差方程式一次呈现，相当有利于比较，如范例程序 9.6 所示。

范例程序9-6: iCIick GARCH使用演示


```R
dat0 = read.csv("doc/Ch09/wti.csv")
head(dat0)
```


<table class="dataframe">
<caption>A data.frame: 6 × 9</caption>
<thead>
	<tr><th></th><th scope=col>Dates</th><th scope=col>Open</th><th scope=col>High</th><th scope=col>Low</th><th scope=col>Last</th><th scope=col>Change</th><th scope=col>Settle</th><th scope=col>Volume</th><th scope=col>Open.Interest</th></tr>
	<tr><th></th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>1983/3/30</td><td>29.01</td><td>29.56</td><td>29.01</td><td>NA</td><td>NA</td><td>29.40</td><td>949</td><td>470</td></tr>
	<tr><th scope=row>2</th><td>1983/3/31</td><td>29.40</td><td>29.60</td><td>29.25</td><td>NA</td><td>NA</td><td>29.29</td><td>521</td><td>523</td></tr>
	<tr><th scope=row>3</th><td>1983/4/4 </td><td>29.30</td><td>29.70</td><td>29.29</td><td>NA</td><td>NA</td><td>29.44</td><td>156</td><td>583</td></tr>
	<tr><th scope=row>4</th><td>1983/4/5 </td><td>29.50</td><td>29.80</td><td>29.50</td><td>NA</td><td>NA</td><td>29.71</td><td>175</td><td>623</td></tr>
	<tr><th scope=row>5</th><td>1983/4/6 </td><td>29.90</td><td>29.92</td><td>29.65</td><td>NA</td><td>NA</td><td>29.90</td><td>392</td><td>640</td></tr>
	<tr><th scope=row>6</th><td>1983/4/7 </td><td>29.90</td><td>30.20</td><td>29.86</td><td>NA</td><td>NA</td><td>30.17</td><td>817</td><td>795</td></tr>
</tbody>
</table>




```R
library(timeSeries)
dat1 = as.timeSeries(dat0[, "Settle"], as.Date(dat0[,"Dates"]))
head(dat1)
```


    GMT
                TS.1
    1983-03-30 29.40
    1983-03-31 29.29
    1983-04-04 29.44
    1983-04-05 29.71
    1983-04-06 29.90
    1983-04-07 30.17



```R
y = returns(dat1) * 100
names(y) = "y"
head(y)
```


    GMT
                        y
    1983-03-31 -0.3748514
    1983-04-04  0.5108133
    1983-04-05  0.9129396
    1983-04-06  0.6374791
    1983-04-07  0.8989573
    1983-04-08  0.6936444



```R
# detach(package:timeSeries)
```


```R
# install.packages('iClick')
```


```R
library(iClick)
```

    Warning message:
    "package 'iClick' was built under R version 4.0.4"
    Loading required package: lattice
    
    Loading required package: tcltk
    
    Loading required package: sandwich
    
    Loading required package: xts
    
    Loading required package: zoo
    
    
    Attaching package: 'zoo'
    
    
    The following object is masked from 'package:timeSeries':
    
        time<-
    
    
    The following objects are masked from 'package:base':
    
        as.Date, as.Date.numeric
    
    
    


```R
meanEQ = list(AR=1, MA=0, Exo=NULL, autoFitArma=FALSE, arfimaDiff=FALSE,
             archM=FALSE)
garchEQ = list(Type="sGARCH", P=1, Q=1, exo=NULL)
# iClick.GARCH(y, meanEQ, garchEQ, n.ahead=10)
# 估计
```


```R

```
