# Ch2. 特征理解：我的数据集里有什么

终于可以开始处理一些真实的数据，编写真实的代码，看到真正的成效了！具体而言，我们会深入了解以下内容：

- 结构化数据与非结构化数据；
- 定量数据与定性数据；
- 数据的4个等级；
- 探索性数据分析和数据可视化；
- 描述性统计。

上面的每个主题都会让我们更好地理解自己面前的数据，数据集里有什么、没有什么，以及对如何进一步学习的基本见解。

如果你熟悉锡南的另一本书《数据科学原理》（*Principles of Data Science*），会发现本章的大部分内容都对应于这本书的第2章。不过，本章会更多地从机器学习的角度，而非整体的角度来看待数据。

## 2.1　数据结构的有无

拿到一个新的数据集后，首要任务是确认数据是结构化还是非结构化的。

- **结构化（有组织）数据**：可以分成观察值和特征的数据，一般以表格的形式组织（行是观察值，列是特征）。
- **非结构化（无组织）数据**：作为自由流动的实体，不遵循标准组织结构（例如表格）的数据。通常，非结构化数据在我们看来是**一团**数据，或只有一个特征（列）。

下面两个例子展示了结构化和非结构化数据的区别：

- 以原始文本格式存储的数据，例如服务器日志和推文，是非结构化数据；
- 科学仪器报告的气象数据是高度结构化的，因为存在表格的行列结构。

### 非结构化数据的例子：服务器日志

我们从公共数据中提取了一些服务器日志，放在文本文件中，作为非结构化数据的例子。可以看看这种数据的样子，方便日后识别：

```python
# 导入数据转换包Pandas
import pandas as pd
# 从服务器日志中创建Pandas DataFrame
logs = pd.read_table('../data/server_logs.txt', header=None, names=['Info'])

# header=None代表数据的第一行是第一个数据点，而不是列名
# names=['Info]表示我在DataFrame中手动设置了列名，方便使用
```

我们创建了一个叫作`logs`的Pandas DataFrame，用于存放服务器日志。可以用`.head()`方法看一下前几行：

```
# 查看前5行
logs.head()
```

`logs` DataFrame中数据的前5行如下表所示。

| Info |                                                   |
| :--- | :------------------------------------------------ |
| 0    | 64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] ... |
| 1    | 64.242.88.10 - - [07/Mar/2004:16:06:51 -0800] ... |
| 2    | 64.242.88.10 - - [07/Mar/2004:16:10:02 -0800] ... |
| 3    | 64.242.88.10 - - [07/Mar/2004:16:11:58 -0800] ... |
| 4    | 64.242.88.10 - - [07/Mar/2004:16:20:55 -0800] ... |

可以发现，表中每行代表一篇日志，而且只有一列：日志文本。这个文本并不是特征，只是来自服务器的原始日志。这个例子很好地代表了非结构化数据。通常，文本形式的数据都是非结构化的。

> ![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/tip.png)　重要的是要认识到，大部分非结构化数据都可以通过一些方法转换为结构化数据，这个问题我们下章再聊。

本书中要处理的大部分数据都是结构化的。也就是说，数据会有行和列。明白了这些，就可以开始研究表格数据中值的类型了。

## 2.2　定量数据和定性数据

为了完成对数据的判断，我们从区分度最高的顺序开始。在处理结构化的表格数据时（大部分时候都是如此），第一个问题一般是：数据是定量的，还是定性的？

**定量数据**本质上是数值，应该是衡量某样东西的数量。

**定性数据**本质上是类别，应该是描述某样东西的性质。

基本示例：

- 以华氏度或摄氏度表示的气温是定量的；
- 阴天或晴天是定性的；
- 白宫参观者的名字是定性的；
- 献血的血量是定量的。

上面的例子表明，对于类似的系统，我们可以从定量数据和定性数据两方面来描述。事实上，在大多数数据集中，我们会同时处理定量数据和定性数据。

