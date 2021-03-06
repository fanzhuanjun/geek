# Ch1. 特征工程简介

近年来，工程师和管理层都在尝试用**机器学习**（ML，machine learning）和**人工智能**（AI，artificial intelligence）来解决以往需要手动操作才能处理的问题。**自然语言处理**（NLP，natural language processing）的发展就是个很好的例子，特别是在自然语言生成和理解方面。更精确地说，我们希望构建一个AI系统，从用户（例如对最新款智能手机不满的用户）那里直接读取原始文本，以机器的速度和人类的措辞来流畅、准确地回复。本章会介绍以下有关特征工程的主题：

- 几个激动人心的例子，解释为什么特征工程至关重要；
- 对机器学习的基本理解，包括性能和评估方法；
- 本书各章的详细信息。

## 1.1　激动人心的例子：AI驱动的聊天

我们的AI聊天系统Arty可以像人类员工一样回复客户支持请求。Arty了解我们公司产品，可以随时提供服务。

下面是人与AI客服系统的一段对话。

| 人类                     | AI                                                   |
| :----------------------- | :--------------------------------------------------- |
| 你好，我的手机坏了。     | 抱歉给您带来了不便，请问您的手机是怎么坏的？         |
| 手机死机了，我没法重启。 | 您的手机是什么型号的？                               |
| 新款iDroid 28            | 啊，知道了。按住电源键和音量减键20秒，手机就重启了。 |
| 可以了，谢谢！           | 不客气，祝您生活愉快。                               |

这种系统令人兴奋，足以撼动市场，因为如此复杂的系统竟然可以十分简洁。让我们仔细分析一下。从表面上看，你有可能觉得，**这问题很简单啊！**提问很简单，回答也很简单，只是接收一个请求，给出一个回复。**“您好，我的手机死机了，应该怎么办？”**很简单，重启就好了。当然，表面上看起来一定是这样的。

```
from Arty import AI
AI.respond_to("my phone froze, what should I do?")
>> "reset it."
```

问题的难点在于要从AI的角度看问题。AI没有完整的人类经验，它既没读过古希腊史诗《伊利亚特》，也没看过儿童故事书《大红狗克里弗》，没办法消化信息。核心问题就是，AI没有什么阅读的经验。人们给这个AI几十万份（乃至几百万份）之前的人类聊天日志，让其从中发现规律。

上文中AI系统的训练数据节选如下。

| 请求                          | 回复                                 |
| :---------------------------- | :----------------------------------- |
| 你哈哦                        | 您好，请问您需要什么帮助？           |
| 我手机坏了！！！！！！        | 天啊！！！！怎么了？                 |
| >等一下，我去遛狗。马上回来。 | 好。我等你。                         |
| 嗨                            | 您好，我是Mark，请问您需要什么帮助？ |

数据分为两列，**请求**表示最终用户输入客服聊天框的内容，**回复**则表示客服对所收到消息的回复。

在读过数千条包含错别字、脏话和中途掉线的聊天记录后，AI开始认为自己可以胜任客服工作了。于是，人类开始让AI处理新收到的消息。虽然人类没有意识到自己的错误，但是开始注意到AI还没有完全掌握这项本领。AI连最简单的消息都识别不了，返回的消息也没有意义。人类很容易觉得AI只是需要更多的时间和更多的数据，但是这些解决方案只是更大问题的小修小补，而且很多时候根本不管用。

这个例子中的潜在问题很有可能是AI的原始输入数据太差，导致AI认识不到语言中的细微差别。例如，问题可能出在这些地方。

- 错别字会无故扩大AI的单词量。“你哈哦”和“你好”是两个无关的词。
- AI不能理解同义词。用来打招呼的“你好”和“嗨”字面上看起来毫不相似，人为地增加了问题的难度。

## 1.2　特征工程的重要性

为了解决实际问题，数据科学家和机器学习工程师要收集大量数据。因为他们想要解决的问题经常具有很高的相关性，而且是在混乱的世界中自然形成的，所以代表这些问题的原始数据有可能未经过滤，非常杂乱，甚至不完整。

因此，过去几年来，类似**数据工程师**的职位应运而生。这些工程师的唯一职责就是设计数据流水线和架构，用于处理原始数据，并将数据转换为公司其他部门——特别是数据科学家和机器学习工程师——可以使用的形式。尽管这项工作和机器学习专家构建机器学习流水线一样重要，但是经常被忽视和低估。

