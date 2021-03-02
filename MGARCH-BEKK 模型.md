# MGARCH-BEKK 模型

参考文献：https://d.cosx.org/d/421268-r-mgarchbekk



```
library(mgarchBEKK)
reg.bg.bear<-BEKK(error_vecmbear,order = c(1,1))
diagnoseBEKK(reg.bg.bear)
```

​	