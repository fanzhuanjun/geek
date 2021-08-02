## 10. 对 Olivetti Faces 数据集进行聚类


```python
import numpy as np
import os
np.random.seed(42)
import matplotlib.pyplot as plt
```


```python
from sklearn.datasets import fetch_olivetti_faces

olivetti = fetch_olivetti_faces()
```


```python
print(olivetti.DESCR)
```

    .. _olivetti_faces_dataset:
    
    The Olivetti faces dataset
    --------------------------
    
    `This dataset contains a set of face images`_ taken between April 1992 and 
    April 1994 at AT&T Laboratories Cambridge. The
    :func:`sklearn.datasets.fetch_olivetti_faces` function is the data
    fetching / caching function that downloads the data
    archive from AT&T.
    
    .. _This dataset contains a set of face images: http://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html
    
    As described on the original website:
    
        There are ten different images of each of 40 distinct subjects. For some
        subjects, the images were taken at different times, varying the lighting,
        facial expressions (open / closed eyes, smiling / not smiling) and facial
        details (glasses / no glasses). All the images were taken against a dark
        homogeneous background with the subjects in an upright, frontal position 
        (with tolerance for some side movement).
    
    **Data Set Characteristics:**
    
        =================   =====================
        Classes                                40
        Samples total                         400
        Dimensionality                       4096
        Features            real, between 0 and 1
        =================   =====================
    
    The image is quantized to 256 grey levels and stored as unsigned 8-bit 
    integers; the loader will convert these to floating point values on the 
    interval [0, 1], which are easier to work with for many algorithms.
    
    The "target" for this database is an integer from 0 to 39 indicating the
    identity of the person pictured; however, with only 10 examples per class, this
    relatively small dataset is more interesting from an unsupervised or
    semi-supervised perspective.
    
    The original dataset consisted of 92 x 112, while the version available here
    consists of 64x64 images.
    
    When using these images, please give credit to AT&T Laboratories Cambridge.


​    


```python
olivetti.target[:20]
```




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])




```python
olivetti.data.shape
```




    (400, 4096)




```python
from sklearn.model_selection import StratifiedShuffleSplit

strat_split = StratifiedShuffleSplit(n_splits=1, test_size=40, random_state=42)
train_valid_idx, test_idx = next(strat_split.split(olivetti.data, olivetti.target))

X_train_valid = olivetti.data[train_valid_idx]
y_train_valid = olivetti.target[train_valid_idx]

X_test = olivetti.data[test_idx]
y_test = olivetti.target[test_idx]

strat_split = StratifiedShuffleSplit(n_splits=1, test_size=80, random_state=43)
train_idx, valid_idx = next(strat_split.split(X_train_valid, y_train_valid))

X_train = X_train_valid[train_idx]
y_train = y_train_valid[train_idx]

X_valid = X_train_valid[valid_idx]
y_valid = y_train_valid[valid_idx]
```


```python
print(X_train.shape, y_train.shape)
print(X_valid.shape, y_valid.shape)
print(X_test.shape, y_test.shape)
```

    (280, 4096) (280,)
    (80, 4096) (80,)
    (40, 4096) (40,)



```python
from sklearn.decomposition import PCA

pca = PCA(n_components=0.99)
pca.fit(X_train)
X_train_pca = pca.transform(X_train)
X_valid_pca = pca.transform(X_valid)
X_test_pca = pca.transform(X_test)
```


```python
pca.n_components_
```




    199




```python
from sklearn.cluster import KMeans

kmeans_per_k = []
k_range = range(5, 150, 5)
for k in k_range:
    print(f"k={k}")
    _ = KMeans(n_clusters=k, random_state=42).fit(X_train_pca)
    kmeans_per_k.append(_)
```

    k=5
    k=10
    k=15
    k=20
    k=25
    k=30
    k=35



