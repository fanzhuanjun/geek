- 聚类

    目标是将相似的实例分组到集群中。聚类是很好的工具，用于数据分析、客户细分、推荐系统、搜索引擎、图像分割、半监督学习、降维等。
    
- 异常检测

    目的是学习“正常”数据看起来是什么样的，然后将其用于检测异常情况，例如生产线上的缺陷产品或时间序列中的新趋势。
    
- 密度估算


```
import numpy as np
import os
np.random.seed(42)
import matplotlib.pyplot as plt
```


```
plt.rcParams['savefig.dpi'] = 100 #图片像素
plt.rcParams['figure.dpi'] = 100 #分辨率
```

# 1. 聚类


```
from sklearn.datasets import load_iris
```


```
data = load_iris()
X = data.data
y = data.target
data.target_names
```




    array(['setosa', 'versicolor', 'virginica'], dtype='<U10')



## 1.1 原始数据分类


```
plt.figure(figsize=(9, 3.5))

plt.subplot(121)
plt.plot(X[y==0, 2], X[y==0, 3], "yo", label="Iris setosa")
plt.plot(X[y==1, 2], X[y==1, 3], "bs", label="Iris versicolor")
plt.plot(X[y==2, 2], X[y==2, 3], "g^", label="Iris virginica")
plt.xlabel("Petal length", fontsize=14)
plt.ylabel("Petal width", fontsize=14)
plt.legend(fontsize=12)

plt.subplot(122)
plt.scatter(X[:, 2], X[:, 3], c='k', marker='.')
plt.xlabel("Petal length", fontsize=14)
plt.tick_params(labelleft=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_7_0.png)


## 1.2 通过高斯混合聚类


```
from sklearn.mixture import GaussianMixture
```


```
y_pred = GaussianMixture(n_components=3, random_state=42).fit(X).predict(X)

# from sklearn.cluster import KMeans
# y_pred = KMeans(n_clusters=3, random_state=42).fit(X).predict(X)
```


```
y_pred
```




    array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=int64)




```
from scipy import stats

mapping = {}
for class_id in np.unique(y):
    mode, _ = stats.mode(y_pred[y==class_id])
    mapping[mode[0]] = class_id

mapping
```




    {2: 0, 0: 1, 1: 2}




```
y_pred = np.array([mapping[cluster_id] for cluster_id in y_pred])
y_pred
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])




```
plt.plot(X[y_pred==0, 2], X[y_pred==0, 3], "yo", label="Iris setosa")
plt.plot(X[y_pred==1, 2], X[y_pred==1, 3], "bs", label="Iris versicolor")
plt.plot(X[y_pred==2, 2], X[y_pred==2, 3], "g^", label="Iris virginica")
plt.xlabel("Petal length", fontsize=14)
plt.ylabel("Petal width", fontsize=14)
plt.legend(fontsize=12)
```




    <matplotlib.legend.Legend at 0x27331feaeb0>




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_14_1.png)



```
np.sum(y_pred==y)
```




    145




```
np.sum(y_pred==y) / len(y)
```




    0.9666666666666667



## 1.3 K-Means


```
from sklearn.datasets import make_blobs
```


```
blob_centers = np.array(
    [[ 0.2,  2.3],
     [-1.5 ,  2.3],
     [-2.8,  1.8],
     [-2.8,  2.8],
     [-2.8,  1.3]])
blob_std = np.array([0.4, 0.3, 0.1, 0.1, 0.1])
```


```
X, y = make_blobs(n_samples=2000, centers=blob_centers,
                  cluster_std=blob_std, random_state=7)
```


```
def plot_clusters(X, y=None):
    plt.scatter(X[:, 0], X[:, 1], c=y, s=1)
    plt.xlabel("$x_1$", fontsize=14)
    plt.ylabel("$x_2$", fontsize=14, rotation=0)
```


```
plt.figure(figsize=(8, 4))
plot_clusters(X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_22_0.png)



```
from sklearn.cluster import KMeans
```


```
k = 5
kmeans = KMeans(n_clusters=k, random_state=42)
y_pred = kmeans.fit_predict(X)
```


```
y_pred
```




    array([0, 4, 1, ..., 2, 1, 4])




```
y_pred is kmeans.labels_
```




    True



模型的中心


```
kmeans.cluster_centers_
```




    array([[-2.80037642,  1.30082566],
           [ 0.20876306,  2.25551336],
           [-2.79290307,  2.79641063],
           [-1.46679593,  2.28585348],
           [-2.80389616,  1.80117999]])




```
X_new = np.array([[0, 2], [3, 2], [-3, 3], [-3, 2.5]])
kmeans.predict(X_new)
```




    array([1, 1, 2, 2])




```
# 画出原数据散点图
def plot_data(X):
    plt.plot(X[:, 0], X[:, 1], 'k.', markersize=2)

# 画出聚类中心位置
def plot_centroids(centroids, weights=None, circle_color='w', cross_color='k'):
    if weights is not None:
        centroids = centroids[weights > weights.max() / 10]
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='o', s=35, linewidths=8,
                color=circle_color, zorder=10, alpha=0.9)
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=30, linewidths=12,
                color=cross_color, zorder=11, alpha=1)



def plot_decision_boundaries(clusterer, X, resolution=1000, show_centroids=True,
                             show_xlabels=True, show_ylabels=True):
    # 获取原数据X每个特征的最小值和最大值，方便后续作图
    mins = X.min(axis=0) - 0.1
    maxs = X.max(axis=0) + 0.1
    # 获取网格图，每个轴点数是1000
    xx, yy = np.meshgrid(np.linspace(mins[0], maxs[0], resolution),
                        np.linspace(mins[1], maxs[1], resolution))
    # np.c_ 合并数据
    # 先打开xx和yy做聚类预测，然后再reshape成网格
    Z = clusterer.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # 绘制等高线
    plt.contourf(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]), cmap='Pastel2')
    plt.contour(Z, extent=(mins[0], maxs[0], mins[1], maxs[1]),
                linewidths=1, colors='k')
    plot_data(X)
    
    if show_centroids:
        plot_centroids(clusterer.cluster_centers_)
    
    if show_xlabels:
        plt.xlabel("$x_1$", fontsize=14)
    else:
        plt.tick_params(labelbottom=False)
    if show_ylabels:
        plt.ylabel("$x_2$", fontsize=14, rotation=0)
    else:
        plt.tick_params(labelleft=False)