有时，数据可以同时是定量和定性的。例如，餐厅的评分（1～5星）虽然是数，但是这个数也可以代表类别。如果餐厅评分应用要求你用定量的星级系统打分，并且公布带小数的平均分数（例如4.71星），那么这个数据是定量的。如果该应用问你的评价是**讨厌、还行、喜欢、喜爱**还是**特别喜爱**，那么这些就是类别。由于定量数据和定性数据之间的模糊性，我们会使用一个更深层次的方法进行处理，称为数据的4个等级。在此之前，先介绍本章的第一个数据集，巩固一下定性和定量数据的例子。

### 按工作分类的工资

我们先导入一些包：

```pyhton
# 导入探索性数据分析所需的包
# 存储表格数据
import pandas as pd
# 数学计算包
import numpy as np
# 流行的数据可视化包
import matplotlib.pyplot as plt
# 另一个流行的数据可视化包
import seaborn as sns
# 允许行内渲染图形
%matplotlib inline
# 流行的数据可视化主题
plt.style.use('fivethirtyeight')
```

然后导入第一个数据集，探索在旧金山做不同工作的工资。这个数据集可以公开获得，随意使用：

```python
# 导入数据集
# https://data.sfgov.org/City-Management-and-Ethics/Salary-Ranges-by-Job-
Classification/7h4w-reyq
salary_ranges = pd.read_csv('../data/Salary_Ranges_by_Job_Classification.csv')

# 查看前几行
salary_ranges.head()
```

我们先看一下前几行数据。

|      | SetID | Job Code | Eff Date               | Sal End Date           | Salary SetID | Sal Plan | Grade | Step | Biweekly High Rate | Biweekly Low Rate | Union Code | Extended Step | Pay Type |
| :--- | :---- | :------- | :--------------------- | :--------------------- | :----------- | :------- | :---- | :--- | :----------------- | :---------------- | :--------- | :------------ | :------- |
| 0    | COMMN | 0109     | 07/01/2009 12:00:00 AM | 06/30/2010 12:00:00 AM | COMMN        | SFM      | 00000 | 1    | $0.00              | $0.00             | 330        | 0             | C        |
| 1    | COMMN | 0110     | 07/01/2009 12:00:00 AM | 06/30/2010 12:00:00 AM | COMMN        | SFM      | 00000 | 1    | $15.00             | $15.00            | 323        | 0             | D        |
| 2    | COMMN | 0111     | 07/01/2009 12:00:00 AM | 06/30/2010 12:00:00 AM | COMMN        | SFM      | 00000 | 1    | $25.00             | $25.00            | 323        | 0             | D        |
| 3    | COMMN | 0112     | 07/01/2009 12:00:00 AM | 06/30/2010 12:00:00 AM | COMMN        | SFM      | 00000 | 1    | $50.00             | $50.00            | 323        | 0             | D        |
| 4    | COMMN | 0114     | 07/01/2009 12:00:00 AM | 06/30/2010 12:00:00 AM | COMMN        | SFM      | 00000 | 1    | $100.00            | $100.00           | 323        | 0             | M        |

可以看到表格有很多列，而且已经能发现其中一些是定性或定量的。我们用`.info()`方法了解一下数据有多少行：

```python
# 查看数据有多少行，是否有缺失值，以及每列的数据类型
salary_ranges.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1356 entries, 0 to 1355
Data columns (total 13 columns):
SetID                 1356 non-null object
Job Code              1356 non-null object
Eff Date              1356 non-null object
Sal End Date          1356 non-null object
Salary SetID          1356 non-null object
Sal Plan              1356 non-null object
Grade                 1356 non-null object
Step                  1356 non-null int64
Biweekly High Rate    1356 non-null object
Biweekly Low Rate     1356 non-null object
Union Code            1356 non-null int64
Extended Step         1356 non-null int64
Pay Type              1356 non-null object
dtypes: int64(3), object(10)
memory usage: 137.8+ KB
```

可以看到，数据有1356个条目（行）和13列。`.info()`方法也会报告每列的非空（`non-null`）项目数。这点非常重要，因为缺失数据是特征工程中最常见的问题之一。在Pandas包中有很多方法可以识别和处理缺失值，其中计算缺失值数量最快的方法是：