```python
from sklearn.metrics import silhouette_score

silhouette_scores = [silhouette_score(X_train_pca, model.labels_) 
                     for model in kmeans_per_k]

best_index = np.argmax(silhouette_scores)
best_k = k_range[best_index]
best_score = silhouette_scores[best_index]

print("best_k: ", best_k)
print("best_score: ", best_score)
```

    best_k:  100
    best_score:  0.2231065



```python
plt.figure(figsize=(8, 3))
plt.plot(k_range, silhouette_scores, "bo-")
plt.xlabel("$k$", fontsize=14)
plt.ylabel("Silhouette score", fontsize=14)
plt.plot(best_k, best_score, "rs")
```




    [<matplotlib.lines.Line2D at 0x17a264cf6a0>]




![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_12_1.png)



```python
inertias = [i.inertia_ for i in kmeans_per_k]
best_inertia = inertias[best_index]

plt.figure(figsize=(8, 3.5))
plt.plot(k_range, inertias, "bo-")
plt.xlabel("$k$", fontsize=14)
plt.ylabel("Inertia", fontsize=14)
plt.plot(best_k, best_inertia, "rs")
plt.show()
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_13_0.png)



```python
best_model = kmeans_per_k[best_index]
best_model
```




    KMeans(n_clusters=100, random_state=42)




```python
def plot_faces(faces, labels, n_cols=5):
    faces = faces.reshape(-1, 64, 64)
    n_rows = (len(faces) - 1) // n_cols + 1
    plt.figure(figsize=(n_cols, n_rows * 1.1))
    for index, (face, label) in enumerate(zip(faces, labels)):
        plt.subplot(n_rows, n_cols, index + 1)
        plt.imshow(face, cmap='gray')
        plt.axis("off")
        plt.title(label)
    plt.show()
```


```python
for cluster_id in np.unique(best_model.labels_):
    print(f"Cluster {cluster_id}")
    in_cluster = best_model.labels_ == cluster_id
    faces = X_train[in_cluster]
    labels = y_train[in_cluster]
    plot_faces(faces, labels)
```

    Cluster 0



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_1.png)


    Cluster 1



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_3.png)


    Cluster 2



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_5.png)


    Cluster 3



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_7.png)


    Cluster 4



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_9.png)


    Cluster 5



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_11.png)


    Cluster 6



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_13.png)


    Cluster 7



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_15.png)


    Cluster 8



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_17.png)


    Cluster 9



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_19.png)


    Cluster 10



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_21.png)


    Cluster 11



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_23.png)


    Cluster 12



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_25.png)


    Cluster 13



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_27.png)


    Cluster 14



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_29.png)


    Cluster 15



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_31.png)


    Cluster 16



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_33.png)


    Cluster 17



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_35.png)


    Cluster 18



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_37.png)


    Cluster 19



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_39.png)


    Cluster 20



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_41.png)


    Cluster 21



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_43.png)


    Cluster 22



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_45.png)


    Cluster 23



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_47.png)


    Cluster 24



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_49.png)


    Cluster 25



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_51.png)


    Cluster 26



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_53.png)


    Cluster 27



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_55.png)


    Cluster 28



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_57.png)


    Cluster 29



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_59.png)


    Cluster 30



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_61.png)


    Cluster 31



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_63.png)


    Cluster 32



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_65.png)


    Cluster 33



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_67.png)


    Cluster 34



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_69.png)


    Cluster 35



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_71.png)


    Cluster 36



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_73.png)


    Cluster 37



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_75.png)


    Cluster 38



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_77.png)


    Cluster 39



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_79.png)


    Cluster 40



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_81.png)


    Cluster 41



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_83.png)


    Cluster 42



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_85.png)


    Cluster 43



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_87.png)


    Cluster 44



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_89.png)


    Cluster 45



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_91.png)


    Cluster 46



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_93.png)


    Cluster 47



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_95.png)


    Cluster 48



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_97.png)


    Cluster 49



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_99.png)


    Cluster 50



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_101.png)


    Cluster 51



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_103.png)


    Cluster 52



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_105.png)


    Cluster 53



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_107.png)


    Cluster 54



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_109.png)


    Cluster 55



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_111.png)


    Cluster 56



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_113.png)


    Cluster 57



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_115.png)


    Cluster 58



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_117.png)


    Cluster 59



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_119.png)


    Cluster 60



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_121.png)


    Cluster 61



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_123.png)


    Cluster 62



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_125.png)


    Cluster 63



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_127.png)


    Cluster 64



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_129.png)


    Cluster 65



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_131.png)


    Cluster 66



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_133.png)


    Cluster 67



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_135.png)


    Cluster 68



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_137.png)


    Cluster 69



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_139.png)


    Cluster 70



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_141.png)


    Cluster 71



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_143.png)


    Cluster 72



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_145.png)


    Cluster 73



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_147.png)


    Cluster 74



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_149.png)


    Cluster 75



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_151.png)


    Cluster 76



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_153.png)


    Cluster 77



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_155.png)


    Cluster 78



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_157.png)


    Cluster 79



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_159.png)


    Cluster 80



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_161.png)


    Cluster 81



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_163.png)


    Cluster 82



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_165.png)


    Cluster 83



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_167.png)


    Cluster 84



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_169.png)


    Cluster 85



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_171.png)


    Cluster 86



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_173.png)


    Cluster 87



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_175.png)


    Cluster 88



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_177.png)


    Cluster 89



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_179.png)


    Cluster 90



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_181.png)


    Cluster 91



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_183.png)


    Cluster 92



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_185.png)


    Cluster 93



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_187.png)


    Cluster 94



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_189.png)


    Cluster 95



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_191.png)


    Cluster 96



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_193.png)


    Cluster 97



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_195.png)


    Cluster 98



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_197.png)


    Cluster 99



![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_16_199.png)


### 计算精度


```python
from scipy import stats
y_pred = best_model.labels_