```


```
plt.figure(figsize=(8, 4))
plot_decision_boundaries(kmeans, X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_31_0.png)



```
# 我做的测试，如果用高斯混合会有什么结果？

plt.figure(figsize=(8, 4))
plot_decision_boundaries(GaussianMixture(n_components=k, random_state=42).fit(X), X, show_centroids=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_32_0.png)


### Hard Clustering vs Soft Clustering


```
# 训练样本到各个中心的距离
kmeans.transform(X_new)
```




    array([[2.88633901, 0.32995317, 2.9042344 , 1.49439034, 2.81093633],
           [5.84236351, 2.80290755, 5.84739223, 4.4759332 , 5.80730058],
           [1.71086031, 3.29399768, 0.29040966, 1.69136631, 1.21475352],
           [1.21567622, 3.21806371, 0.36159148, 1.54808703, 0.72581411]])




```
np.linalg.norm(np.tile(X_new, (1, k)).reshape(-1, k, 2) - kmeans.cluster_centers_, axis=2)
```




    array([[2.88633901, 0.32995317, 2.9042344 , 1.49439034, 2.81093633],
           [5.84236351, 2.80290755, 5.84739223, 4.4759332 , 5.80730058],
           [1.71086031, 3.29399768, 0.29040966, 1.69136631, 1.21475352],
           [1.21567622, 3.21806371, 0.36159148, 1.54808703, 0.72581411]])



### K-means 算法


```
kmeans_iter1 = KMeans(n_clusters=5, init="random", n_init=1,
                     algorithm="full", max_iter=1, random_state=0)
kmeans_iter2 = KMeans(n_clusters=5, init="random", n_init=1,
                     algorithm="full", max_iter=2, random_state=0)
kmeans_iter3 = KMeans(n_clusters=5, init="random", n_init=1,
                     algorithm="full", max_iter=3, random_state=0)
kmeans_iter1.fit(X)
kmeans_iter2.fit(X)
kmeans_iter3.fit(X)
```




    KMeans(algorithm='full', init='random', max_iter=3, n_clusters=5, n_init=1,
           random_state=0)




```
plt.figure(figsize=(10, 8))

plt.subplot(321)
plot_data(X)
plot_centroids(kmeans_iter1.cluster_centers_, circle_color='r', cross_color='w')
plt.ylabel("$x_2$", fontsize=14, rotation=0)
plt.tick_params(labelbottom=False)
plt.title("Update the centroids (initially randomly)", fontsize=14)

plt.subplot(322)
plot_decision_boundaries(kmeans_iter1, X, show_xlabels=False, show_ylabels=False)
plt.title("Label the instances", fontsize=14)

plt.subplot(323)
plot_decision_boundaries(kmeans_iter1, X, show_centroids=False, show_xlabels=False)
plot_centroids(kmeans_iter2.cluster_centers_)

plt.subplot(324)
plot_decision_boundaries(kmeans_iter2, X, show_xlabels=False, show_ylabels=False)

plt.subplot(325)
plot_decision_boundaries(kmeans_iter2, X, show_centroids=False)
plot_centroids(kmeans_iter3.cluster_centers_)

plt.subplot(326)
plot_decision_boundaries(kmeans_iter3, X, show_ylabels=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_38_0.png)



```
def plot_clusterer_comparison(clusterer1, clusterer2, X, title1=None, title2=None):
    clusterer1.fit(X)
    clusterer2.fit(X)

    plt.figure(figsize=(10, 3.2))

    plt.subplot(121)
    plot_decision_boundaries(clusterer1, X)
    if title1:
        plt.title(title1, fontsize=14)

    plt.subplot(122)
    plot_decision_boundaries(clusterer2, X, show_ylabels=False)
    if title2:
        plt.title(title2, fontsize=14)
```


```
kmeans_rnd_init1 = KMeans(n_clusters=5, init="random", n_init=1,
                         algorithm="full", random_state=2)
kmeans_rnd_init2 = KMeans(n_clusters=5, init="random", n_init=1,
                         algorithm="full", random_state=5)

plot_clusterer_comparison(kmeans_rnd_init1, kmeans_rnd_init2, X,
                          "Solution 1", "Solution 2 (with a different random init)")
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_40_0.png)



```
kmeans_rnd_init1.inertia_
```




    219.84385402233195




```
kmeans_rnd_init2.inertia_
```




    236.95563196978733




```
# 多次初始化的参数n_init, 一般情况下多次n_init能够找到比较好的结果

plt.figure(figsize=(8, 4))
plot_decision_boundaries(KMeans(n_clusters=k, n_init=1, random_state=42).fit(X), X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_43_0.png)



```
# 多次初始化的参数n_init

plt.figure(figsize=(8, 4))
plot_decision_boundaries(KMeans(n_clusters=k, n_init=10, random_state=42).fit(X), X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_44_0.png)



```
kmeans.inertia_
```




    211.59853725816828




```
X_dist = kmeans.transform(X)
np.sum(X_dist[np.arange(len(X_dist)), kmeans.labels_]**2)
```




    211.59853725816862




```
kmeans.score(X)
```




    -211.59853725816836



### 如何找到最合适的聚类数？


```
kmeans_k3 = KMeans(n_clusters=3, random_state=42)
kmeans_k8 = KMeans(n_clusters=8, random_state=42)
```


```
plot_clusterer_comparison(kmeans_k3, kmeans_k8, X, "$k=3$", "$k=8$")
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_50_0.png)



```
kmeans_k3.inertia_
```




    653.2223267580945




```
kmeans_k8.inertia_
```




    118.44108623570084




```
kmeans_per_k = [KMeans(n_clusters=k, random_state=42).fit(X) 
               for k in range(1, 10)]
inertias = [model.inertia_ for model in kmeans_per_k]
```


```
plt.figure(figsize=(8, 3.5))
plt.plot(range(1, 10), inertias, "bo-")
plt.xlabel("$k$", fontsize=14)
plt.ylabel("Inertia", fontsize=14)
plt.annotate('Elbow',
             xy=(4, inertias[3]),
             xytext=(0.55, 0.55),
             textcoords='figure fraction',
             fontsize=16,
             arrowprops=dict(facecolor='black', shrink=0.1)
            )

plt.axis([1, 8.5, 0, 1300])
```




    (1.0, 8.5, 0.0, 1300.0)




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_54_1.png)



