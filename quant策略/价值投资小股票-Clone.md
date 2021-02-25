

# 价值投资小股票-Clone

- 是否有未来函数被使用？
- 是否在阈值选择中偶然选中大牛股？（要记住，策略选股旨在找出潜力大的股票，如果单支股票的收益占比太大，那么说明你的收益大部分只来源于一支股票，是极不稳定的，代表性会降低。）





最大回撤如何降低？



理解代码

如何研究选股的策略？

策略优化？（选股条件、明确什么时期策略收益较低）

​	选股条件：阈值、增加选择条件、替换更优条件

```python
import pandas as pd
import numpy as np
from jqdata import *
from kuanke.wizard import *
```

`kuanke.wizard` 包，后面使用了 `order_style` 函数。



```python
# 初始化函数，设定基准等等
def initialize(context):
    # 设定沪深300
    set_benchmark('000300.XSHG')
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)
    # 输出内容到日志 log.info()
    log.info('初始函数开始运行且全局只运行一次')
    # 过滤掉order系列API产生的比error级别低的log
    # log.set_level('order', 'error')
    #策略参数设置
    #操作的股票列表
    g.buy_list = []
    # 设置滑点
    set_slippage(FixedSlippage(0.0026))
    ### 股票相关设定 ###
    # 股票类每笔交易时的手续费是：买入时佣金万分之三，卖出时佣金万分之三加千分之一印花税, 每笔交易佣金最低扣5块钱
    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
    # 个股最大持仓比重
    g.security_max_proportion = 0.2
    # 最大建仓数量
    # g.max_hold_stocknum = 10
    g.max_hold_stocknum = 5
    # 单只最大买入股数或金额
    g.max_buy_value = None
    g.max_buy_amount = None
    # 委托类型
    g.order_style_str = 'by_cap_mean'
    g.order_style_value = 100
    # 每月第10个交易日进行操作
    # 开盘前运行
    run_monthly(before_market_open,10,time='before_open', reference_security='000300.XSHG') 
    # 开盘时运行
    run_monthly(market_open,10,time='open', reference_security='000300.XSHG')
```

委托类型一块不太明白。

```python
## 开盘前运行函数     
def before_market_open(context):
    # 获取要操作的股票列表
    temp_list = get_stock_list(context)
    # 去除周期行业
    # 排除行业：采掘、化工、轻工制造、房地产、 餐饮旅游、休闲服务、 汽车、机械设备
    g.industry_list = ["801010","801040","801050","801080","801110","801120","801130","801150","801160","801200","801230","801710","801720","801730","801740","801750","801760","801770","801780","801790"]
    temp_list = industry_filter(context, temp_list, g.industry_list)

    log.info('满足条件的股票有%s只'%len(temp_list))
    #按市值进行排序
    g.buy_list = get_check_stocks_sort(context,temp_list)
    print(("the list consist of ",g.buy_list));
```



```python
## 开盘时运行函数
def market_open(context):
    #卖出不在买入列表中的股票
    sell(context,g.buy_list)
    #买入不在持仓中的股票，按要操作的股票平均资金
    buy(context,g.buy_list)
```



```python
#交易函数 - 买入
def buy(context, buy_lists):
    # 获取最终的 buy_lists 列表
    Num = g.max_hold_stocknum - len(context.portfolio.positions)
    buy_lists = buy_lists[:Num]
    # 买入股票
    if len(buy_lists)>0:
        # 分配资金
        
        result = order_style(context,buy_lists,g.max_hold_stocknum, g.order_style_str, g.order_style_value)
        for stock in buy_lists:
            if len(context.portfolio.positions) < g.max_hold_stocknum:
                # 获取资金
                amount = result[stock]
                
                # 判断个股最大持仓比重
                #value = judge_security_max_proportion(context,stock,Cash,g.security_max_proportion)
                # 判断单只最大买入股数或金额
                #amount = max_buy_value_or_amount(stock,value,g.max_buy_value,g.max_buy_amount)
                # 下单
                #log.info('Cash: ' + str(Cash) + ' value:' +str(value))
                cash = context.portfolio.available_cash
                
                log.info(stock +' 购买资金：' +str(amount) + ' 剩余资金：' + str(cash))
                #order(stock, amount, MarketOrderStyle())
                order_target_value(stock, amount)
                 
        #半年平衡一次仓位避免单一持仓过大
        #month = context.current_dt.month
        #if month == 6  or month == 12:
        #    maxvalue = context.portfolio.total_value*g.security_max_proportion
        #    for s in list(context.portfolio.positions.keys()):
        #        if context.portfolio.positions[s].value > maxvalue :
        #            order_target_value(s,maxvalue)
    return
```



