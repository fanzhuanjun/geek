# 一些做过的 py 文件



### 网球王子字幕换名字

```python
import os, re

os.chdir("c:/vlog/")
target_list = os.listdir("c:/vlog/")
# 找到要重新命名的ass文件与相对的mp4的名字
zimu = [i for i in target_list if ".SC.ass" in i]
mp4_list = [i for i in target_list if ("网球王子" in i) and (".mp4" in i)]

# 构建名字字典{"集数": "名字"}
pa = "第(.*?)話"
# mp4_list[0]
mp4_dict = {}
for mp4 in mp4_list:
    num = re.findall(pa, mp4)[0]
    mp4_name = mp4[:-3]
    mp4_dict[int(num)] = mp4_name

for ass in zimu:
    num = int(ass.split('.')[0])
    if num in mp4_dict.keys():
        new_name = mp4_dict[num]+"ass"
        os.rename(ass, new_name)
```