```
plot_decision_boundaries(kmeans_per_k[4-1], X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_55_0.png)



```
# 轮廓系数
from sklearn.metrics import silhouette_score
```


```
silhouette_score(X, kmeans.labels_)
```




    0.655517642572828




```
silhouette_scores = [silhouette_score(X, model.labels_)
                     for model in kmeans_per_k[1:]]
```


```
silhouette_scores
```




    [0.5966442557582528,
     0.5723900247411775,
     0.688531617595759,
     0.655517642572828,
     0.601878677912387,
     0.6068660656395705,
     0.5616085743054687,
     0.567647042788722]




```
plt.figure(figsize=(8, 3))
plt.plot(range(2, 10), silhouette_scores, "bo-")
plt.xlabel("$k$", fontsize=14)
plt.ylabel("Silhouette score", fontsize=14)
plt.axis([1.8, 8.5, 0.55, 0.7])

```




    (1.8, 8.5, 0.55, 0.7)




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_60_1.png)



```
from sklearn.metrics import silhouette_samples
from matplotlib.ticker import FixedLocator, FixedFormatter
```


```
k = 4
y_pred = kmeans_per_k[k - 1].labels_
silhouette_coefficients = silhouette_samples(X, y_pred)
```


```
silhouette_coefficients
```




    array([0.7796651 , 0.66677869, 0.48656361, ..., 0.87850593, 0.70971862,
           0.45825862])




```
import matplotlib as mpl


def plot_silhouette_diagram(clusterer, X):
    y_pred = clusterer.labels_
    silhouette_coefficients = silhouette_samples(X, y_pred)
    
    k = clusterer.n_clusters
    padding = len(X) // 30
    pos = padding
    ticks = []
    for i in range(k):
        coeffs = silhouette_coefficients[y_pred == i]
        coeffs.sort()

        color = mpl.cm.Spectral(i / k)
        plt.fill_betweenx(np.arange(pos, pos + len(coeffs)), 0, coeffs,
                          facecolor=color, edgecolor=color, alpha=0.7)
        ticks.append(pos + len(coeffs) // 2)
        pos += len(coeffs) + padding

    plt.gca().yaxis.set_major_locator(FixedLocator(ticks))
    plt.gca().yaxis.set_major_formatter(FixedFormatter(range(k)))
#     if k in (3, 5):
#         plt.ylabel("Cluster")
    
#     if k in (5, 6):
#         plt.gca().set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
#         plt.xlabel("Silhouette Coefficient")
#     else:
#         plt.tick_params(labelbottom=False)

    plt.axvline(x=silhouette_scores[k - 2], color="red", linestyle="--")
    plt.title("$k={}$".format(k), fontsize=16)
```


```
plt.figure(figsize=(11, 9))

for k in (3, 4, 5, 6):
    plt.subplot(2, 2, k - 2)
    plot_silhouette_diagram(kmeans_per_k[k - 1], X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_65_0.png)


### Limits of K-Means


```
X2, y2 = make_blobs(n_samples=250, centers=1, random_state=42)
plot_clusters(X2)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_67_0.png)



```
X1, y1 = make_blobs(n_samples=1000, centers=((4, -4), (0, 0)), random_state=42)
X1 = X1.dot(np.array([[0.374, 0.95], [0.732, 0.598]]))
X2, y2 = make_blobs(n_samples=250, centers=1, random_state=42)
X2 = X2 + [6, -8]
X = np.r_[X1, X2]
y = np.r_[y1, y2]
```


```
plot_clusters(X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_69_0.png)



```
kmeans_good = KMeans(n_clusters=3, init=np.array([[-1.5, 2.5], [0.5, 0], [4, 0]]), n_init=1, random_state=42)
kmeans_bad = KMeans(n_clusters=3, random_state=42)
kmeans_good.fit(X)
kmeans_bad.fit(X)
```




    KMeans(n_clusters=3, random_state=42)




```
plt.figure(figsize=(10, 3.2))

plt.subplot(121)
plot_decision_boundaries(kmeans_good, X)

plt.subplot(122)
plot_decision_boundaries(kmeans_bad, X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_71_0.png)



```
# 不标记初始点的话，即使是多次随机定点也无法得到准确的中心点

# 同时，我们也可以知道，当集群具有不同的大小，不同密度或非球形时，kmeans的表现不佳。
plot_decision_boundaries(KMeans(n_clusters=3, random_state=42, n_init=100).fit(X), X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_72_0.png)



```
# 高斯混合好一些，但是还是很奇怪，比如边缘的一些预测

plot_decision_boundaries(GaussianMixture(n_components=3, random_state=42, n_init=10).fit(X), X, show_centroids=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_73_0.png)


### 使用聚类进行图像分割


```
from matplotlib.image import imread

image = imread("C:/我的研究/ml/机器学习实战2/handson-ml2-master/images/unsupervised_learning/ladybug.png")
image.shape
```




    (533, 800, 3)




```
plt.imshow(image)
plt.tick_params(labelbottom=False, labelleft=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_76_0.png)



```
X = image.reshape(-1, 3)
kmeans = KMeans(n_clusters=8, random_state=42).fit(X)
segmented_img = kmeans.cluster_centers_[kmeans.labels_]
segmented_img = segmented_img.reshape(image.shape)
```


```
segmented_imgs = []
n_colors = (10, 8, 6, 4, 2)
for n_clusters in n_colors:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(X)
    segmented_img = kmeans.cluster_centers_[kmeans.labels_]
    segmented_imgs.append(segmented_img.reshape(image.shape))
```


```
plt.figure(figsize=(10, 5))
plt.subplots_adjust(wspace=0.05, hspace=0.1)

plt.subplot(231)
plt.imshow(image)
plt.title("Original image")
plt.axis("off")

for idx, n_clusters in enumerate(n_colors):
    plt.subplot(232 + idx)
    plt.imshow(segmented_imgs[idx])
    plt.title("{} colors".format(n_clusters))
    plt.axis('off')
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_79_0.png)


## 使用聚类进行预处理


```
from sklearn.datasets import load_digits
```


```
X_digits, y_digits = load_digits(return_X_y=True)
```


```
X_digits
```




    array([[ 0.,  0.,  5., ...,  0.,  0.,  0.],
           [ 0.,  0.,  0., ..., 10.,  0.,  0.],
           [ 0.,  0.,  0., ..., 16.,  9.,  0.],
           ...,
           [ 0.,  0.,  1., ...,  6.,  0.,  0.],
           [ 0.,  0.,  2., ..., 12.,  0.,  0.],
           [ 0.,  0., 10., ..., 12.,  1.,  0.]])




```
plt.imshow(X_digits[1].reshape(8, -1))
```




    <matplotlib.image.AxesImage at 0x27343744130>




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_84_1.png)



```
y_digits
```




    array([0, 1, 2, ..., 8, 9, 8])




```
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, random_state=42)
```


```
from sklearn.linear_model import LogisticRegression
```


```
log_reg = LogisticRegression(multi_class="ovr", solver="lbfgs", max_iter=5000, random_state=42)
log_reg.fit(X_train, y_train)
```




    LogisticRegression(max_iter=5000, multi_class='ovr', random_state=42)




```
log_reg_score = log_reg.score(X_test, y_test)
log_reg_score
```




    0.9688888888888889




```
from sklearn.pipeline import Pipeline
```


```
pipeline = Pipeline([
    ("kmeans", KMeans(n_clusters=50, random_state=42)),
    ("log_reg", LogisticRegression(multi_class="ovr", solver="lbfgs", max_iter=5000, random_state=42)),
])
pipeline.fit(X_train, y_train)
```




    Pipeline(steps=[('kmeans', KMeans(n_clusters=50, random_state=42)),
                    ('log_reg',
                     LogisticRegression(max_iter=5000, multi_class='ovr',
                                        random_state=42))])




```
pipeline_score = pipeline.score(X_test, y_test)
pipeline_score
```




    0.98




```
1 - (1 - pipeline_score) / (1 - log_reg_score)
```




    0.3571428571428561




```
from sklearn.model_selection import GridSearchCV
```


```
param_grid = dict(kmeans__n_clusters=range(2, 100))
grid_clf = GridSearchCV(pipeline, param_grid, cv=3)
grid_clf.fit(X_train, y_train)
```




    GridSearchCV(cv=3,
                 estimator=Pipeline(steps=[('kmeans',
                                            KMeans(n_clusters=50, random_state=42)),
                                           ('log_reg',
                                            LogisticRegression(max_iter=5000,
                                                               multi_class='ovr',
                                                               random_state=42))]),
                 param_grid={'kmeans__n_clusters': range(2, 100)})




```
grid_clf.best_params_
```




    {'kmeans__n_clusters': 57}




```
grid_clf.score(X_test, y_test)
```




    0.98



### 使用聚类进行半监督学习


```
n_labeled = 50
```


```
log_reg = LogisticRegression(multi_class='ovr', solver='lbfgs', random_state=42)
log_reg.fit(X_train[:n_labeled], y_train[:n_labeled])
log_reg.score(X_test, y_test)
```




    0.8333333333333334




```
k = 50
```


```
kmeans = KMeans(n_clusters=k, random_state=42)
X_digits_dist = kmeans.fit_transform(X_train)