```python
# 另一种计算缺失值数量的方法
salary_ranges.isnull().sum()

SetID                 0
Job Code              0
Eff Date              0
Sal End Date          0
Salary SetID          0
Sal Plan              0
Grade                 0
Step                  0
Biweekly High Rate    0
Biweekly Low Rate     0
Union Code            0
Extended Step         0
Pay Type              0
dtype: int64
```

数据中看起来没有缺失值，可以（暂时）松一口气了。接下来用`describe`方法查看一些定量数据的描述性统计（应该有定量列）。注意，`describe`方法默认描述定量列，但是如果没有定量列，也会描述定性列：

```
# 显示描述性统计
salary_ranges.describe()
```

下表可以加深理解。

|       | Step        | Union Code  | Extended Step |
| :---- | :---------- | :---------- | :------------ |
| count | 1356.000000 | 1356.000000 | 1356.000000   |
| mean  | 1.294985    | 392.676991  | 0.150442      |
| std   | 1.045816    | 338.100562  | 1.006734      |
| min   | 1.000000    | 1.000000    | 0.000000      |
| 25%   | 1.000000    | 21.000000   | 0.000000      |
| 50%   | 1.000000    | 351.000000  | 0.000000      |
| 75%   | 1.000000    | 790.000000  | 0.000000      |
| max   | 5.000000    | 990.000000  | 11.000000     |

Pandas认为，数据只有3个定量列：`Step`、`Union Code`和`Extended Step`（步进、工会代码和增强步进）。先不说步进和增强步进，很明显工会代码不是定量的。虽然这一列是数，但这些数不代表数量，只代表某个工会的代码。因此需要做一些工作来理解我们感兴趣的特征。最值得注意的特征是一个定量列`Biweekly High Rate`（双周最高工资）和一个定性列`Grade`（工作种类）。

```python
salary_ranges = salary_ranges[['Biweekly High Rate', 'Grade']]
salary_ranges.head()
```

上面代码的执行结果如下所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.001.png)

我们清理一下数据，移除工资前面的美元符号，保证数据类型正确。当处理定量数据时，一般使用整数或浮点数作为类型（最好使用浮点数）；定性数据则一般使用字符串或Unicode对象。

```python
# 删除工资的美元符号
salary_ranges['Biweekly High Rate'].describe()

count         1356
unique         593
top       $3460.00
freq            12
Name: Biweekly High Rate, dtype: object
```

我们可以用Pandas的`map`功能，将函数映射到整个数据集：

```python
# 为了可视化，需要删除美元符号
salary_ranges['Biweekly High Rate'] = salary_ranges['Biweekly High Rate'].map(lambda value: value.replace('$',''))

# 检查是否已删除干净
salary_ranges.head()
```

执行结果如下：

|      | Biweekly High Rate | Grade |
| :--- | :----------------- | :---- |
| 0    | 0.00               | 00000 |
| 1    | 15.00              | 00000 |
| 2    | 25.00              | 00000 |
| 3    | 50.00              | 00000 |
| 4    | 100.00             | 00000 |

最后，将`Biweekly High Rate`列中的数据转换为浮点数：

```python
# 将双周最高工资转换为浮点数
salary_ranges['Biweekly High Rate'] = salary_ranges['Biweekly High Rate'].astype(float)
```

同时，将`Grade`列中的数据转换为字符串：

```python
# 将工作种类转换为字符串
salary_ranges['Grade'] = salary_ranges['Grade'].astype(str)

# 检查转换是否生效
salary_ranges.info()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1356 entries, 0 to 1355
Data columns (total 2 columns):
Biweekly High Rate    1356 non-null float64
Grade                 1356 non-null object
dtypes: float64(1), object(1)
memory usage: 21.3+ KB
```

可以看见，我们共有：

- 1356行（和开始时相同）

- 2列（我们选择的）

  - 双周最高工资

    ：定量列，代表某个部门的平均最高工资

    - 此列是定量的，因为其中的值是数，代表某人每两周的工资
    - 数据类型是浮点数，因为进行了强制转换

  - 工作种类

    ：工资对应的部门

    - 此列肯定是定性的，因为代码代表一个部门，而不是数量
    - 数据类型是对象，Pandas会把字符串归为此类