```python
# 交易函数 - 出场
def sell(context, buy_lists):
    # 获取 sell_lists 列表
    hold_stock = list(context.portfolio.positions.keys())
    for s in hold_stock:
        #卖出不在买入列表中的股票
        if s not in buy_lists:
            order_target_value(s,0)
```



```python
#按市值进行排序   
#从大到小
def get_check_stocks_sort(context,check_out_lists):
    df = get_fundamentals(query(valuation.circulating_cap,valuation.pe_ratio,valuation.code).filter(valuation.code.in_(check_out_lists)),date=context.previous_date)
    #asc值为0，从大到小
    #df = df.sort_values('circulating_cap',ascending=0)
    #asc值为1，从小到大
    df = df.sort_values('circulating_cap',ascending=1)
    out_lists = list(df['code'].values)
    return out_lists
```



```python
'''
1.总市值≧市场平均值*1.0。
2.最近一季流动比率≧市场平均值（流动资产合计/流动负债合计）。
3.近四季股东权益报酬率（roe）≧市场平均值。
4.近五年自由现金流量均为正值。（cash_flow.net_operate_cash_flow - cash_flow.net_invest_cash_flow）
5.近四季营收成长率介于6%至30%（）。    'IRYOY':indicator.inc_revenue_year_on_year, # 营业收入同比增长率(%)
6.近四季盈余成长率介于8%至50%。(eps比值)
'''
def get_stock_list(context):
    temp_list = list(get_all_securities(types=['stock']).index)    
    #剔除停牌股
    all_data = get_current_data()
    temp_list = [stock for stock in temp_list if not all_data[stock].paused]
    #获取多期财务数据
    panel = get_data(temp_list,4)
    #1.总市值≧市场平均值*1.0。
    df_mkt = panel.loc[['circulating_market_cap'],3,:]
    df_mkt = df_mkt[df_mkt['circulating_market_cap']>df_mkt['circulating_market_cap'].mean()]
    l1 = set(df_mkt.index)
    
    #2.最近一季流动比率≧市场平均值（流动资产合计/流动负债合计）。
    df_cr = panel.loc[['total_current_assets','total_current_liability'],3,:]
    #替换零的数值
    df_cr = df_cr[df_cr['total_current_liability'] != 0]
    df_cr['cr'] = df_cr['total_current_assets']/df_cr['total_current_liability']
    df_cr_temp = df_cr[df_cr['cr']>df_cr['cr'].mean()]
    l2 = set(df_cr_temp.index)

    #3.近四季股东权益报酬率（roe）≧市场平均值。
    l3 = {}
    for i in range(4):
        roe_mean = panel.loc['roe',i,:].mean()
        df_3 = panel.iloc[:,i,:]
        df_temp_3 = df_3[df_3['roe']>roe_mean]
        if i == 0:    
            l3 = set(df_temp_3.index)
        else:
            l_temp = df_temp_3.index
            l3 = l3 & set(l_temp)
    l3 = set(l3)

    #4.近三年自由现金流量均为正值。（cash_flow.net_operate_cash_flow - cash_flow.net_invest_cash_flow）
    y = context.current_dt.year
    mo = context.current_dt.month
    if mo < 4:
        y -= 1
    l4 = {}
    for i in range(1,4):
        df = get_fundamentals(query(cash_flow.code,cash_flow.statDate,cash_flow.net_operate_cash_flow, cash_flow.net_invest_cash_flow),statDate=str(y-i))
        if len(df) != 0:
            df['FCF'] = df['net_operate_cash_flow']-df['net_invest_cash_flow']
            #df = df[df['net_operate_cash_flow']>0]
            df = df[df['FCF']>0]
            l_temp = df['code'].values
            if len(l4) != 0:
                l4 = set(l4) & set(l_temp)
            l4 = l_temp
        else:
            continue
    l4 = set(l4)
    #print 'test'
    #print l4
    
    #5.近四季营收成长率介于0%至50%（）。    'IRYOY':indicator.inc_revenue_year_on_year, # 营业收入同比增长率(%)
    l5 = {}
    for i in range(4):
        df_5 = panel.iloc[:,i,:]
        df_temp_5 = df_5[(df_5['inc_revenue_year_on_year']>0) & (df_5['inc_revenue_year_on_year']<50)]
        if i == 0:    
            l5 = set(df_temp_5.index)
        else:
            l_temp = df_temp_5.index
            l5 = l5 & set(l_temp)
    l5 = set(l5)
    
    #6.近四季EPS在0.04至1
    l6 = {}
    for i in range(4):
        df_6 = panel.iloc[:,i,:]
        df_temp = df_6[(df_6['eps']>0.04) & (df_6['eps']<0.5)]
        if i == 0:    
            l6 = set(df_temp.index)
        else:
            l_temp = df_temp.index
            l6 = l6 & set(l_temp)
    l6 = set(l6)
    
    return list(l1 & l2 &l3 & l4 & l5 & l6)
```