# 找出一个代表性的中心点，即离每个中心点最近的一个点, 有50个中心所以最后找出50个点
representative_digit_idx = np.argmin(X_digits_dist, axis=0)

X_representative_digits = X_train[representative_digit_idx]
```


```
X_representative_digits
```




    array([[ 0.,  0.,  7., ...,  3.,  0.,  0.],
           [ 0.,  0.,  0., ..., 15.,  4.,  0.],
           [ 0.,  0.,  6., ..., 11.,  1.,  0.],
           ...,
           [ 0.,  0.,  3., ...,  2.,  0.,  0.],
           [ 0.,  0.,  1., ...,  0.,  0.,  0.],
           [ 0.,  0.,  0., ...,  6.,  0.,  0.]])




```
kmeans.labels_
```




    array([13, 14, 26, ..., 39,  4, 10])




```
plt.figure(figsize=(8, 2))
for index, X_representative_digit in enumerate(X_representative_digits):
    plt.subplot(k // 10, 10, index + 1)
    plt.imshow(X_representative_digit.reshape(8, 8), cmap='binary', interpolation='bilinear')
    plt.axis('off')
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_105_0.png)



```
y_representative_digits = y_train[representative_digit_idx]
```


```
y_representative_digits
```




    array([0, 1, 3, 2, 7, 6, 4, 6, 9, 5, 1, 2, 9, 5, 2, 7, 8, 1, 8, 6, 3, 1,
           5, 4, 5, 4, 0, 3, 2, 6, 1, 7, 7, 9, 1, 8, 6, 5, 4, 8, 5, 3, 3, 6,
           7, 9, 7, 8, 4, 9])




```
log_reg = LogisticRegression(multi_class="ovr", solver="lbfgs", max_iter=5000, random_state=42)
log_reg.fit(X_representative_digits, y_representative_digits)
log_reg.score(X_test, y_test)
```




    0.9244444444444444




```
y_train_propagated = np.empty(len(X_train), dtype=np.int32)
```


```
for i in range(k,):
    y_train_propagated[kmeans.labels_ == i] = y_representative_digit[i]
```


```
y_train_propagated
```




    array([5, 2, 0, ..., 8, 7, 1])



经过传播后预测的精度能够提高更多


```
log_reg = LogisticRegression(multi_class="ovr", solver="lbfgs", max_iter=5000, random_state=42)
log_reg.fit(X_train, y_train_propagated)
```




    LogisticRegression(max_iter=5000, multi_class='ovr', random_state=42)




```
log_reg.score(X_test, y_test)
```




    0.9377777777777778



我们获得了一点点的准确度提升。 总比没有好，但我们可能应该只将标签传播到最靠近质心的实例，因为通过传播到整个集群，我们肯定包含了一些异常值。 让我们只将标签传播到最接近质心的第 75 个百分位数：


```
# 定义75百分数
percentile_closest = 70

# 找出每一个样本到所在类中心的距离
X_cluster_dist = X_digits_dist[np.arange(len(X_train)), kmeans.labels_]

# 为什么循环？
# 每一个类别都做一次筛选，把离中心比较远的点作为离群点，赋值为-1
for i in range(k):
    in_cluster = (kmeans.labels_ == i)
    cluster_dist = X_cluster_dist[in_cluster]
    # 找出百分位对应的数值
    cutoff_distance = np.percentile(cluster_dist, percentile_closest)
    # 筛选出大于该数值的样本，并标记为-1
    above_cutoff = (X_cluster_dist > cutoff_distance)
    X_cluster_dist[in_cluster & above_cutoff] = -1
```


```
partially_propagated = (X_cluster_dist != -1)
X_train_partially_propagated = X_train[partially_propagated]
y_train_partially_propagated = y_train_propagated[partially_propagated]
```