为了进一步研究定量数据和定性数据，我们开始研究数据的4个等级。

## 2.3　数据的4个等级

我们已经可以将数据分为定量和定性的，但是还可以继续分类。数据的4个等级是：

- 定类等级（nominal level）
- 定序等级（ordinal level）
- 定距等级（interval level）
- 定比等级（ratio level）

每个等级都有不同的控制和数学操作等级。了解数据的等级十分重要，因为它决定了可以执行的可视化类型和操作。

### 2.3.1　定类等级

定类等级是数据的第一个等级，其结构最弱。这个等级的数据只按名称分类。例如，血型（A、B、O和AB型）、动物物种和人名。这些数据都是定性的。

其他的例子包括：

- 在上面“旧金山工作工资”的数据集中，工作种类处于定类等级；
- 对于公司的访客名单，访客的姓和名处于定类等级；
- 实验中的动物物种处于定类等级。

**可以执行的数学操作**

对于每个等级，我们都会简要介绍可以执行的数学操作，以及不可以执行的数学操作。在这个等级上，不能执行任何定量数学操作，例如加法或除法。这些数学操作没有意义。因为没有加法和除法，所以在此等级上找不到平均值。当然了，没有“平均名”或“平均工作”这种说法。

但是，我们可以用Pandas的`value_counts`方法进行计数：

```python
# 对工作种类进行计数
salary_ranges['Grade'].value_counts().head()

00000    61
07450    12
07170     9
07420     9
06870     9
Name: Grade, dtype: int64
```

出现最多的工作种类是`00000`，意味着这个种类是**众数**，即最多的类别。因为能在定类等级上进行计数，所以可以绘制图表（如条形图）：

```python
# 对工作种类绘制条形图
salary_ranges['Grade'].value_counts().sort_values(ascending=False).head(20).plot
(kind='bar')
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.002.png)

在定类等级上，也可以绘制饼图：

```python
# 对工作种类绘制饼图（前5项）
salary_ranges['Grade'].value_counts().sort_values(ascending=False).head(5).plot
(kind='pie')
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.003.png)

### 2.3.2　定序等级

定类等级为我们提供了很多进一步探索的方法。向上一级就到了定序等级。定序等级继承了定类等级的所有属性，而且有重要的附加属性：

- 定序等级的数据可以**自然排序**；
- 这意味着，可以认为列中的某些数据比其他数据更好或更大。

和定类等级一样，定序等级的天然数据属性仍然是类别，即使用数来表示类别也是如此。

**可以执行的数学操作**

和定类等级相比，定序等级多了一些新的能力。在定序等级，我们可以像定类等级那样进行计数，也可以引入比较和排序。因此，可以使用新的图表了。不仅可以继续使用条形图和饼图，而且因为能排序和比较，所以能计算中位数和百分位数。对于中位数和百分位数，我们可以绘制茎叶图和箱线图。

其他的例子包括：

- 使用李克特量表**1**（比如1～10的评分）；
- 考试的成绩（F、D、C、B、A）。

**1**李克特量表（Likert scale）是调查研究中常用的心理反应量表，由一组陈述组成，每个陈述有从“非常同意”到“非常不同意”几种回答，由高到低计为不同的分数。——编者注

我们引入一个新的数据集来解释定序等级的数据。这个数据集表示多少人喜欢旧金山国际机场（IATA代码：SFO），也可以在旧金山的公开数据库中获取（https://data.sfgov.org/api/views/mjr8-p6m5/rows.csv?accessType=DOWNLOAD）。

```python
# 导入数据集
customer = pd.read_csv('../data/2013_SFO_Customer_survey.csv')
```

这个CSV文件有很多列：

```python
customer.shape

(3535, 95)
```

确切地说，是95列。有关这个数据集的更多信息，请参见网站上的数据字典（https://data.sfgov.org/api/views/mjr8-p6m5/files/FHnAUtMCD0C8CyLD3jqZ1-Xd1aap8L086KLWQ9SKZ_8?download=true&filename=AIR_DataDictionary_2013-SFO-Customer-Survey.pdf）。