在数据科学家中进行的一项调查显示，他们工作中超过80%的时间都用在捕获、清洗和组织数据上。构造机器学习流水线所花费的时间不到20%，却占据着主导地位。此外，数据科学家的大部分时间都在准备数据。超过75%的人表示，准备数据是流程中最不愉快的部分。

上文提到的调查结果如下。

下图展示了数据科学家进行不同工作的时间比例。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/02.d01z.001.png)

从上图可见，数据科学家的工作占比如下。

- 设置训练集：3%
- 清洗和组织数据：60%
- 收集数据集：19%
- 挖掘数据模式：9%
- 调整算法：5%
- 其他：4%

下图展示了数据科学家最不喜欢的流程。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/02.d01z.002.png)

在一项类似的调查中，数据科学家认为他们最不喜欢的流程如下。

- 设置训练集：10%
- 清洗和组织数据：57%
- 收集数据集：21%
- 挖掘数据模式：3%
- 调整算法：4%
- 其他：5%

上面第一幅图表示了数据科学家在流程中的不同部分所花费的时间比例。数据科学家有超过80%的时间花在了准备数据上，以便进一步利用数据。第二幅图则表示了数据科学家最不喜欢的步骤。超过75%的人表示，他们最不喜欢准备数据。

> ![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/tip.png)　数据源：https://whatsthebigdata.com/2016/05/01/data-scientists-spend-most-of-their-time-cleaning-data/。

好的数据科学家不仅知道准备数据很重要，会占用大部分工作时间，而且知道这个步骤很艰难，没人喜欢。很多时候我们会觉得，像机器学习竞赛和学术文献中那样干净的数据是理所当然的。然而实际上，超过90%的数据（最有趣、最有用的数据）都以原始形式存在，就像在之前AI聊天系统的例子中一样。

**准备数据**的概念很模糊，包括捕获数据、存储数据、清洗数据，等等。之前的图中显示，清洗和组织数据占用的工作时间十分可观。数据工程师在这个步骤中能发挥最大作用。清洗数据的意思是将数据转换为云系统和数据库可以轻松识别的形式。组织数据一般更为彻底，经常包括将数据集的格式整体转换为更干净的格式，例如将原始聊天数据转换为有行列结构的表格。

**清洗数据**和**组织数据**的区别如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/02.d01z.003.png)

图片上半部分的转换代表清洗服务器日志，包含数据和服务器状态的描述文本。注意在清洗时，Unicode字符**&**被转换为了更可读的**&**。清洗前后，文档的格式基本保持不变。下半部分的组织转换则彻底得多，把原始数据转换为了行列结构，其中每行代表服务器的一次操作，每列代表服务器操作的属性（attribute）。在这个例子中，两个属性是**日期**和**文本**。

清洗和组织数据都属于更大的数据科学范畴，也是本书要讨论的主题——特征工程。

## 1.3　特征工程是什么

终于说到本书的主题了。

是的，本书的主题是特征工程。我们将着眼于清洗和组织数据的过程，为机器学习流水线服务。除了这些概念，我们还会介绍如何用数学公式和神经理解的方式看待数据转换，但是现在暂时不涉及。让我们从概念开始入手吧。

> ![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/info.png)　**特征工程**（feature engineering）是这样一个过程：将数据转换为能更好地表示潜在问题的特征，从而提高机器学习性能。

为了进一步理解这个定义，我们看看特征工程具体包含什么。

- **转换数据的过程**：注意这里并不特指原始数据或未过滤的数据，等等。特征工程适用于任何阶段的数据。通常，我们要将特征工程技术应用于在数据分发者眼中已经**处理过**的数据。还有很重要的一点是，我们要处理的数据经常是表格形式的。数据会被组织成行（观察值）和列（属性）。有时我们从最原始的数据形式开始入手，例如之前服务器日志的例子，但是大部分时间，要处理的数据都已经在一定程度上被清洗和组织过了。
- **特征**：显而易见，这个词在本书中会很常用。从最基本的层面来说，特征是对机器学习过程有意义的数据属性。我们经常需要查看表格，确定哪些列是特征，哪些只是普通的属性。
- **更好地表示潜在问题**：我们要使用的数据一定代表了某个领域的某个问题。我们要保证，在处理数据时，不能一叶障目不见泰山。转换数据的目的是要更好地表达更大的问题。
- **提高机器学习性能**：特征工程是数据科学流程的一部分。如我们所见，这个步骤很重要，而且经常被低估。特征工程的最终目的是让我们获取更好的数据，以便学习算法从中挖掘模式，取得更好的效果。本书稍后将详细讨论机器学习的指标和效果，但是现在我们要知道的是，执行特征工程不仅是要获得更干净的数据，而且最终要在机器学习流水线中使用这些数据。