```python
#去极值（分位数法）  
def winsorize(se):
    q = se.quantile([0.025, 0.975])
    if isinstance(q, pd.Series) and len(q) == 2:
        se[se < q.iloc[0]] = q.iloc[0]
        se[se > q.iloc[1]] = q.iloc[1]
    return se
```



```python
#获取多期财务数据内容
def get_data(pool, periods):
    q = query(valuation.code, income.statDate, income.pubDate).filter(valuation.code.in_(pool))
    df = get_fundamentals(q)
    df.index = df.code
    stat_dates = set(df.statDate)
    stat_date_stocks = { sd:[stock for stock in df.index if df['statDate'][stock]==sd] for sd in stat_dates }

    def quarter_push(quarter):
        if quarter[-1]!='1':
            return quarter[:-1]+str(int(quarter[-1])-1)
        else:
            return str(int(quarter[:4])-1)+'q4'

    q = query(valuation.code,valuation.code,valuation.circulating_market_cap,balance.total_current_assets,balance.total_current_liability,\
indicator.roe,cash_flow.net_operate_cash_flow,cash_flow.net_invest_cash_flow,indicator.inc_revenue_year_on_year,indicator.eps
              )

    stat_date_panels = { sd:None for sd in stat_dates }

    for sd in stat_dates:
        quarters = [sd[:4]+'q'+str(int(int(sd[5:7])/3))]
        for i in range(periods-1):
            quarters.append(quarter_push(quarters[-1]))
        nq = q.filter(valuation.code.in_(stat_date_stocks[sd]))
        pre_panel = { quarter:get_fundamentals(nq, statDate = quarter) for quarter in quarters }
        for thing in list(pre_panel.values()):
            thing.index = thing.code.values
        panel = pd.Panel(pre_panel)
        panel.items = list(range(len(quarters)))
        stat_date_panels[sd] = panel.transpose(2,0,1)

    final = pd.concat(list(stat_date_panels.values()), axis=2)

    return final.dropna(axis=2)
```



```python
# 行业过滤
def industry_filter(context, security_list, industry_list):
    if len(industry_list) == 0:
        # 返回股票列表
        return security_list
    else:
        securities = []
        for s in industry_list:
            temp_securities = get_industry_stocks(s)
            securities += temp_securities
        security_list = [stock for stock in security_list if stock in securities]
        # 返回股票列表
        return security_list
```



![image-20201218232313825](C:\Users\13631\AppData\Roaming\Typora\typora-user-images\image-20201218232313825.png)