现在，我们关注`Q7A_ART`这一列。如数据字典所述，`Q7A_ART`是关于艺术品和展览的。可能的选择是0、1、2、3、4、5、6，每个数字都有含义。

- **1**：不可接受
- **2**：低于平均
- **3**：平均
- **4**：不错
- **5**：特别好
- **6**：从未有人使用或参观过
- **0**：空

可以这样表示：

```python
art_ratings = customer['Q7A_ART']
art_ratings.describe()

count    3535.000000
mean        4.300707
std         1.341445
min         0.000000
25%         3.000000
50%         4.000000
75%         5.000000
max         6.000000
Name: Q7A_ART, dtype: float64
```

Pandas把这个列当作数值处理了，因为这个列充满数。然而我们需要知道，虽然这些值是数，但每个数其实代表的是类别，所以该数据是定性的，更具体地说，是属于定序等级。如果删除0和6这两个类别，剩下的5个有序类别类似于餐厅的评分：

```python
# 只考虑1～5
art_ratings = art_ratings[(art_ratings>=1) & (art_ratings<=5)]
```

然后将这些值转换为字符串：

```python
# 将值转换为字符串
art_ratings = art_ratings.astype(str)

art_ratings.describe()

count     2656
unique       5
top          4
freq      1066
Name: Q7A_ART, dtype: object
```

现在定序数据的格式是正确的，可以进行可视化：

```python
# 像定类等级一样用饼图
art_ratings.value_counts().plot(kind='pie')
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.004.png)

也可以将其可视化为条形图：

```python
# 像定类等级一样用条形图
art_ratings.value_counts().plot(kind='bar')
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.005.png)

此外，在定序等级还可以引入箱线图：

```python
# 定序等级也可以画箱线图
art_ratings.value_counts().plot(kind='box')
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.006.png)

不可能将之前的`Grade`列画成箱线图，因为找不到中位数。

### 2.3.3　定距等级

我们开始加大火力了。在定类和定序等级，我们一直在处理定性数据。即使其内容是数，也不代表真实的数量。在定距等级，我们摆脱了这个限制，开始研究定量数据。在定距等级，数值数据不仅可以像定序等级的数据一样排序，而且值之间的差异也有意义。这意味着，在定距等级，我们不仅可以对值进行排序和比较，而且可以**加减**。

例子：

定距等级的一个经典例子是温度。如果美国得克萨斯州的温度是32℃，阿拉斯加州的温度是4℃，那么可以计算出32 - 4 = 28℃的温差。这个例子看上去简单，但是回首之前的两个等级，我们从未对数据执行过这种操作。

反例：

一个经典的反例是李克特量表。因为可以排序，所以我们把李克特量表归为定序等级。但是需要注意的是，对其做减法并没有意义。如果在李克特量表上将5减去3，得出的结果2既不代表数字2，也不代表2这个类别。因此，李克特量表的减法很困难。

**可以执行的数学操作**

请记住，在定距等级上可以进行加减，这改变了整个游戏规则。既然可以把值加在一起，就能引入两个熟悉的概念：**算术平均数**（就是均值）和**标准差**。为了举例说明，我们引入一个新的数据集，它是关于气候变化的：

```python
# 加载数据集
climate = pd.read_csv('../data/GlobalLandTemperaturesByCity.csv')
climate.head()
```

为了更好地理解，我们看一下这个表格。

|      | dt         | AverageTemperature | AverageTemperatureUncertainty | City  | Country | Latitude | Longitude |
| :--- | :--------- | :----------------- | :---------------------------- | :---- | :------ | :------- | :-------- |
| 0    | 1743-11-01 | 6.068              | 1.737                         | Århus | Denmark | 57.05N   | 10.33E    |
| 1    | 1743-12-01 | NaN                | NaN                           | Århus | Denmark | 57.05N   | 10.33E    |
| 2    | 1744-01-01 | NaN                | NaN                           | Århus | Denmark | 57.05N   | 10.33E    |
| 3    | 1744-02-01 | NaN                | NaN                           | Århus | Denmark | 57.05N   | 10.33E    |
| 4    | 1744-03-01 | NaN                | NaN                           | Århus | Denmark | 57.05N   | 10.33E    |

这个数据集有860万行，每行代表某个城市某月的平均温度，上溯到18世纪。请注意，只看前5行，我们已经可以注意到有数据缺失了。把这些数据删除，美化一下结果：

```python
# 移除缺失值
climate.dropna(axis=0, inplace=True)