```
log_reg = LogisticRegression(multi_class="ovr", solver="lbfgs", max_iter=5000, random_state=42)
log_reg.fit(X_train_partially_propagated, y_train_partially_propagated)
```




    LogisticRegression(max_iter=5000, multi_class='ovr', random_state=42)




```
log_reg.score(X_test, y_test)
```




    0.9355555555555556




```
np.mean(y_train_partially_propagated == y_train[partially_propagated])
```




    0.9430955993930197



## DBSCAN


```
from sklearn.datasets import make_moons
```


```
X, y = make_moons(n_samples=1000, noise=0.05, random_state=42)
```


```
X.shape
```




    (1000, 2)




```
y[:10]
```




    array([1, 1, 1, 1, 0, 1, 1, 1, 1, 0], dtype=int64)




```
from sklearn.cluster import DBSCAN
```


```
dbscan = DBSCAN(eps=0.05, min_samples=5)
dbscan.fit(X)
```




    DBSCAN(eps=0.05)




```
dbscan.labels_[:10]
```




    array([ 0,  2, -1, -1,  1,  0,  0,  0,  2,  5], dtype=int64)




```
len(dbscan.core_sample_indices_)
```




    808




```
# 核心实例的索引
dbscan.core_sample_indices_[:10]
```




    array([ 0,  4,  5,  6,  7,  8, 10, 11, 12, 13], dtype=int64)




```
# 可得到核心实例本身
dbscan.components_
```




    array([[-0.02137124,  0.40618608],
           [-0.84192557,  0.53058695],
           [ 0.58930337, -0.32137599],
           ...,
           [ 1.66258462, -0.3079193 ],
           [-0.94355873,  0.3278936 ],
           [ 0.79419406,  0.60777171]])




```
np.unique(dbscan.labels_)
```




    array([-1,  0,  1,  2,  3,  4,  5,  6], dtype=int64)



#### 我的尝试


```
plt.figure(figsize=(10, 5))

plt.plot(X[y==0, 0], X[y==0, 1], 'bo')
plt.plot(X[y==1, 0], X[y==1, 1], 'yo')
# plt.plot(dbscan.components_[:, 0], dbscan.components_[:, 1], "r^")
```




    [<matplotlib.lines.Line2D at 0x273404632b0>]




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_134_1.png)



```
plt.figure(figsize=(10, 5))
for i in np.unique(dbscan.labels_):
    if i != -1:
        plt.plot(X[dbscan.labels_==i, 0], X[dbscan.labels_==i, 1], 'o')
    else:
        plt.scatter(X[dbscan.labels_==i, 0], X[dbscan.labels_==i, 1], c="r", marker="x", s=100)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_135_0.png)



```
def plot_dbscan(dbscan, X, size, show_xlabels=True, show_ylabels=True):
    core_mask = np.zeros_like(dbscan.labels_, dtype=bool)
    core_mask[dbscan.core_sample_indices_] = True
    anomalies_mask = dbscan.labels_ == -1
    non_core_mask = ~(core_mask | anomalies_mask)
    
    cores = dbscan.components_
    anomalies = X[anomalies_mask]
    non_cores = X[non_core_mask]
    
    plt.scatter(cores[:, 0], cores[:, 1],
                c=dbscan.labels_[core_mask], marker='o', s=size, cmap="Paired")
    plt.scatter(cores[:, 0], cores[:, 1],
                marker='*', s=20, c=dbscan.labels_[core_mask])
    plt.scatter(anomalies[:, 0], anomalies[:, 1],
                c="r", marker="x", s=100)
    plt.scatter(non_cores[:, 0], non_cores[:, 1], c=dbscan.labels_[non_core_mask], marker=".")
    
    if show_xlabels:
        plt.xlabel("$x_1$", fontsize=14)
    else:
        plt.tick_params(labelbottom=False)
    if show_ylabels:
        plt.ylabel("$x_2$", fontsize=14, rotation=0)
    else:
        plt.tick_params(labelleft=False)
    plt.title("eps={:.2f}, min_samples={}".format(dbscan.eps, dbscan.min_samples), fontsize=14)
```


```
dbscan2 = DBSCAN(eps=0.2)
dbscan2.fit(X)
```




    DBSCAN(eps=0.2)




```
plt.figure(figsize=(9, 3.2))

plt.subplot(121)
plot_dbscan(dbscan, X, size=100)

plt.subplot(122)
plot_dbscan(dbscan2, X, size=600, show_ylabels=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_138_0.png)



```
# 我的尝试，很失败的KMeans
plot_decision_boundaries(KMeans(n_clusters=8).fit(X), X, show_centroids=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_139_0.png)



```
dbscan = dbscan2
```


```
from sklearn.neighbors import KNeighborsClassifier
```


```
knn = KNeighborsClassifier(n_neighbors=50)
knn.fit(dbscan.components_, dbscan.labels_[dbscan.core_sample_indices_])
```




    KNeighborsClassifier(n_neighbors=50)




```
X_new = np.array([[-0.5, 0], [0, 0.5], [1, -0.1], [2, 1]])
knn.predict(X_new)
```




    array([1, 0, 1, 0], dtype=int64)




```
# 估计为每个集群的概率
knn.predict_proba(X_new)
```




    array([[0.18, 0.82],
           [1.  , 0.  ],
           [0.12, 0.88],
           [1.  , 0.  ]])




```
plt.figure(figsize=(6, 3))

plot_decision_boundaries(knn, X, show_centroids=False)
plt.scatter(X_new[:, 0], X_new[:, 1], c='b', marker='+', s=200, zorder=10)
```




    <matplotlib.collections.PathCollection at 0x273408af040>




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_145_1.png)



```
y_dist, y_pred_idx = knn.kneighbors(X_new, n_neighbors=1)
y_pred = dbscan.labels_[dbscan.core_sample_indices_][y_pred_idx]
y_pred[y_dist > 0.2] = -1
y_pred.ravel()
```




    array([-1,  0,  1, -1], dtype=int64)




```
# 支持向量机
from sklearn.svm import SVC
svm = SVC()
svm.fit(dbscan.components_, dbscan.labels_[dbscan.core_sample_indices_])

plt.figure(figsize=(6, 3))

plot_decision_boundaries(svm, X, show_centroids=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_147_0.png)