你一定在想：**为什么我应该花时间阅读一本大家都不喜欢的事情的书？**我们觉得，很多人之所以不喜欢特征工程，是因为他们常常看不到这些工作的益处。

大部分公司会同时招聘数据工程师和机器学习工程师。数据工程师主要关注准备和转换数据，而机器学习工程师一般拥有算法知识，知道如何从清洗好的数据中挖掘出模式来。

这两种工作一般是分开的，但是会交织在一起循环进行。数据工程师把数据集交给机器学习工程师，机器学习工程师则会说结果不好，让数据工程师进一步转换数据，反反复复。这种过程不仅单调重复，而且影响大局。

如果工程师不具备特征工程和机器学习两方面的知识，则整个流程很有可能不会那么有效。因此本书应运而生。我们会讨论特征工程，以及特征工程和机器学习如何直接相关。这个方法是以结果为导向的，我们认为，只有能提高机器学习效果的技术才是有用的技术。现在我们来深入了解数据、数据结构和机器学习的基础知识，以确保术语的统一性。

### 数据和机器学习的基础知识

一般来说，我们处理的数据都是表格形式的，按行列组织。可以将其想象成能在电子表格程序（例如Microsoft Excel）中打开。数据的每行又称为**观察值**（observation），代表问题的一个实例或例子。例如，如果数据是关于股票日内交易的，那么每个观察值有可能是一小时内整体股市和股价的涨跌。

又例如，如果数据是关于网络安全的，那么观察值也许是可能的黑客攻击，或者是无线网络发送的一个数据包。

下表是网络安全领域的示例数据，确切地说是网络入侵领域。

| DateTime       | Protocol | Urgent | Malicious |
| :------------- | :------- | :----- | :-------- |
| June 2nd, 2018 | TCP      | FALSE  | TRUE      |
| June 2nd, 2018 | HTTP     | TRUE   | TRUE      |
| June 2nd, 2018 | HTTP     | TRUE   | FALSE     |
| June 3rd, 2018 | HTTP     | FALSE  | TRUE      |

可以看到，每行（每个观察值）都是一次网络连接，有4个属性：`DateTime`（日期）、`Protocol`（协议）、`Urgent`（紧急）和`Malicious`（恶意）。我们暂时不深入研究每个属性，先观察以表格形式给出的数据结构。

因为大部分数据都是表格形式的，也可以看看一种特殊的实例：数据只有一列（一个属性）。例如，我们要开发一个软件，输入房间的一张图像，它会输出房间中是否有人。输入的数据矩阵有可能只有一列——房间照片的链接（URL），别的什么都没有。

例如，下面的表格中只有一列，列标题是“照片URL”。表格中数据的值（这些URL仅为示例，并不指向真的图片）对数据科学家而言具有相关性。

| 照片URL                        |
| :----------------------------- |
| http://photo-storage.io/room/1 |
| http://photo-storage.io/room/2 |
| http://photo-storage.io/room/3 |
| http://photo-storage.io/room/4 |

输入的数据有可能只有一列，像这个例子一样。在创建图像分析系统时，输入有可能仅仅是图像的URL。作为数据科学家，我们要从这些URL中构建特征。

数据科学家要准备好接受并处理多或少、宽或窄（从特征上讲）、完整或稀疏（可能有缺失值）的数据，并准备好在机器学习中应用这些数据。现在是时候讨论机器学习了。机器学习算法是按其从数据中提取并利用模式、以基于历史训练数据完成任务的能力来定义的。是不是摸不到头脑？机器学习可以处理很多类型的任务，因此我们不给出定义，而是继续深入探讨。

大体上，我们把机器学习分为两类：监督学习和无监督学习。两种算法都可以从特征工程中获益，所以了解每种类型非常重要。