climate.head()  # 检查是否已移除干净
```

看下表会更容易理解。

|      | dt         | AverageTemperature | AverageTemperatureUncertainty | City  | Country | Latitude | Longitude |
| :--- | :--------- | :----------------- | :---------------------------- | :---- | :------ | :------- | :-------- |
| 0    | 1743-11-01 | 6.068              | 1.737                         | Århus | Denmark | 57.05N   | 10.33E    |
| 5    | 1744-04-01 | 5.788              | 3.624                         | Århus | Denmark | 57.05N   | 10.33E    |
| 6    | 1744-05-01 | 10.644             | 1.283                         | Århus | Denmark | 57.05N   | 10.33E    |
| 7    | 1744-06-01 | 14.051             | 1.347                         | Århus | Denmark | 57.05N   | 10.33E    |
| 8    | 1744-07-01 | 16.082             | 1.396                         | Århus | Denmark | 57.05N   | 10.33E    |

用这行代码检查缺失值：

```
climate.isnull().sum()

dt                               0
AverageTemperature               0
AverageTemperatureUncertainty    0
City                             0
Country                          0
Latitude                         0
Longitude                        0
dtype: int64

# 没有问题
```

我们关注的是`AverageTemperature`（平均温度）列。温度数据属于定距等级，这里不能使用条形图或饼图进行可视化，因为值太多了：

```
# 显示独特值的数量
climate['AverageTemperature'].nunique()

 111994
```

对111 994个值绘图非常奇怪，当然也没有必要，因为我们知道这些数是定量的。从这个级别开始，最常用的图是**直方图**。直方图是条形图的“近亲”，用不同的桶包含不同的数据，对数据的频率进行可视化。

对世界平均温度画一个直方图，从整体的角度看温度分布：

```
climate['AverageTemperature'].hist()
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.007.png)

可以看到，平均温度约为20℃。下面确认一下：

```
climate['AverageTemperature'].describe()

count    8.235082e+06
mean     1.672743e+01
std      1.035344e+01
min     -4.270400e+01
25%      1.029900e+01
50%      1.883100e+01
75%      2.521000e+01
max      3.965100e+01
Name: AverageTemperature, dtype: float64
```

很接近，均值大概是17℃。我们继续处理数据，加入`year`（年）和`century`（世纪）两列，只观察美国的数据：

```
# 将dt栏转换为日期，取年份
climate['dt'] = pd.to_datetime(climate['dt'])
climate['year'] = climate['dt'].map(lambda value: value.year)

# 只看美国
climate_sub_us = climate.loc[climate['Country'] == 'United States']

climate_sub_us['century'] = climate_sub_us['year'].map(lambda x: int(x/100+1))
# 1983变成20
# 1750变成18
```

我们用新的`century`列，对每个世纪画直方图：

```
climate_sub_us['AverageTemperature'].hist(by=climate_sub_us['century'],
 sharex=True, sharey=True,
 figsize=(10, 10),
 bins=20)
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.008.png)

这4幅直方图显示`AverageTemperature`随时间略微上升。确认一下：

```
climate_sub_us.groupby('century')['AverageTemperature'].mean().plot(kind='line')
```

以上代码的结果如下图所示。

![{%}](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.009.png)

有意思！因为差值在这个等级是有意义的，所以我们可以回答美国从18世纪至今平均温度上升多少这个问题。先把随世纪变化的温度数据存储到Pandas的Series对象中：

```python
century_changes =
climate_sub_us.groupby('century')['AverageTemperature'].mean()

century_changes

century
18    12.073243
19    13.662870
20    14.386622
21    15.197692
Name: AverageTemperature, dtype: float64
```

现在可以对这个Series进行切片，用21世纪的数据减去18世纪的数据，得到温差：

```python
# 21世纪的平均温度减去18世纪的平均温度
century_changes[21] - century_changes[18]