```
# 随机森林
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=200)
rf.fit(dbscan.components_, dbscan.labels_[dbscan.core_sample_indices_])

plt.figure(figsize=(6, 3))

plot_decision_boundaries(rf, X, show_centroids=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_148_0.png)



```
# 决策树
from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier()
tree.fit(dbscan.components_, dbscan.labels_[dbscan.core_sample_indices_])

plt.figure(figsize=(6, 3))

plot_decision_boundaries(tree, X, show_centroids=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_149_0.png)


## 其他聚类算法

### 光谱聚类


```
from sklearn.cluster import SpectralClustering
```


```
sc1 = SpectralClustering(n_clusters=2, gamma=100, random_state=42)
sc1.fit(X)
```




    SpectralClustering(gamma=100, n_clusters=2, random_state=42)




```
sc2 = SpectralClustering(n_clusters=2, gamma=1, random_state=42)
sc2.fit(X)
```




    SpectralClustering(gamma=1, n_clusters=2, random_state=42)




```
np.percentile(sc1.affinity_matrix_, 95)
```




    0.04251990648936265




```
def plot_spectral_clustering(sc, X, size, alpha, show_xlabels=True, show_ylabels=True):
    plt.scatter(X[:, 0], X[:, 1], marker='o', s=size, c='gray', cmap="Paired", alpha=alpha)
    plt.scatter(X[:, 0], X[:, 1], marker='o', s=30, c='w')
    plt.scatter(X[:, 0], X[:, 1], marker='.', s=10, c=sc.labels_, cmap="Paired")
    
    if show_xlabels:
        plt.xlabel("$x_1$", fontsize=14)
    else:
        plt.tick_params(labelbottom=False)
    if show_ylabels:
        plt.ylabel("$x_2$", fontsize=14, rotation=0)
    else:
        plt.tick_params(labelleft=False)
    plt.title("RBF gamma={}".format(sc.gamma), fontsize=14)
```


```
plt.figure(figsize=(9, 3.2))

plt.subplot(121)
plot_spectral_clustering(sc1, X, size=500, alpha=0.1)

plt.subplot(122)
plot_spectral_clustering(sc2, X, size=4000, alpha=0.01, show_ylabels=False)

plt.show()

```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_157_0.png)


### 凝聚聚类


```
from sklearn.cluster import AgglomerativeClustering
```


```
X = np.array([0, 2, 5, 8.5]).reshape(-1, 1)
agg = AgglomerativeClustering(linkage="complete").fit(X)
```


```
def learned_parameters(estimator):
    return [attrib for attrib in dir(estimator)
            if attrib.endswith("_") and not attrib.startswith("_")]
```


```
learned_parameters(agg)
```




    ['children_',
     'labels_',
     'n_clusters_',
     'n_connected_components_',
     'n_features_in_',
     'n_leaves_']




```
agg.children_
```




    array([[0, 1],
           [2, 3],
           [4, 5]])



## Gaussian Mixtures


```
X1, Y1 = make_blobs(n_samples=1000, centers=((4, -4), (0, 0)), random_state=42)
X1 = X1.dot(np.array([[0.374, 0.95], [0.732, 0.598]]))
X2, y2 = make_blobs(n_samples=250, centers=1, random_state=42)
X2 = X2 + [6, -8]
X = np.r_[X1, X2]
y = np.r_[y1, y2]
```


```
plt.figure(figsize=(8, 4))
plot_clusters(X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_166_0.png)



```
from sklearn.mixture import GaussianMixture
```


```
gm = GaussianMixture(n_components=3, n_init=10, random_state=42)
gm.fit(X)
```




    GaussianMixture(n_components=3, n_init=10, random_state=42)




```
gm.weights_
```




    array([0.39054348, 0.2093669 , 0.40008962])




```
500/1250, 250/1250
```




    (0.4, 0.2)




```
gm.means_
```




    array([[ 0.05224874,  0.07631976],
           [ 3.40196611,  1.05838748],
           [-1.40754214,  1.42716873]])




```
# 协方差
gm.covariances_
```




    array([[[ 0.6890309 ,  0.79717058],
            [ 0.79717058,  1.21367348]],
    
           [[ 1.14296668, -0.03114176],
            [-0.03114176,  0.9545003 ]],
    
           [[ 0.63496849,  0.7298512 ],
            [ 0.7298512 ,  1.16112807]]])




```
y_pred = gm.predict(X)
np.unique(y_pred)
```




    array([0, 1, 2], dtype=int64)




```
for i in np.unique(y_pred):
    plt.plot(X[y_pred==i, 0], X[y_pred==i, 1], 'o', marker='.')
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_174_0.png)



```
plot_decision_boundaries(gm, X, show_centroids=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_175_0.png)



```
# 是否收敛
gm.converged_
```




    True




```
# 迭代次数
gm.n_iter_
```




    4




```
gm.predict(X)
```




    array([0, 0, 2, ..., 1, 1, 1], dtype=int64)




```
gm.predict_proba(X)
```




    array([[9.77227791e-01, 2.27715290e-02, 6.79898914e-07],
           [9.83288385e-01, 1.60345103e-02, 6.77104389e-04],
           [7.51824662e-05, 1.90251273e-06, 9.99922915e-01],
           ...,
           [4.35053542e-07, 9.99999565e-01, 2.17938894e-26],
           [5.27837047e-16, 1.00000000e+00, 1.50679490e-41],
           [2.32355608e-15, 1.00000000e+00, 8.21915701e-41]])




```
X_new, y_new = gm.sample(6)
X_new
```




    array([[-0.8690223 , -0.32680051],
           [ 0.29945755,  0.2841852 ],
           [ 1.85027284,  2.06556913],
           [ 3.98260019,  1.50041446],
           [ 3.82006355,  0.53143606],
           [-1.04015332,  0.7864941 ]])




```
y_new
```




    array([0, 0, 1, 1, 1, 2])




```
# 计算该位置的概率密度函数(PDF)的对数
gm.score_samples(X)
```




    array([-2.60674489, -3.57074133, -3.33007348, ..., -3.51379355,
           -4.39643283, -3.8055665 ])




```
resolution = 100
grid = np.arange(-10, 10, 1 / resolution)
xx, yy = np.meshgrid(grid, grid)
X_full = np.vstack([xx.ravel(), yy.ravel()]).T

pdf = np.exp(gm.score_samples(X_full))
pdf_probas = pdf * (1 / resolution) ** 2
pdf_probas.sum()
```




    0.9999999999271592




```
grid
```




    array([-10.  ,  -9.99,  -9.98, ...,   9.97,   9.98,   9.99])




```
from matplotlib.colors import LogNorm