1. **监督学习**

   一般来说，我们都是在监督学习（也叫预测分析）的特定上下文中提到特征工程。监督学习算法专门处理预测一个值的任务，通常是用数据中的其他属性来预测余下的一个属性。以如下表示网络入侵的数据集为例。

   | DateTime       | Protocol | Urgent | Malicious |
   | :------------- | :------- | :----- | :-------- |
   | June 2nd, 2018 | TCP      | FALSE  | TRUE      |
   | June 2nd, 2018 | HTTP     | TRUE   | TRUE      |
   | June 2nd, 2018 | HTTP     | TRUE   | FALSE     |
   | June 3rd, 2018 | HTTP     | FALSE  | TRUE      |

   还是前文用到的数据集，这次我们在预测分析的上下文中深入探讨。

   注意，数据集有4个属性：`DateTime`、`Protocol`、`Urgent`和`Malicious`。假设`Malicious`属性包含代表该观测值是否为恶意入侵的值。所以在这个小数据集中，第1次、第2次和第4次连接都是恶意入侵。

   进一步假设，在这个数据集中，我们要尝试用3个属性（`DateTime`、`Protocol`和`Urgent`）准确预测`Malicious`属性。简单地说，我们想建立一个系统，将`DateTime`、`Protocol`和`Urgent`属性的值映射到`Malicious`的值。监督学习问题就是这样建立起来的：

   ```
   Network_features = pd.DataFrame({'datetime': ['6/2/2018', '6/2/2018',
   '6/2/2018', '6/3/2018'], 'protocol': ['tcp', 'http', 'http', 'http'],
   'urgent': [False, True, True, False]})
   Network_response = pd.Series([True, True, False, True])
   Network_features
   >>
    datetime protocol urgent
   0  6/2/2018      tcp  False
   1  6/2/2018     http   True
   2  6/2/2018     http   True
   3  6/3/2018     http  False
   Network_response
   >>
   0      True
   1      True
   2     False
   3      True
   dtype: bool
   ```

   在监督学习中，我们一般将数据集中希望预测的属性（一般只有一个，但也不尽然）叫作响应（response），其余属性叫作**特征**（feature）。

   也可以认为，监督学习是一种利用数据结构的算法。我们的意思是，机器学习算法会试图从很漂亮整洁的数据中提取模式。但是之前我们讨论过，不应该想当然地认为进入流水线的数据都是干净的：特征工程由此而来。

   你可能会问：如果我们不做预测，机器学习又有什么用呢？问得好。在机器学习可以利用数据结构之前，我们有时需要调整乃至创造结构。无监督学习在这里大放异彩。

2. **无监督学习**

   监督学习的目的是预测。我们利用数据的特征对响应进行预测，提供有用的信息。如果不是要通过探索结构进行预测，那就是想从数据中提取结构。要做到后者，一般对数据的数值矩阵或迭代过程应用数学变换，提取新的特征。

   这个概念有可能比监督学习更难理解，我们在此提供一个例子来阐明。

   - **无监督学习的例子：市场细分**

   假如我们的数据集很大（有100万行），每行是一个人的基本特征（年龄、性别等）以及购买商品的数量（代表从某个店铺购买的商品数）。

   | 年龄 | 性别 | 购买商品的数量 |
   | :--- | :--- | :------------- |
   | 25   | 女   | 1              |
   | 28   | 女   | 23             |
   | 61   | 女   | 3              |
   | 54   | 男   | 17             |
   | 51   | 男   | 8              |
   | 47   | 女   | 3              |
   | 27   | 男   | 22             |
   | 31   | 女   | 14             |

   这是营销数据集的一个样本，每行代表一个顾客，每人有3个基本属性。我们的目标是将这个数据集细分成不同的类型或**聚类**，让执行分析的公司更好地理解客户资料。

   这里只显示了100万行数据的前8行，全部数据令人望而生畏。我们当然可以对该数据集进行基本的描述性统计分析，例如计算所有数值列的均值和标准差等。不过，如果想把100万人划分为不同的**类型**，方便市场部门更好地理解不同的消费人群、为每类人更精准地投放广告呢？

   每种类型的顾客都有独一无二的特征。例如，有可能20%的顾客属于年轻富裕阶层，他们的年龄较小、买的商品数量较多。

   此类分析和类型的创建属于无监督学习的一个特殊类别，称作**聚类**，后文中将详细讨论这种机器学习算法。目前我们知道，聚类会创造一个新的特征，将顾客划分到不同类型或聚类中。

   | 年龄 | 性别 | 购买商品的数量 | 聚类 |
   | :--- | :--- | :------------- | :--- |
   | 25   | 女   | 1              | 6    |
   | 28   | 女   | 23             | 1    |
   | 61   | 女   | 3              | 3    |
   | 54   | 男   | 17             | 2    |
   | 51   | 男   | 8              | 3    |
   | 47   | 女   | 3              | 8    |
   | 27   | 男   | 22             | 5    |
   | 31   | 女   | 14             | 1    |

   以上是应用聚类算法后的数据集。注意在最后有一个新的**聚类**特征，表示这个算法认为此人属于哪个类型。我们的想法是，同一类型的人**行为**相似（年龄、性别和购买行为等相仿）。也许聚类6可以叫作**年轻消费者**。

   这个聚类的例子显示，我们不一定需要输出预测值，可以只是深入了解数据，添加有价值的新特征，甚至删除不相关的特征。

   > ![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/info.png)　注意，这里将所有的列都称为特征，因为无监督学习没有响应，我们没有做预测。

   现在是不是清楚一些了？我们反复讨论的特征就是本书的重点。特征工程包括理解并转换监督学习和无监督学习中的特征。