mapping = {}
for class_id in np.unique(y_train):
    mode, _ = stats.mode(y_pred[y_train==class_id])
    mapping[mode[0]] = class_id

# mapping
```


```python
for _ in y_pred:
    if _ not in mapping.keys():
        mapping[_] = -1
```


```python
y_pred_2 = np.array([mapping[cluster_id] for cluster_id in y_pred ])

np.sum(y_pred_2==y_train) / len(y_train)
```




    0.5107142857142857



大约 3 个集群中有 2 个是有用的：也就是说，它们至少包含 2 张图片，都是同一个人。 然而，其余的集群要么有一个或多个入侵者，要么只有一张图片。

在训练模型时，以这种方式聚类图像可能太不精确而无法直接使用（如下所示），但是在新数据集中标记图像时它可能非常有用：它通常会使标记速度更快。

## 11. 使用聚类作为分类的预处理


```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=150, random_state=42)
clf.fit(X_train_pca, y_train)
clf.score(X_valid_pca, y_valid)
```




    0.9




```python
# 先通过KMeans进行转换，然后用rf预测
X_train_reduced = best_model.transform(X_train_pca)
X_valid_reduced = best_model.transform(X_valid_pca)
X_test_reduced = best_model.transform(X_test_pca)

clf = RandomForestClassifier(n_estimators=150, random_state=42)
clf.fit(X_train_reduced, y_train)
    
clf.score(X_valid_reduced, y_valid)
```




    0.75




```python
from sklearn.pipeline import Pipeline

for n_clusters in k_range:
    pipeline = Pipeline([
        ("kmeans", KMeans(n_clusters=n_clusters, random_state=42)),
        ("forest_clf", RandomForestClassifier(n_estimators=150, random_state=42))
    ])
    pipeline.fit(X_train_pca, y_train)
    print(n_clusters, pipeline.score(X_valid_pca, y_valid))