# 均值是21世纪的月平均温度减去18世纪的月平均温度
3.124449115460754
```

- **在定距等级绘制两列数据**

定距及更高等级的一大好处是，我们可以使用散点图：在两个轴上绘制两列数据，将数据点可视化为图像中真正的点。在气候变化数据集中，`year`和`averageTemperature`列都属于定距等级，因为它们的差值是有意义的。因此可以对美国每月的温度绘制散点图，其中![x](https://private.codecogs.com/gif.latex?x)轴是年份，![y](https://private.codecogs.com/gif.latex?y)轴是温度。我们希望可以看见之前折线图表示的升温趋势：

```
x = climate_sub_us['year']
y = climate_sub_us['AverageTemperature']
fig, ax = plt.subplots(figsize=(10,5))
ax.scatter(x, y)
plt.show()
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.010.png)

好像不怎么好看。和预期一样，里面有很多噪声。考虑到每年每个城镇都会报告好几个平均气温，在图上每年有很多点也是理所应当的。

我们用`groupby`清除年份的大部分噪声：

```python
# 用groupby清除美国气温的噪声
climate_sub_us.groupby('year').mean()['AverageTemperature'].plot()
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.011.png)

好多了！可以看出气温随年份上升的趋势，但是可以再用滑动均值（rolling mean）平滑一下：

```python
# 用滑动均值平滑图像
climate_sub_us.groupby('year').mean()['AverageTemperature'].rolling(10).mean().plot()
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.012.png)

我们在定距等级同时绘制两列数据，重新确认了之前用折线图表示的内容：美国的平均气温总体的确有上升的趋势。

数据的定距等级为我们提供了全新的理解方式，但是还没有结束。

### 2.3.4　定比等级

最终，我们到达了最高的等级：定比等级。在这个等级上，可以说我们拥有最高程度的控制和数学运算能力。和定距等级一样，我们在定比等级上处理的也是定量数据。这里不仅继承了定距等级的加减运算，而且有了一个**绝对零点**的概念，可以做乘除运算。

**可以执行的数学操作**

在定比等级，我们可以进行乘除运算。虽然看起来没什么大不了，但是这些运算可以让我们对这个等级上的数据进行独特的观察，而这在低等级上是无法做到的。我们先看几个例子，了解一下这意味着什么。

例子：

当处理金融数据时，我们几乎肯定要计算一些货币的值。货币处于定比等级，因为“零资金”这个概念可以存在。那么我们就可以说：

- $100是$50的**两倍**，因为100 / 50 = 2；
- 10 mg青霉素是20 mg青霉素的**一半**，因为10 / 20 = 0.5。

因为存在0这个概念，所以这种比较是有意义的。

反例：

我们一般认为，温度属于定距等级，而不是定比等级，因为100℃比50℃高两倍这种说法没有意义，并不合理。温度是主观的，不是客观正确的。

> ![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/info.png)　有人会说摄氏度和华氏度都有一个起始点，因为这两个单位都可以转换为开尔文，而开尔文有零点。实际上，摄氏度和华氏度都允许负值存在，但是开尔文不允许。因此，摄氏度和华氏度都没有真正的**零点**，但是开尔文有。

回到旧金山的工资数据，可以看到`Biweekly High Rate`列处于定比等级，因而可以进行新的观察。先看一下最高的工资：

```python
# 哪个工作种类的工资最高
# 每个工作种类的平均工资是多少
fig = plt.figure(figsize=(15,5))
ax = fig.gca()

salary_ranges.groupby('Grade')[['Biweekly High Rate']].mean().sort_values(
 'Biweekly High Rate', ascending=False).head(20).plot.bar(stacked=False, ax=ax, color='darkorange')
ax.set_title('Top 20 Grade by Mean Biweekly High Rate')
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.013.png)

如果看一下旧金山的最高工资记录：

http://sfdhr.org/sites/default/files/documents/Classification-and-Compensation/Archives/Compensation-Manual-FY09-10.pdf **2**

**2**感谢旧金山政府人力资源部的HR分析师Eliot Watt对链接修正提供的帮助。

会发现，工资最高的是**公共交通部总经理**（General Manager, Public Transportation Dept.）。我们用同样的办法查看工资最低的工作：

```python
# 哪个工作种类的工资最低
fig = plt.figure(figsize=(15,5))
ax = fig.gca()