## 1.4　机器学习算法和特征工程的评估

注意，在文献中，**特征**和**属性**通常有明显的区分。**属性**一般是表格数据的列，**特征**则一般只指代对机器学习算法有益的属性。也就是说，某些属性对机器学习系统不一定有益，甚至有害。例如，当预测二手车下次维修的时间时，车的颜色应该不会对预测有什么帮助。

本书中，我们一般将所有的列都称为特征，直到证明某些列是无用或有害的。之后，我们会用代码将这些属性抛弃。那么，对这种决定做出评估就是至关重要的。如何评估机器学习系统和特征工程呢？

### 1.4.1　特征工程的例子：真的有人能预测天气吗

考虑一个用于预测天气的机器学习流水线。为简化起见，假设我们的算法直接从传感器获取大气数据，并预测两个值之一：**晴天**或**雨天**。很明显，这条流水线是分类流水线，只能输出两个答案中的一个。我们每天早上运行这个流水线。如果算法输出**晴天**而且这天基本是晴朗的，则算法正确；同理，如果输出**雨天**而且这天下雨了，那么算法也是正确的。对于其他任何情况，输出都是错的。我们在一个月的每一天都运行算法，这样会收集差不多30个预测值和实际观测到的天气值。然后就可以计算出算法的准确率。也许算法在30天内正确预测了20次，那么准确率是三分之二，大约为67%。利用这个标准化的值或准确率，我们可以调整算法，观察准确率上升还是下降。

当然，这个例子过度简化了，但是思路很明确：对于任何机器学习流水线而言，如果不能使用一套标准指标评估其性能，那么它就是没用的。因此，特征工程不可能没有评估过程。本书将多次审视这种思路，但是目前先简单谈一下，如何进行该操作。

关于特征工程的话题一般涉及转换数据集（根据特征工程的定义）。为了明确定义某一特征工程是否对机器学习算法有利，我们会采用下节中的步骤。

### 1.4.2　特征工程的评估步骤

以下是评估特征工程的步骤：

(1) 在应用任何特征工程之前，得到机器学习模型的基准性能；

(2) 应用一种或多种特征工程；

(3) 对于每种特征工程，获取一个性能指标，并与基准性能进行对比；

(4) 如果性能的增量（变化）大于某个阈值（一般由我们定义），则认为这种特征工程是有益的，并在机器学习流水线上应用；

(5) 性能的改变一般以百分比计算（如果基准性能从40%的准确率提升到76%的准确率，那么改变是90%）。

性能的定义随算法不同而改变。大部分优秀的主流机器学习算法会告诉你，在数据科学的实践中有数十种公认的指标。

因为本书的重点并不在于机器学习，而是理解和转换特征，所以我们会在例子中用机器学习算法的基准性能评估特征工程。

### 1.4.3　评估监督学习算法

当进行预测建模（即**监督学习**）时，性能直接与模型利用数据结构的能力，以及使用数据结构进行恰当预测的能力有关。一般而言，可以将监督学习分为两种更具体的类型：**分类**（预测定性响应）和**回归**（预测定量响应）。

评估分类问题时，直接用5折交叉验证计算逻辑回归模型的准确率：

```
# 评估分类问题的例子
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
X = some_data_in_tabular_format
y = response_variable
lr = LinearRegression()
scores = cross_val_score(lr, X, y, cv=5, scoring='accuracy')
scores
>> [.765, .67, .8, .62, .99]
```

与之类似，对于回归问题，我们用线性回归的**均方误差**（MSE，mean squared error）进行评估，同样使用5折交叉验证：

```
# 评估回归问题的例子
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
X = some_data_in_tabular_format
y = response_variable
lr = LinearRegression()
scores = cross_val_score(lr, X, y, cv=5, scoring='mean_squared_error')
scores
>> [31.543, 29.5433, 32.543, 32.43, 27.5432]
```

我们用这两个线性模型，而不是出于速度和低方差的考虑使用更新、更高级的模型。这样可以更加确定，性能的增长直接与特征工程相关，而不是因为模型可以发现隐藏的模式。

### 1.4.4　评估无监督学习算法