def plot_gaussian_mixture(clusterer, X, resolution=1000, show_ylabels=True):
    mins = X.min(axis=0) - 0.1
    maxs = X.max(axis=0) + 0.1
    xx, yy = np.meshgrid(np.linspace(mins[0], maxs[0], resolution),
                        np.linspace(mins[1], maxs[1], resolution),)
    Z = -clusterer.score_samples(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z,
                norm=LogNorm(vmin=1.0, vmax=30.0),
                levels=np.logspace(0, 2, 12))
    plt.contour(xx, yy, Z,
                norm=LogNorm(vmin=1.0, vmax=30.0),
                levels=np.logspace(0, 2, 12),
                linewidths=1, colors='k')
    
    Z = clusterer.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z, 
                linewidths=2, colors='r', linestyles='dashed')
    
    plt.plot(X[:, 0], X[:, 1], 'k.', markersize=2)
    plot_centroids(clusterer.means_, clusterer.weights_)
    
    plt.xlabel("$x_1$", fontsize=14)
    if show_ylabels:
        plt.ylabel("$x_2$", fontsize=14, rotation=0)
    else:
        plt.tick_params(labelleft=False)
```


```
plt.figure(figsize=(8, 4))

plot_gaussian_mixture(gm, X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_186_0.png)



```
gm_full = GaussianMixture(n_components=3, n_init=10, covariance_type='full', random_state=42)
gm_tied = GaussianMixture(n_components=3, n_init=10, covariance_type='tied', random_state=42)
gm_spherical = GaussianMixture(n_components=3, n_init=10, covariance_type='spherical', random_state=42)
gm_diag = GaussianMixture(n_components=3, n_init=10, covariance_type='diag', random_state=42)

gm_full.fit(X)
gm_tied.fit(X)
gm_spherical.fit(X)
gm_diag.fit(X)
```




    GaussianMixture(covariance_type='diag', n_components=3, n_init=10,
                    random_state=42)




```
def compare_gaussian_mixtures(gm1, gm2, X):
    plt.figure(figsize=(9, 3))
    
    plt.subplot(121)
    plot_gaussian_mixture(gm1, X)
    plt.title(f"covariance_type={gm1.covariance_type}", fontsize=14)
    
    plt.subplot(122)
    plot_gaussian_mixture(gm2, X)
    plt.title(f"covariance_type={gm2.covariance_type}", fontsize=14)
```


```
compare_gaussian_mixtures(gm_tied, gm_spherical, X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_189_0.png)



```
compare_gaussian_mixtures(gm_full, gm_diag, X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_190_0.png)


### 使用高斯混合进行异常检测

高斯混合可用于异常检测：位于低密度区域的实例可被视为异常。 您必须定义要使用的密度阈值。 例如，在试图检测缺陷产品的制造公司中，缺陷产品的比率通常是众所周知的。 假设它等于 4%，那么您可以将密度阈值设置为导致 4% 的实例位于低于该阈值密度的区域的值：


```
# 通过高斯混合进行数据清洗！！！！
densities = gm.score_samples(X)
densities_threshold = np.percentile(densities, 4)
anomalies = X[densities < densities_threshold]
```


```
plt.figure(figsize=(8, 4))

plot_gaussian_mixture(gm, X)
plt.scatter(anomalies[:, 0], anomalies[:, 1], c='r', marker='x')
```




    <matplotlib.collections.PathCollection at 0x273409528e0>




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_194_1.png)



```
gm.bic(X)
```




    8189.662685850679




```
gm.aic(X)
```




    8102.437405735641



### AIC和BIC的手动计算方法


```
n_clusters = 3
n_dims = 2
n_params_for_weights = n_clusters - 1
n_params_for_means = n_clusters * n_dims
n_params_for_covariance = n_clusters * n_dims * (n_dims + 1) // 2
n_params = n_params_for_weights + n_params_for_means + n_params_for_covariance
max_log_likelihood = gm.score(X) * len(X) # log(L^)
bic = np.log(len(X)) * n_params - 2 * max_log_likelihood
aic = 2 * n_params - 2 * max_log_likelihood
```


```
aic
```




    8102.437405735641




```
n_params
```




    17




```
gms_per_k = [GaussianMixture(n_components=k, n_init=10, random_state=42).fit(X)
            for k in range(1, 11)]
```


```
bics = [model.bic(X) for model in gms_per_k]
aics = [model.aic(X) for model in gms_per_k]
```


```
plt.figure(figsize=(8, 3))

plt.plot(range(1, 11), bics, 'bo-', label='BIC')
plt.plot(range(1, 11), aics, 'go--', label='AIC')

plt.xlabel("$k$", fontsize=14)
plt.ylabel("Information Criterion", fontsize=14)
plt.axis([1, 9.5, np.min(aics) - 50, np.max(aics) + 50])
plt.annotate('Minimum',
             xy=(3, bics[2]),
             xytext=(0.35, 0.6),
             textcoords='figure fraction',
             fontsize=14,
             arrowprops=dict(facecolor='black', shrink=0.1)
            )

plt.legend()
```




    <matplotlib.legend.Legend at 0x2734705e940>




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_203_1.png)



```
min_bic = np.infty

for k in range(1, 11):
    for covariance_type in ["full", "tied", "spherical", "diag"]:
        bic = GaussianMixture(n_components=k, n_init=10,
                             covariance_type=covariance_type,
                             random_state=42).fit(X).bic(X)
        if bic < min_bic:
            min_bic = bic
            best_k = k
            best_covariance_type = covariance_type
```


```
print(f"min_bic: {min_bic}, \nbest_k: {best_k}, \nbest_covariance_type: {best_covariance_type}")
```

    min_bic: 8189.662685850679, 
    best_k: 3, 
    best_covariance_type: full


### 贝叶斯高斯混合模型

不是手动搜索最佳集群数，而是可以使用 BayesianGaussianMixture 类来代替，该类能够为不必要的集群赋予等于（或接近）为零的权重。 只需将组件数量设置为您认为大于最佳集群数量的值，算法将自动消除不必要的集群。


```
from sklearn.mixture import BayesianGaussianMixture
```