salary_ranges.groupby('Grade')[['Biweekly High Rate']].mean().sort_values(
 'Biweekly High Rate', ascending=False).tail(20).plot.bar(stacked=False, ax=ax, color='darkorange')
ax.set_title('Bottom 20 Grade by Mean Biweekly High Rate')
```

以上代码的结果如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.014.png)

对照可知，工资最低的是**集会助理**（Camp Assistant）。

因为金钱处于定比等级，所以可以计算最高工资和最低工资的比值：

```python
sorted_df = salary_ranges.groupby('Grade')[['Biweekly High Rate']].mean().sort_values(
 'Biweekly High Rate', ascending=False)
sorted_df.iloc[0][0] / sorted_df.iloc[-1][0]

13.931919540229886
```

工资最高的员工比工资最低的员工多赚近13倍。多亏了定比等级，我们才能知道这件事情！

## 2.4　数据等级总结

理解数据的不同等级对于特征工程是非常必要的。当需要构建新特征或修复旧特征时，我们必须有办法确定如何处理每一列。

下表言简意赅地总结了每个等级上可行与不可行的操作。

| 等级 | 属性                                                         | 例子                               | 描述性统计                   | 图表                             |
| :--- | :----------------------------------------------------------- | :--------------------------------- | :--------------------------- | :------------------------------- |
| 定类 | 离散 无序                                                    | 二元响应（真或假） 人名 油漆颜色   | 频率/占比 众数               | 条形图 饼图                      |
| 定序 | 有序类别 比较                                                | 李克特量表 考试等级                | 频率 众数 中位数 百分位数    | 条形图 饼图 茎叶图               |
| 定距 | 数字差别有意义                                               | 摄氏度/华氏度 某些特殊的李克特量表 | 频率 众数 中位数 均值 标准差 | 条形图 饼图 茎叶图 箱线图 直方图 |
| 定比 | 连续 存在有意义的绝对零点，可以做除法（例如，$100是$50的两倍） | 金钱 重量                          | 均值 标准差                  | 直方图 箱线图                    |

下表展示了每个等级上可行与不可行的统计类型。

| 统计量               | 定类 | 定序 | 定距 | 定比     |
| :------------------- | :--- | :--- | :--- | :------- |
| 众数                 | √    | √    | √    | 有时可行 |
| 中位数               | ×    | √    | √    | √        |
| 差值、最小值、最大值 | ×    | √    | √    | √        |
| 均值                 | ×    | ×    | √    | √        |
| 标准差               | ×    | ×    | √    | √        |

最后这张表显示了每个等级上可以或不可以绘制的图表。

| 图表        | 定类 | 定序 | 定距     | 定比 |
| :---------- | :--- | :--- | :------- | :--- |
| 条形图/饼图 | √    | √    | 有时可以 | ×    |
| 茎叶图      | ×    | √    | √        | √    |
| 箱线图      | ×    | √    | √        | √    |
| 直方图      | ×    | ×    | 有时可以 | √    |

当你拿到一个新的数据集时，下面是基本的工作流程。

(1) 数据有没有组织？数据是以表格形式存在、有不同的行列，还是以非结构化的文本格式存在？

(2) 每列的数据是定量的还是定性的？单元格中的数代表的是数值还是字符串？

(3) 每列处于哪个等级？是定类、定序、定距，还是定比？

(4) 我可以用什么图表？条形图、饼图、茎叶图、箱线图、直方图，还是其他？

下图是对以上逻辑的可视化。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/03.d02z.015.png)

## 2.5　小结

了解我们要处理的特征是特征工程的基础。如果不理解拿到的数据，就不可能修复、创建和利用特征，不可能创建性能良好的机器学习流水线。本章中，我们可以在数据集中识别并提取不同等级的数据，并用这些信息创造有用、有意义的可视化图表，帮助我们进一步理解数据。

在下一章中，我们会利用有关数据等级的新知识来改进特征，并使用机器学习有效地衡量特征工程流水线的效果。