这个问题比较棘手。因为无监督学习不做出预测，所以不能直接根据模型预测的准确率进行评估。尽管如此，如果我们进行了聚类分析（例如之前的市场细分例子），通常会利用**轮廓系数**（silhouette coefficient，这是一个表示聚类分离性的变量，在-1和1之间）加上一些人工分析来确定特征工程是提升了性能还是在浪费时间。

下面的例子用Python和scikit-learn导入并计算了一些假数据的轮廓系数：

```
attributes = tabular_data
cluster_labels = outputted_labels_from_clustering

from sklearn.metrics import silhouette_score
silhouette_score(attributes, cluster_labels)
```

随着讨论的深入，后面会花更多时间讨论无监督学习。不过大部分例子会围绕预测分析/监督学习展开。

> ![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/tip.png)　需要记住，之所以对评估的算法和指标进行标准化，是因为要展示特征工程的强大，而且要让你成功复现我们的过程。实践中，你优化的性能有可能不是准确率，例如真阳性率（true positive rate），想用决策树而不是逻辑回归。这样很好，我们鼓励这样做。始终记住，要按步骤评估特征工程的结果，并将特征工程后的结果与基准性能进行对比。

你阅读本书的目的可能并不是提高机器学习性能。特征工程在其他领域（例如假设检验和一般的统计）中也非常有用。在本书的几个例子中，我们会研究将特征工程和数据转换应用于各种统计检验的统计显著性上。我们也会探索![R^2](https://private.codecogs.com/gif.latex?R^2)和![p](https://private.codecogs.com/gif.latex?p)值等指标，以帮助判断特征工程是否有益。

大体上，我们会在3个领域内对特征工程的好处进行量化。

- 监督学习

  ：也叫

  预测分析

  - 回归——预测

    定量

    数据

    - 主要使用均方误差作为测量指标

  - 分类——预测

    定性

    数据

    - 主要使用准确率作为测量指标

- 无监督学习

  ：聚类——将数据按特征行为进行分类

  - 主要用轮廓系数作为测量指标

- **统计检验**：用相关系数、![t](https://private.codecogs.com/gif.latex?t)检验、卡方检验，以及其他方法评估并量化原始数据和转换后数据的效果

在下面几节中，我们会讨论一下本书要覆盖的内容。

## 1.5　特征理解：我的数据集里有什么

这一章着手为数据处理打下基础。理解了我们面前的数据，就可以更好地明确下一步的方向。我们会开始探索不同类型的数据，并且学习如何识别数据集中的数据类型。我们会从不同的视角研究数据集，确定它们之间的异同。可以轻松地检查数据并识别不同属性的特点之后，就能开始理解不同的数据转换方法，并用其改进我们的机器学习算法了。

在繁杂的切入点中，我们将着眼于以下几个方面：

- 结构化数据与非结构化数据；
- 数据的4个等级；
- 识别数据的缺失值；
- 探索性数据分析；
- 描述性统计；
- 数据可视化。

我们从理解最基本的数据结构入手，然后研究不同的数据种类。在理解数据后，就可以开始修正有问题的数据了。例如，我们必须知道数据中有多少缺失值，以及如何处理。

毫无疑问，数据可视化、描述性统计和探索性数据分析都是特征工程的一部分。我们会从机器学习工程师的角度研究这些过程。每个过程都可以增强机器学习流水线，我们会用它们试验并修正对数据的假设。

## 1.6　特征增强：清洗数据

在这一章中，我们会用自己对数据的理解，对数据集进行清洗。本书的大部分内容都会按此流程进行，用前面章节的结果处理后面章节的内容。在特征增强这步，我们可以开始利用对数据的理解修改数据集。我们会使用数学变换增强给定的数据，但是并不删除或插入新的属性（这些内容在之后几章涉及）。

我们探索的主题包括以下这些。

- 对非结构化数据进行结构化。
- 数据填充——在原先没有数据的位置填充（缺失）数据。
- 数据归一化：
  - 标准化（也称为![z](https://private.codecogs.com/gif.latex?z)分数标准化）；
  - 极差法（也称为min-max标准化）；
  - L1和L2正则化（将数据投影到不同的空间，很有趣）。

此时，我们将可以判断数据是否有**结构**。也就是说，我们的数据是否是漂亮的表格格式。如果不是，这一章将提供将数据表格化的工具。在创建机器学习流水线时，这一步必不可少。

数据填充是个特别有趣的话题。在数据中填充缺失的部分比听起来要困难得多。我们会从最简单的方式（把有缺失值的特征删掉）讲到更有趣也更复杂的方式（在其他特征上进行机器学习，填充缺失值）。在填充大量缺失值后，就可以测量缺失值对机器学习算法的影响了。

归一化是用（一般比较简单的）数学工具改变数据的缩放比例。还是一样，这可以很简单，例如将英里转换为英尺、将磅转换为千克；也可以很复杂，例如将数据投影到单位球体上（到时候会详细介绍）。

在这一章和之后的章节中，我们会更加关注特征工程的量化评估流程。基本上，每当遇见一个新的数据集或特征工程，都要进行测试。我们会根据不同的标准为各种特征工程方法打分，例如机器学习的性能、速度，等等。这一章的流程仅供参考，并不能作为指南，因为不能在忽略难度和性能的情况下选择特征工程方法。每个数据任务都有自己的注意事项，需要的流程可能和先前的不同。

## 1.7　特征选择：对坏属性说不

到了这一章，我们在处理新数据集时已经比较得心应手了。我们有能力理解并清洗任何数据。此后，就可以做一些重大决策了，例如，**属性在何种程度上才能成为真正的特征**。注意特征和属性的区别，这里真正的意思是：**哪些列对我们的机器学习流水线没有帮助而且有害，应该移除掉？**这一章着重介绍如何决定删除数据集中的哪些属性。我们会研究几个有助于我们做决定的统计和迭代过程。

这些过程包括：

- 相关系数；
- 识别并移除多重共线性；
- 卡方检验；
- 方差分析；
- 理解![p](https://private.codecogs.com/gif.latex?p)值；
- 迭代特征选择；
- 用机器学习测量熵和信息增益。

上述所有过程都会建议删除某些特征，并给出不同的理由。最后，数据科学家要最终决定保留哪些能为机器学习算法做出贡献的特征。

## 1.8　特征构建：能生成新特征吗

在前几章中，我们主要关注移除对机器学习流水线不利的特征；这一章则着眼于构建全新的特征，并将其正确地插入数据集。我们希望这些新特征可以更好地保存新信息，并生成新的模式供机器学习流水线使用、提高其性能。

我们要构建的特征可以有很多来源。通常，我们用现有的特征构建新特征。可以对现有特征进行转换，将结果向量和原向量放置在一起。我们还会研究从其他的系统中引入特征。例如，如果处理数据的目的是要基于购物行为对顾客群进行聚类，加入人口普查数据（这些数据不在企业的购物数据中）就有可能对结果有利。然而这样会带来如下几个问题。

- 如果普查数据中有1700个无名氏，但是企业只知道其中13个人的购物数据，那么如何从1700人里找到这13个人？这叫作**实体匹配**（entity matching）。
- 人口普查数据很大，实体匹配有可能极度耗时。

除此之外，还会有其他问题增加这个步骤的难度，但是也经常会创造出一个非常密集、数据丰富的环境。

在这一章中，我们会花时间讨论如何通过高度非结构化的数据手动创建特征。文本和图像是其中的两个例子。因为机器学习和人工智能流水线无法理解这些数据本身，所以需要手动创建可以代表图像或文本的特征。举一个简单的例子，假设我们要编写自动驾驶汽车的基础代码。首先要做的就是创建一个模型，接收汽车前方的图像来决定是否应该刹车。直接输入原始图像的办法不够好，因为机器学习算法不知道如何处理图像。我们必须手动构建特征。可以用以下几种方法分割原始图像。

- 考虑像素的颜色强度，将每个像素作为一个特征：

  - 例如，如果车载摄像头的分辨率是2048像素 × 1536像素，那么会有3 145 728列

- 将每行像素视为一个特征，将每行的平均颜色作为值：

  - 这样只有1536列 *

- 将图像投影到某个空间中，其中每个特征代表图像中的一个对象。这个办法是最困难的，结果可能如下：

  | 停车标志 | 猫   | 天空 | 道路 | 草地 | 潜水艇 |
  | :------- | :--- | :--- | :--- | :--- | :----- |
  | 1        | 0    | 1    | 1    | 4    | 0      |

  在上表中，特征是有可能存在或不存在于图像中的对象，值代表该对象出现的次数。如果模型收到这样的信息，就最好要停车了！

## 1.9　特征转换：数学显神通

我们会在这一章接触一些有趣的数学知识。我们已经讨论了如何理解并清洗特征，也研究了如何移除或增加特征。在特征构建那一章，我们需要手动构建新的特征。在之前自动驾驶的例子中，我们必须用人脑想出3种解构停车标志的方法。固然可以写代码把这个流程自动化，但是最终还是需要人工决策。

这一章将开始着眼于自动创建特征，因为这些特征适用于数学维度。如果把数据理解为一个![n](https://private.codecogs.com/gif.latex?n)维空间中的向量（![n](https://private.codecogs.com/gif.latex?n)是列数），那么我们可以考虑，**能不能创建一个![\boldsymbol{k}](https://private.codecogs.com/gif.latex?\boldsymbol{k})维（![\boldsymbol{k<n}](https://private.codecogs.com/gif.latex?\boldsymbol{k%3Cn})）的子集，完全或几乎完全表示原数据，从而提升机器学习速度或性能？**这里的目标是，创建一个维度更低、比原有高维度数据集性能更好的数据集。

第一个问题是，**我们做特征选择的时候不就是在降维吗？假如原来的数据有17个特征，我们删除5个，就把数据的维度降到12了，是不是？**没错，当然是！但是这里不是简单地讨论删除一些列，而是对数据集应用复杂的数学变换（一般从线性代数中寻求灵感）。

一个值得注意的例子是主成分分析（PCA，principal component analysis），我们会花一些时间深入探讨。这种转换将数据分成3个完全不同的数据集，然后可以用这些结果创造全新的数据集，让其性能超过原先的数据集！

下面的这个例子来自普林斯顿大学的研究实验，用PCA探究基因表达的模式。这是对降维的一个绝佳应用，因为基因和基因组合极多，即使是世界上最精巧的算法也需要很长时间才能处理。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/02.d01z.004.png)

上图中，![\boldsymbol{A}](https://private.codecogs.com/gif.latex?\boldsymbol{A})代表原始数据集，![\boldsymbol{U}](https://private.codecogs.com/gif.latex?\boldsymbol{U})、![\boldsymbol{W}](https://private.codecogs.com/gif.latex?\boldsymbol{W})和![\boldsymbol{V^T}](https://private.codecogs.com/gif.latex?\boldsymbol{V^T})代表奇异值分解的结果。然后将结果放在一起，创造一个新的数据集，在一定程度上替代![\boldsymbol{A}](https://private.codecogs.com/gif.latex?\boldsymbol{A})。

## 1.10　特征学习：以AI促AI

该领域顶层的研究是，用目前最精巧的算法自动构建特征，以改善机器学习和AI流水线。

前面的自动特征创建是用数学公式处理数据，但最终还是要让人类选择公式并从中获益。这一章概述的算法不是数学公式，而是尝试对数据进行理解和建模的一种架构，从而发掘数据的模式并创建新数据。这个描述目前可能比较模糊，但是希望你已经心动了！

我们会主要关注基于神经网络（节点和权重）的算法。这些算法在数据上增加的特征虽然有时不为人类所理解，但是机器会大受裨益。这章的主题包括：

- 受限玻尔兹曼机（RBM，restricted Boltzmann machine）；
- Word2vec/GloVe等词嵌入（word embedding）算法**1**。

**1**词嵌入算法的意思是用向量表示每个单词，聚类的结果中相似单词的距离会较近，不同的单词则会分开。——译者注

Word2vec和GloVe算法可以将高维度数据嵌入文本的词项（token）中。例如，Word2vec算法的可视化结果可能如下图所示。

![img](http://www.ituring.com.cn/figures/2019/FeatureEngineering/02.d01z.005.png)

在欧几里得空间中将单词表示为向量后，就可以得到数学样式的结果。在上面的例子中，加入自动生成的特征后，可以在Word2vec算法的帮助下通过计算单词的向量表示来对单词进行**加减**。然后可以得到有趣的结论，例如**国王 - 男 + 女 = 女王**。厉害！

## 1.11　小结

特征工程是数据科学家和机器学习工程师需要承担的一项重大任务。这项任务对于成功的、可以投入生产的机器学习流水线而言必不可少。在接下来的7章中，我们将讨论特征工程的6个主要方面。

- 特征理解：学习如何识别定量数据和定性数据。
- 特征增强：清洗和填充缺失值，最大化数据集的价值。
- 特征选择：通过统计方法选择一部分特征，以减少数据噪声。
- 特征构建：构建新的特征，探索特征间的联系。
- 特征转换：提取数据中的隐藏结构，用数学方法转换数据集、增强效果。
- 特征学习：利用深度学习的力量，以全新的视角看待数据，从而揭示新的问题，并予以解决。

本书将探索特征工程，因为特征工程会影响到机器学习的结果。在将特征工程这个大主题分为子主题，并在每章深入讨论一个主题后，我们可以更加深入地理解这些过程的原理，以及如何在Python中加以应用。

在下一章中，我们会直接介绍第一个主题**特征理解**。终于可以开始处理真实数据了，现在就来吧！