```
bgm = BayesianGaussianMixture(n_components=10, n_init=10, random_state=42)
bgm.fit(X)
```

    c:\users\13631\appdata\local\programs\python\python38\lib\site-packages\sklearn\mixture\_base.py:265: ConvergenceWarning: Initialization 10 did not converge. Try different init parameters, or increase max_iter, tol or check for degenerate data.
      warnings.warn('Initialization %d did not converge. '





    BayesianGaussianMixture(n_components=10, n_init=10, random_state=42)




```
np.round(bgm.weights_, 2)
```




    array([0.4 , 0.  , 0.  , 0.  , 0.39, 0.2 , 0.  , 0.  , 0.  , 0.  ])



**贝叶斯高斯混合确实很好用，类似于lasso，可以直接确定比较好的类别数**


```
plt.figure(figsize=(5, 3))
plot_gaussian_mixture(bgm, X)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_212_0.png)



```
bgm_low = BayesianGaussianMixture(n_components=10, max_iter=1000, n_init=1,
                                 weight_concentration_prior=0.01, random_state=42)

bgm_high = BayesianGaussianMixture(n_components=10, max_iter=1000, n_init=1,
                                 weight_concentration_prior=10000, random_state=42)

nn = 73
bgm_low.fit(X[:nn])
bgm_high.fit(X[:nn])
```




    BayesianGaussianMixture(max_iter=1000, n_components=10, random_state=42,
                            weight_concentration_prior=10000)




```
np.round(bgm_low.weights_, 2)
```




    array([0.49, 0.51, 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ])




```
np.round(bgm_high.weights_, 2)
```




    array([0.43, 0.01, 0.01, 0.11, 0.01, 0.01, 0.01, 0.37, 0.01, 0.01])




```
plt.figure(figsize=(9, 4))

plt.subplot(121)
plot_gaussian_mixture(bgm_low, X[:nn])
plt.title("weight_concentration_prior = 0.01", fontsize=14)

plt.subplot(122)
plot_gaussian_mixture(bgm_high, X[:nn], show_ylabels=False)
plt.title("weight_concentration_prior = 10000", fontsize=14)
```




    Text(0.5, 1.0, 'weight_concentration_prior = 10000')




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_216_1.png)



```
X_moons, y_moons = make_moons(n_samples=1000, noise=0.05, random_state=42)
```


```
bgm = BayesianGaussianMixture(n_components=10, n_init=10, random_state=42)
bgm.fit(X_moons)
```




    BayesianGaussianMixture(n_components=10, n_init=10, random_state=42)




```
plt.figure(figsize=(9, 3.2))

plt.subplot(121)
plot_data(X_moons)
plt.xlabel("$x_1$", fontsize=14)
plt.ylabel("$x_2$", fontsize=14, rotation=0)

plt.subplot(122)
plot_gaussian_mixture(bgm, X_moons, show_ylabels=False)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_219_0.png)


## Likelihood Function(似然函数)


```
from scipy.stats import norm
```


```
xx = np.linspace(-6, 4, 101)
ss = np.linspace(1, 2, 101)

XX, SS = np.meshgrid(xx, ss)
ZZ = 2 * norm.pdf(XX - 1.0, 0, SS) + norm.pdf(XX + 4.0, 0, SS)
ZZ = ZZ / ZZ.sum(axis=1)[:, np.newaxis] / (xx[1] - xx[0])
```


```
from matplotlib.patches import Polygon

plt.figure(figsize=(12, 10))

x_idx = 85
s_idx = 30

plt.subplot(221)
plt.contourf(XX, SS, ZZ, cmap="GnBu")
plt.plot([-6, 4], [ss[s_idx], ss[s_idx]], "k-", linewidth=2)
plt.plot([xx[x_idx], xx[x_idx]], [1, 2], "b-", linewidth=2)
plt.xlabel(r"$x$")
plt.ylabel(r"$\theta$", fontsize=14, rotation=0)
plt.title(r"Model $f(x; \theta)$", fontsize=14)

plt.subplot(222)
plt.plot(ss, ZZ[:, x_idx], "b-")
max_idx = np.argmax(ZZ[:, x_idx])
max_val = np.max(ZZ[:, x_idx])
plt.plot(ss[max_idx], max_val, "r.")
plt.plot([ss[max_idx], ss[max_idx]], [0, max_val], "r:")
plt.plot([0, ss[max_idx]], [max_val, max_val], "r:")
plt.text(1.01, max_val + 0.005, r"$\hat{L}$", fontsize=14)
plt.text(ss[max_idx]+ 0.01, 0.055, r"$\hat{\theta}$", fontsize=14)
plt.text(ss[max_idx]+ 0.01, max_val - 0.012, r"$Max$", fontsize=12)
plt.axis([1, 2, 0.05, 0.15])
plt.xlabel(r"$\theta$", fontsize=14)
plt.grid(True)
plt.text(1.99, 0.135, r"$=f(x=2.5; \theta)$", fontsize=14, ha="right")
plt.title(r"Likelihood function $\mathcal{L}(\theta|x=2.5)$", fontsize=14)

plt.subplot(223)
plt.plot(xx, ZZ[s_idx], "k-")
plt.axis([-6, 4, 0, 0.25])
plt.xlabel(r"$x$", fontsize=14)
plt.grid(True)
plt.title(r"PDF $f(x; \theta=1.3)$", fontsize=14)
verts = [(xx[41], 0)] + list(zip(xx[41:81], ZZ[s_idx, 41:81])) + [(xx[80], 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
plt.gca().add_patch(poly)

plt.subplot(224)
plt.plot(ss, np.log(ZZ[:, x_idx]), "b-")
max_idx = np.argmax(np.log(ZZ[:, x_idx]))
max_val = np.max(np.log(ZZ[:, x_idx]))
plt.plot(ss[max_idx], max_val, "r.")
plt.plot([ss[max_idx], ss[max_idx]], [-5, max_val], "r:")
plt.plot([0, ss[max_idx]], [max_val, max_val], "r:")
plt.axis([1, 2, -2.4, -2])
plt.xlabel(r"$\theta$", fontsize=14)
plt.text(ss[max_idx]+ 0.01, max_val - 0.05, r"$Max$", fontsize=12)
plt.text(ss[max_idx]+ 0.01, -2.39, r"$\hat{\theta}$", fontsize=14)
plt.text(1.01, max_val + 0.02, r"$\log \, \hat{L}$", fontsize=14)
plt.grid(True)
plt.title(r"$\log \, \mathcal{L}(\theta|x=2.5)$", fontsize=14)

```




    Text(0.5, 1.0, '$\\log \\, \\mathcal{L}(\\theta|x=2.5)$')




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_223_1.png)