```

    5 0.4125
    10 0.525
    15 0.5375
    20 0.6375
    25 0.65
    30 0.6375
    35 0.675
    40 0.7375
    45 0.725
    50 0.75
    55 0.7375
    60 0.725
    65 0.7375
    70 0.725
    75 0.725
    80 0.775
    85 0.7375
    90 0.7375
    95 0.75
    100 0.75
    105 0.75
    110 0.7375
    115 0.7375
    120 0.775
    125 0.7875
    130 0.725
    135 0.75
    140 0.7625
    145 0.7375


哦，好吧，即使通过调整集群的数量，我们也永远不会超过 80% 的准确率。 看起来到集群质心的距离不像原始图像那样提供信息。

练习：如果将缩减集中的特征附加到原始特征（同样，搜索最佳聚类数）会怎样？


```python
X_train_extended = np.c_[X_train_pca, X_train_reduced]
X_valid_extended = np.c_[X_valid_pca, X_valid_reduced]
X_test_extended = np.c_[X_test_pca, X_test_reduced]
```


```python
clf = RandomForestClassifier(n_estimators=150, random_state=42)
clf.fit(X_train_extended, y_train)
clf.score(X_valid_extended, y_valid)
```




    0.825



这有点好，但仍然比没有集群功能更糟糕。 在这种情况下，集群对于直接训练分类器没有用（但在标记新训练实例时它们仍然可以提供帮助）。

## 12. Olivetti Faces 数据集的高斯混合模型


```python
from sklearn.mixture import GaussianMixture

gm = GaussianMixture(n_components=40, random_state=42)
y_pred = gm.fit_predict(X_train_pca)
```


```python
n_gen_faces = 20
gen_faces_reduced, y_gen_faces = gm.sample(n_samples=n_gen_faces)
gen_faces = pca.inverse_transform(gen_faces_reduced)
```


```python
plot_faces(gen_faces, y_gen_faces)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_34_0.png)



```python
n_rotated = 4
rotated = np.transpose(X_train[:n_rotated].reshape(-1, 64, 64), axes=[0, 2, 1])
rotated = rotated.reshape(-1, 64*64)
y_rotate = y_train[:n_rotated]

n_flipped = 3
flipped = X_train[:n_flipped].reshape(-1, 64, 64)[:, ::-1]
flipped = flipped.reshape(-1, 64*64)
y_flipped = y_train[:n_flipped]

n_darkened = 3
darkened = X_train[:n_darkened].copy()
darkened[:, 1:-1] *= 0.3
y_darkened = y_train[:n_darkened]

X_bad_faces = np.r_[rotated, flipped, darkened]
y_bad = np.concatenate([y_rotate, y_flipped, y_darkened])

plot_faces(X_bad_faces, y_bad)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_35_0.png)



```python
X_bad_faces_pca = pca.transform(X_bad_faces)
```


```python
gm.score_samples(X_bad_faces_pca)
```




    array([-1.79997493e+07, -2.26427537e+07, -3.96415610e+07, -4.60254504e+07,
           -3.13975264e+07, -1.39330380e+07, -2.90882972e+07, -1.06298636e+08,
           -1.20931045e+08, -7.49740278e+07])



Gaussian Mixture 模型认为这些脸都不太可能出现。 将此与一些训练实例的分数进行比较：


```python
gm.score_samples(X_train_pca[:10])
```




    array([1163.02020812, 1149.1668234 , 1148.47710515, 1170.67602792,
           1088.46009531, 1075.71700184, 1075.71700619, 1088.46008906,
           1096.42609611, 1119.68626932])




```python
def reconstruction_errors(pca, X):
    X_pca = pca.transform(X)
    X_reconstructed = pca.inverse_transform(X_pca)
    mse = np.square(X_reconstructed - X).mean(axis=-1)
    return mse
```


```python
reconstruction_errors(pca, X_train).mean()
```




    0.0001920535




```python
reconstruction_errors(pca, X_bad_faces).mean()
```




    0.004707354




```python
plot_faces(X_bad_faces, y_bad)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_43_0.png)



```python
X_bad_faces_reconstructed = pca.inverse_transform(X_bad_faces_pca)
plot_faces(X_bad_faces_reconstructed, y_bad)
```


![png](ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_files/ch9%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0_%E8%AF%BE%E5%90%8E%E4%BD%9C%E4%B8%9A_44_0.png)



```python

```
